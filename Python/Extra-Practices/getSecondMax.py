"""
author : Enes Çavuş
subject : hackerrank solutions
date : 26 Feb 2021
goal : find the second max value in a list - max value can be exist more than once

"""

def getSecondMax(arr):
    '''
        prints result directly (second max value in a list)
    '''
    max_value = max(arr)
    while max_value in arr:
        arr.remove(max_value)
    print(max(arr))

if __name__ == "__main__":
    getSecondMax(arr = [2,3,5,8,8,7])