# -------------------- # 
# author: ENES
# date: 16 Nov 2020
# problem solved: finding STANDART DEVIATION in a list data structure - STATISTICS Questions
# Main source of this problem - please check hackerrrank statistics roblems
# Also check this amazing explanation of std deviation video https://www.youtube.com/watch?v=dq_D30kyR1A
# -------------------- # 

# Input 
nums = [10, 40, 30, 50, 20]

# find the mean
mean = sum(nums) / len(nums)

# find the squared distance for individual value in our list
# we need a total value for sum of the squeared values and then we are going to divide them
# by the lenght of the lest, i mean the number count of the list
total = 0
for i in range(len(nums)):
    total += (nums[i] - mean) ** 2

# divide the total squared value by number counts which is 5 in our case
# then go back to the square root value of this VARIANCE - it's called variance
# and the suared root of the variance is called STANDART DEVIATION

std_dev = round((total / len(nums)) ** (1/2.0),1)
print(std_dev)