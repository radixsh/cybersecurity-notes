# CTF notes
My first attempt to collect cybersecurity resources and create explanatory notes
for myself. I remember things best when I teach them to myself.

## To do 
* dirbuster

### Miscellaneous tips and tricks
* To search for a file by a string in the filename (in the current directory and
  one directory down): `find . -maxdepth 1 -name "*foobar*" -print`
* To find the n most frequent terms in a file: `sed -e 's/\s/\n/g' < test.txt |
  sort | uniq -c | sort -nr | head  -10 `
