# hackerrank buble sort problem solution
# problem link --- > https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))  # these input lines had already given
    numberOfSwaps = 0
    # Write your code here
    for i in range(len(a)):
      for j in range(len(a)-1):
        if a[j] > a[j+1]:
          temp = a[j+1]
          a[j+1] = a[j]       # swap
          a[j] = temp
          numberOfSwaps += 1
    
    print("Array is sorted in " + str(numberOfSwaps) + " swaps.")
    print("First Element: " + str(a[0]))
    print("Last Element: " + str(a[-1]))

#check out the source code - and problem page on hackerrank link below

#### https://www.hackerrank.com/challenges/30-sorting/problem?isFullScreen=true