# left rotation

# arr = [1,2,3,4,5]
# rotation left number 2 - each items moves 2 steps back/left 
# expected output 3 4 5 1 2

arr = [1,2,3,4,5]
rotate = 2


# the quick way with collections

from collections import deque
d = deque()
d.extend(arr)
d.rotate(-2)

print("This is d : moved 2 steps back/left", *d)
# print("This is d : moved 2 steps forward/right", *d) # use rotate(2)




def rotateIt(arr, rotNum):
    rotatedArray = list(arr)
    for i in range(rotNum):
        rotatedArray.append(rotatedArray[0])
        rotatedArray.pop(0)

    return rotatedArray

# OR in an anoter way - but way more complicated and long

# rotations functin 
# def rotateIt(arr, rotNum):
#     rotatedArray = list(arr)
#     rotatedArray.append(0)
#     for i in range(rotNum):
#         rotatedArray[-1] = rotatedArray[0]
#         rotatedArray.pop(0)
#         rotatedArray.append(0)
#     rotatedArray.pop(-1)
#     return rotatedArray


print(rotateIt(arr,2))


