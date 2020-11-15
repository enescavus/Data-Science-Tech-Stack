#----------------------#
# author: ENES
# date: 15 Nov 2020
# subject: statistisc with python coding
#----------------------#


# Statistics Find _ Mean _ Median and Mode of a list
# this file includes statistics practices - source of these problems is hackerrank Statistics challenge

# note : hacerrank solution down below

#Numbers list 
numbers = [23523, 11735, 35252, 23552, 64545, 23626, 14470, 4978, 56453, 38120, 62353, 12412]

# Mean sometimes called average
# 1 - calculate sum of the all elements in our list
# 2 - Divide the result by ength of the list

# total = 0
# for number in numbers:
#     total += number
# print(total/len(numbers))

# or 

total = sum(numbers)
print("Mean is : " + str(total / float(len(numbers))))

# Median - in the middle
# sort from lowest to the highest number or reverse doesn't matter
# find the middle - if the numbers total count is odd take middle one if not take average of both two middle numbers

numbers.sort() # sort the numbers
# find the middle one or ones
if len(numbers) % 2 == 0:
    print("Median is : " + str(((numbers[len(numbers) // 2 ] ) + (numbers[len(numbers) // 2 - 1 ] )) / float(2) ))
else:
    print("Median is : " + str(numbers[len(numbers) // 2 + 1]))


# Mode is the popular one
# most numbers that are the same are mode 
# find the most repeated number in a list / most frequent
mode = max(sorted(numbers), key=numbers.count) # sorting for selecting the lowest value
# in case all numbers has same frequency
print("Mode is :" + str(mode))




# hacerrank solution

# Enter your code here. Read input from STDIN. Print output to STDOUT
# def mean(numbers):
#     total = sum(numbers)
#     return "{:.1f}".format((total / len(numbers)))
#     #return str(total / len(numbers))
    
# def median(numbers):
#     numbers.sort() # sort the numbers
#     if len(numbers) % 2 == 0:
#         return str(((numbers[len(numbers) // 2 ] ) + (numbers[len(numbers) // 2 - 1 ] )) / 2 )
#     else:
#         return str(numbers[len(numbers) // 2 + 1])
        
# def mode(numbers):
#     mode = max(sorted(numbers), key=numbers.count) 
#     return  str(mode)

# if __name__ == '__main__':
#     n = int(raw_input())
#     numbers = str(raw_input()).split()
#     numbers = map(int,numbers)

#     print(mean(numbers))
#     print(median(numbers))
#     print(mode(numbers))
# source link  https://www.hackerrank.com/challenges/s10-basic-statistics/tutorial


# Mean ()
# The average of all the integers in a set of values. 
# Here is the basic formula for calculating the mean of a set of  values:
# , where  is the  element of the set. 

# Median
# The midpoint value of a data set for which an equal number 
# of samples are less than and greater than the value. 
# For an odd sample size, this is the middle element of the sorted sample; 
# for an even sample size, this is the average of the  middle elements of the sorted sample. 

# Mode
# The element(s) that occur most frequently in a data set. 
# For the set , the mode is  because the number appears three times in the set and every 
# other number in the set has a frequency . In contrast, 
# the set  is multimodal because no number in the set appears more than  time,
#  so every number in the set is a valid mode. 


# check out this link for more : https://www.hackerrank.com/challenges/s10-basic-statistics/tutorial