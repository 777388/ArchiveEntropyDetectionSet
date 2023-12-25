import os
import sys
import requests
import time
print("usage eagle.py website")

check = sys.argv[1]
talon = []
def checking(root):
    os.popen("dig +trace " + root)
    e = os.popen("wget -qO - https://web.archive.org/cdx/search/cdx?url=*." + sys.argv[1] + "/*&output=json&fl=original&collapse=urlkey").read()
    for line in e:
        if line in talon:
            continue
        else:
            talon.append(line)

f = lambda d: checking(d) 

roots = []
with open("rootservers.txt", "r") as r:
    for g in r:
        roots.append(g)

(list(map(f, roots)))
print(talon)