import sys
import collections

counter = collections.Counter()
for line in enumerate(open("/Users/aman/PycharmProjects/DIC/BigDataAnalysis/output3/SampleOutput", encoding="utf-8")):
    key, value = line.strip().split("\t", 2)
    counter[key] += int(value)
print counter.most_common(10)