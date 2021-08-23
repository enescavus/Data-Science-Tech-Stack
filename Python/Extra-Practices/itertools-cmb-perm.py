# the problem is https://www.hackerrank.com/challenges/2d-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays 
# solved by Enes Çavuş
# Arrays in Python 
s, i = input().split() # get itnput 
from itertools import combinations # import libs

for x in range(1, int(i)+1): # need a 1 to n loop ,extra addition for getting the last item value
    
    for comb in list(combinations(sorted(s),x)): # firstly sorted stirng, then x amount of combination
                                                 # then converting into list
        print(''.join(comb))

# product
from itertools import product

if __name__ == '__main__':
    line1 = map(int, input().split())    
    line2 = map(int, input().split())        
    print(*(product(line1, line2)))

# permutation
from itertools import permutations

word, num = input().split(" ")
outp = list(permutations(word, int(num)))
outp.sort()

for i in outp:
    print("".join(i))

# END 
