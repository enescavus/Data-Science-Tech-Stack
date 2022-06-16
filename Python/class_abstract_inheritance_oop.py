# hackerrank class abstract Inheritance problem solution
# problem link --- > https://www.hackerrank.com/challenges/30-abstract-classes/problem?isFullScreen=true

# My solution with super() method and abstract function display

from abc import ABCMeta, abstractmethod
class Book(object, metaclass=ABCMeta):
    def __init__(self,title,author):
        self.title=title
        self.author=author   
    @abstractmethod
    def display(): pass

#Write MyBook class
class MyBook(Book):
  def __init__(self, title, author,price):
    super().__init__(title,author)
    self.price = price
    
  def display(self):
    print("Title:", self.title)
    print("Author:", self.author)
    print("Price:", self.price )
    
title=input()
author=input()
price=int(input())
new_novel=MyBook(title,author,price)
new_novel.display()

#check out the source code - and problem page on hackerrank link below

#### https://www.hackerrank.com/challenges/30-abstract-classes/problem?isFullScreen=true
