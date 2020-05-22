import random
import os

def ascii_sum(key):
    sum = 0
    for c in key:
        sum += ord(c)

    return sum

letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM-_"
keys = []
key = ""
while len(keys) < 10:
    key += random.choice(letters)
    sum = ascii_sum(key)
    if sum > 916:
        key = ""
    elif sum == 916:
        keys.append(key)

for k in keys:
    print(k)
