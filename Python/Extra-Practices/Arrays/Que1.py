# the problem is https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays 
# solved by Enes Çavuş
# Arrays in Python 

import numpy as np # to make a random 2D array - pip install numpy
arr = [[np.random.randint(-5,15) for i in range(4)] for j in range(10) ]
print(arr)

rows = len(arr)
cols = len(arr[0])  # it has 3 so we got 2 as the max indessx number for this 3 column and 3 rows array
# print(len(arr)) # row count
# print(len(arr[0])) # column count
# print(arr[1][1])

hoursGlassArr2D = [[0 for i in range(cols-2)] for j in range(rows-2)] # nested list assignment 
print(type(hoursGlassArr2D))
for i in range(rows - 2):
    for j in range(cols -2):
        number = 0
        number = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]        #print(number)
        hoursGlassArr2D[i][j] = number
print(hoursGlassArr2D)
print(max(map(max, hoursGlassArr2D))) # get max mapping
print(np.amax(hoursGlassArr2D)) # fun an easy way with numpy - get max 

# END 