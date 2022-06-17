# hackerrank Inheritance problem solution
# problem link --- > https://www.hackerrank.com/challenges/30-interfaces/problem?isFullScreen=true

class AdvancedArithmetic(object):
    def divisorSum(n):
        raise NotImplementedError

#  ---- my code starts here 
class Calculator(AdvancedArithmetic):
  sum_of_divs = 0
  def divisorSum(self, n):
    for i in range(n):
      if n % (i+1) == 0 :
        self.sum_of_divs += i + 1
      else:
        continue
    return self.sum_of_divs
#  ---- my code ends here 


n = int(input())
my_calculator = Calculator()
s = my_calculator.divisorSum(n)
print("I implemented: " + type(my_calculator).__bases__[0].__name__)
print(s)

#check out the source code - and problem page on hackerrank link below

#### https://www.hackerrank.com/challenges/30-interfaces/problem?isFullScreen=true