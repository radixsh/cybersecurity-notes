# CTF notes
My first attempt to collect cybersecurity resources and create explanatory notes
for myself. I remember things best when I teach them to myself.

### To do
- [x] Transfer notes from Google Drive to here
- [ ] Transfer links from my years-old bookmarks list here
- [ ] Annotate said links

## Table of contents
1. [Cryptography](cryptography.md)
2. [Networking](networking.md)
3. [OSINT](osint.md)
4. [Reverse-engineering](#reverse-engineering)
5. [Web exploitation](#web-exploitation)
6. [Forensics](#forensics)
7. [Binary exploitation](#binary-exploitation)
8. [Miscellaneous tips and tricks](#miscellaneous-tips-and-tricks)

### Reverse-engineering
* Ghidra
    * [Ghidra: a quick overview](https://0xeb.net/2019/03/ghidra-a-quick-overview)
    * [Ghidra cheatsheet](https://ghidra-sre.org/CheatSheet.html)
    * [Here Be Dragons: Reverse Engineering with Ghidra](https://shogunlab.com/blog/2019/12/22/here-be-dragons-ghidra-1.html)
* [Compiler Explorer](https://godbolt.org)

### Web exploitation
* How to examine HTTP request made when a purchase is made: Inspect
  (Ctrl+Shift+i) < Network, then reload and select any HTTP request on the left
  panel to display it on the right.
* SQL injection
    * To view database: try just typing a space to bring up all names with a
      space (which is all of them, since each entry is `firstName lastName`.
      This is (probably) the SQL being used: `'SELECT name, type FROM USERS
      WHERE name LIKE "%' + query + '%";', so run 1"; SELECT * FROM USERS WHERE
      "%"="`
    * To try to log in: put `' or 1=1 --` as your username#
* dirbuster

### Forensics
* [Autopsy](https://sleuthkit.org/autopsy/docs/user-docs/4.0)
* [Walkthroughs](https://cci.calpoly.edu/2019-digital-forensics-downloads) from
  CCIC 2019

### Binary exploitation
* [Displaying value at address](https://stackoverflow.com/questions/14493707/display-value-found-at-given-address-gdb)

### Miscellaneous tips and tricks
* To search for a file by a string in the filename (in the current directory and
  one directory down): `find . -maxdepth 1 -name "*foobar*" -print`
* To find the n most frequent terms in a file: `sed -e 's/\s/\n/g' < test.txt |
  sort | uniq -c | sort -nr | head  -10 `
* To address `error: gpg failed to sign the data`: see 
  [this Stack Overflow question](https://web.archive.org/web/20200701072347/https://stackoverflow.com/questions/41052538/git-error-gpg-failed-to-sign-data)
* [How to use code snippets in Vim like a cowboy](https://bhupesh.me/learn-how-to-use-code-snippets-vim-cowboy/)

### CTFs
* [NCAE Cyber Games](https://ncaecybergames.org)
