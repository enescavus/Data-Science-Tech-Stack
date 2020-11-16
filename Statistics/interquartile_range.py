# -------------------- # 
# author: ENES
# date: 16 Nov 2020
# problem solved: finding interquartile range in a list data structure - STATISTICS Questions
# -------------------- # 


# Interquartile range is the difference between first and the third(last) quartiles
# check the quartile solution python file before this code....


# input arrays , first one is the numbers , second one is the frequency of the first array
# as an example [1,2,3] ; [2,3,1], main array will be like [1,1,2,2,2,3]
# Note: both arrays must have same range of the data
# we are going go find interquartile for this new created data structure


### FUNCTIONS 

def findTheInterQuartile(numbers):
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

    return findTheMedian(highest_half) - findTheMedian(lowest_half)


def findTheMedian(numbers):
    sortedLst = sorted(numbers)
    lstLen = len(numbers)
    index = (lstLen - 1) // 2
   
    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

#### End of the functions section 


# Inputs
elements = [10, 40, 30, 50, 20, 10, 40, 30, 50, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
frequencies = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 40, 30, 50, 20, 10, 40, 30, 50, 20]
main_list = []

# expand the main list
for i in range(len(elements)):
    for j in range(frequencies[i]):
        main_list.append(elements[i])

main_list.sort()
print(float(findTheInterQuartile(main_list)))

