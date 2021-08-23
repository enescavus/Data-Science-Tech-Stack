# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem

def average(array):
    # your code goes here
    return float(sum(set(array)) / len(set(array)))

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)

# https://www.hackerrank.com/challenges/py-set-add/problem

s = input()

countries = set()
for country in range(int(s)):
    country = input()
    countries.add(country)
    
print(len(countries))

# https://www.hackerrank.com/challenges/symmetric-difference/problem

x,set1, y , set2 = input(), input().split() ,input(), input().split()
set1 = set(set1)
set2 = set(set2)


set3 = set1.difference(set2).union(set2.difference(set1))
print('\n'.join(sorted(set3, key=int)))



# cmdDict = {}
for cmd in range(int(input())):
    new_input = input().split()
    if new_input[0] == "pop":
        s.pop()
    elif new_input[0] == "remove":
        s.remove(int(new_input[1]))
    elif new_input[0] == "discard":
        s.discard(int(new_input[1]))
print(sum(s))

# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem
cmdDict = {}
for cmd in range(int(input())):
    new_input = input().split()
    if new_input[0] == "pop":
        s.pop()
    elif new_input[0] == "remove":
        s.remove(int(new_input[1]))
    elif new_input[0] == "discard":
        s.discard(int(new_input[1]))
print(sum(s))


#  https://www.hackerrank.com/challenges/py-set-intersection-operation/problem
n1,set1,n2,set2 = input(),input().split(),input(),input().split()

set1 = set(set1)
set2 = set(set2)

print(len(set1.intersection(set2)))

#https://www.hackerrank.com/challenges/py-set-difference-operation/problem
n1, set1, n2, set2 = input(), set(map(int,input().split())), input(), set(map(int, input().split()))

print(len(set1.difference(set2)))

# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem
n1, s1, n2, s2 = input(), set(map(int,input().split())), input(), set(map(int,input().split()))

print(len(s1.symmetric_difference(s2)))

