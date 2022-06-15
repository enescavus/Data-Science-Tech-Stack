# hackerrank Inheritance problem solution
# problem link --- >https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true
class Calculator():
  
  def power(self,n,p):
    if n >= 0 and p >= 0:
      return n ** p
    else:
      raise Exception("n and p should be non-negative")
      

myCalculator=Calculator()
T=int(input())
for i in range(T):
    n,p = map(int, input().split())
    try:
        ans=myCalculator.power(n,p)
        print(ans)
    except Exception as e:
        print(e)   
#check out the source code - and problem page on hackerrank link below

#### https://www.hackerrank.com/challenges/30-exceptions-string-to-integer/problem?isFullScreen=true