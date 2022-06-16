import re
import matplotlib.pyplot as plt
import collections
import pandas as pd
import random
import sys
from math import sqrt

# README
# In this function, string is used to receive the text
# p represent a prime number larger than 256 different situtations,in this task e.g. 701
# The limitation of the result (8-bits) = 256 different situtations, therefore we need to mod 256

def hash_function(string,p):
    hash = 0
    k = 0
    for i in string:
        k += 1
        hash += ((p**(len(string)-k)) * ord(i))
    hash = hash % 256
    return hash

# This function is used to extract pure text from "1000_words_uniformity.txt"
def read_words(inputfile):
    with open(inputfile, 'r',encoding='utf-8') as f:
        content = f.read()
        #words = content.split()
        words = re.split('\ |\.|\/|\n',content)
        lst = []
        for word in words:
            # using ASCII to identify punctuation
            for i in word:
                # 39 is "'"
                if ord( i )<39:
                    word = word.replace(i,'')
                # 45 is "-" in the middle of a word
                if 39<ord( i )<45:
                    word = word.replace(i,'')
                # 65 is "A"
                if 45<ord( i )<65:
                    word = word.replace(i,'')
                # 90 is "Z"
                # 97 is "a"
                if 90<ord( i )<97:
                    word = word.replace(i,'')
                # 122 is "z"
                if ord( i )>122:
                    word = word.replace(i,'')
                # remove "-" at the end of the word
                if word.endswith('-'):
                    word = word.replace('-','')
                if word.startswith('-'):
                    word = word.replace('-','')
            if word != "":
                lst.append(word)
        return lst

def mean(lst):
    sum = 0
    for i in lst:
        sum += int(i)
    return round( float(sum / len(lst) ), 4 )
def std(lst):
    avg_lst = mean(lst)
    sum = 0
    for i in lst:
        sum += ( ( int(i) - avg_lst ) ** 2 )
    std = sqrt ( sum / len(lst) )
    return round (std, 4)

# save the words in lst
lst = read_words("1000_words_uniformity.txt")

# save all hash values in lst_hash
# the large prime number is generated from online tool
lst_hash = []
for i in lst:
    hash_value = hash_function(i,701)
    lst_hash.append(hash_value)

b = collections.Counter(lst_hash)
dic = {number: value for number, value in b.items()}
x = [i for i in dic.keys()]
y = []
for i in dic.keys():
    y.append(dic.get(i))
# standard deviation analysis tool
std_hash = std(y)
print(std_hash)
while True:
    print("************************************************************************************************************************")
    selection = int(input(">>>Please make a selection,'1'Hash Function Distribution(Bar Chart),'2'Frequency Distribution Histogram: "))
    if selection == 1:
        # plot "Hash Function Distribution(Bar Chart)""
        plt.xlabel("Hash Values")
        plt.ylabel("Hash Value Occurrences")
        plt.title("Hash Value Occurrences Distribution (1000 words)")
        plt.bar(x,y)
        plt.show()
    elif selection == 2:
        #plot "Frequency Distribution Histogram"
        plt.xlabel("Hash Values")
        plt.ylabel("Frequency")
        plt.title("Frequency Distribution Histogram (1000 words)")
        plt.hist(x,256)
        plt.show()
    else:
        sys.exit("Unvalid Selection! Exit!")