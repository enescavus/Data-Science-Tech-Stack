"""
author : Enes Çavuş
subject : itertools
date : 28 Feb 2021
goal : to practice itertools and solve hackerrank questions/problems
sources : https://www.hackerrank.com/dashboard
"""

import itertools

limit = 50 # set a limit
'''
    starts with 3 , increases 9 in every step till reaching the limit
'''
print("--------") # more readable
for i in itertools.count(3,9):
    if i > limit:
        #print("break")
        break
    else:
        print(str(i) + " ")

print("--------") # more readable

'''
    cycling the values giving in cycle function
    repeats 6 (limit we gave ) times
'''
count = 0 # to set a coutner
for i in itertools.cycle("ABCD"):
    if count < 6:
        print(i + " ")
        count  += 1
    else:
        break

print("--------") # more readable

# PRODUCT function like multiple for-loops
# NOTE : this code below written for a hackerrank problem

# # liste = [1,2,3] ##### * this star thing is using for unpacking lists or something
# from itertools import product

# if __name__ == '__main__':
#     line1 = map(int, input().split())    
#     line2 = map(int, input().split())        
#     print(*(product(line1, line2)))

#end