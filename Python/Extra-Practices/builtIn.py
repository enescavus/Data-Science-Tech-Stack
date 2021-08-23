# https://www.hackerrank.com/challenges/zipped/problem
from statistics import mean

s = input().split()
student1 = map(float,input().split())
student2 = map(float,input().split())
student3 = map(float,input().split())


comb = zip(student1 ,student2, student3 )

for i in list(comb):
    print(mean(i))



# https://www.hackerrank.com/challenges/input/problem

inp = input().split()
def poly(x,y):
    return (x**3 + x**2 + x + 1 ) == y
print(poly(int(inp[0]), int(inp[1])))




# eval built in funciton https://www.hackerrank.com/challenges/python-eval/problem
inp = input()
eval(inp)






# 