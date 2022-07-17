# python 3.7
"""
Challenge 2:
Write a solution to find the character that has the highest number of occurrences within a certain string, ignoring  case. If there is more than one character with equal highest occurrences, return the character that appeared first  within the string.
For example:
 Input: "Character"
 Output: c
"""
import collections

d = collections.defaultdict(int)
strinput = input("Please input your string:")
strinput.lower()
for i in strinput:
    d[i] += 1
print(d)
print(max(d, key=d.get))
