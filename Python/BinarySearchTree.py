# hackerrank python binary search tree problem solution
# problem link --- > https://www.hackerrank.com/challenges/30-binary-search-trees/problem?isFullScreen=true

class Node:
  def __init__(self,data):
    self.right = self.left = None
    self.data = data

class Solution:
  def insert(self,root, data):
    if root == None:
      return Node(data)
    else:
      if data <= root.data:
        cur = self.insert(root.left, data)
        root.left = cur
      else:
        cur = self.insert(root.right , data)
        root.right = cur

    return root

######### --- my code starts here --- ######### 
# recursive  approaches

# one line  return solution  

  # def getHeight(self,root):
  #   #Write your code here

  #   if root is not None:
  #     return max(self.getHeight(root.left), self.getHeight(root.right)) + 1
  #   else:
  #     return -1

  def getHeight(self,root):
    if root is not None:
      left_depth = self.getHeight(root.left)
      right_depth = self.getHeight(root.right)

      if left_depth > right_depth:
        return left_depth + 1
      else:
        return right_depth + 1
    else:
      return -1
######### --- my code ends here --- #########

T=int(input())
myTree=Solution()
root=None
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
height=myTree.getHeight(root)
print(height)  

#check out the source code - and problem page on hackerrank link below

#### https://www.hackerrank.com/challenges/30-binary-search-trees/problem?isFullScreen=true