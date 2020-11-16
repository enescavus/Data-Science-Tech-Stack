# -------------------- # 
# author: ENES
# date: 16 Nov 2020
# problem solved: finding quartiles in a list data structure - STATISTICS Questions
# Main source of this problem - please check the link at bottom of this code
# -------------------- # 



# Q1: The first quartile is the middle number between the smallest number in a dataset and it's median.   
# Q2: The second quartile is the median
# Q3: The third quartile is the middle number betwwen the highest number in a dataset and its median.



# find the median function  all quartiles actually a median of an another list
def findTheMedian(numbers):
    sortedLst = sorted(numbers)
    print(sortedLst)
    lstLen = len(numbers)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return int(sortedLst[index])
    else:
        return int((sortedLst[index] + sortedLst[index + 1])/2.0)
    
#input

numbers = [4, 17, 7, 14, 18, 12, 3, 16, 10, 4, 4, 12]
lowest_half = []
highest_half = []

if len(numbers) % 2 != 0:
    numbers.sort()
    lowest_half = numbers[:(len(numbers) // 2 ) ]
    highest_half = numbers[((len(numbers) // 2 ) + 1) : ]
elif len(numbers) % 2 == 0:
    numbers.sort()
    lowest_half = numbers[:(len(numbers) // 2 ) ]
    highest_half = numbers[(len(numbers) // 2 ) : ]


print(findTheMedian(lowest_half))
print(findTheMedian(numbers))   
print(findTheMedian(highest_half))



# soruce link : https://www.hackerrank.com/challenges/s10-quartiles/tutorial 