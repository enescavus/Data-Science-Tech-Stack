# hackerrank Python Scope (global_local variable understanding) problem solution
# problem link --- > https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true

# My solution with super() method and abstract function display

class Difference:
    def __init__(self, a):
        self.__elements = a
  # Add your code here
    def computeDifference(self):
      self.maximumDifference = abs(min(self.__elements) - max(self.__elements))
        
# End of Difference class
_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)

#check out the source code - and problem page on hackerrank link below

# https://www.hackerrank.com/challenges/30-scope/problem?isFullScreen=true
