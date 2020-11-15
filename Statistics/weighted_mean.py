#----------------------#
# author: ENES
# date: 15 Nov 2020
# subject: statistisc with python coding / weighted_mean
#----------------------#


# Statistics Find weighted mean

# Note : hackerrank solution down below

# The weighted mean is the mean of each value when it's multiplied by some weight ...
# for ecxample , your classes notes are calculation with weighted mean
# if a class is more important it has has bigger weights than the others

values = [10, 40, 30, 50, 20,10,40,30,50,20]
weights = [1,2,3,4,5,6,7,8,9,10]
weighted_total = 0
weights_sum = sum(weights)

for i in range(len(values)):# both length of these lists must be same
    weighted_total += values[i] * weights[i]

print(round(weighted_total / float(weights_sum),1))

# this file includes statistics practices - source of these problems is hackerrank Statistics challenge


# def weighted_mean(values, weights):
#     weighted_total = 0
#     weights_sum = sum(weights)

#     for i in range(len(values)):
#         weighted_total += values[i] * weights[i]

#     return round(weighted_total / float(weights_sum),1)

# if __name__ == '__main__':
#     n = int(raw_input())
#     values = str(raw_input()).split()
#     weights = str(raw_input()).split() #take each value as a unique item for list  
#     values = map(int, values) # convert from string toint
#     weights = map(int, weights)
#     print(weighted_mean(values,weights))

# check this link out for more : https://www.hackerrank.com/domains/tutorials/10-days-of-statistics