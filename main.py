#!/usr/local/bin/python3.9
import math
import json
import random

global dash
dash = "-"

with open("words.json", "r") as w:
    data = json.load(w)

    int1 = random.randint(1, 6)
    int2 = random.randint(1, 6)
    int3 = random.randint(1, 6)
    int4 = random.randint(1, 6)
    int5 = random.randint(1, 6)

    number1 = str(int1) + str(int2) + str(int3) + str(int4) + str(int5)
    number2 = str(int5) + str(int4) + str(int3) + str(int1) + str(int1)
    number3 = str(int5) + str(int2) + str(int4) + str(int1) + str(int3)
    number4 = str(int4) + str(int1) + str(int2) + str(int5) + str(int3)
    number5 = str(int2) + str(int3) + str(int4) + str(int5) + str(int1)

word1 = data[number1]
word2 = data[number2]
word3 = data[number3]
word4 = data[number4]
word5 = data[number5]

passphrase = word1 + dash + word2 + dash + word3 + dash + word4 + dash + word5

print(passphrase)
