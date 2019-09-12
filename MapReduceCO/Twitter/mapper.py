#!/usr/bin/env python
"""mapper.py"""

import sys
myWords = ["football","messi","fifa","nba","game","one","like","team","fbi","win"]

for line in sys.stdin:
    line = line.strip()
    line = line.lower()
    words = line.split()
    for myWord in myWords:
        for i in range(0, len(words)-1):
            if words[i] == myWord:
                print("%s,%s\t%s" % (words[i],words[i+1], 1))