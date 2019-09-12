#!/usr/bin/env python
"""reducer.py"""

from operator import itemgetter
import sys
import collections

current_word = None
current_count = 0
word = None

wordDict = {}

# input comes from STDIN
for line in sys.stdin:
    # remove leading and trailing whitespace
    line = line.strip()

    # parse the input we got from mapper.py
    word, count = line.split('\t', 1)

    # convert count (currently a string) to int
    try:
        count = int(count)
    except ValueError:
        # count was not a number, so silently
        # ignore/discard this line
        continue

    try :
        wordDict[word] = wordDict[word] + count
    except:
        wordDict[word] = count

    # this IF-switch only works because Hadoop sorts map output
    # by key (here: word) before it is passed to the reducer

wordDict = sorted(wordDict.items(), key= lambda kv:(kv[1],kv[0]), reverse = True)

for word in wordDict:
    print('%s\t%s' % (word[0], word[1]))
