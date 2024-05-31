class Person:
  def __init__(self, first, last):
    self.first = first
    self.last = last

  def reverse(self):
    print(f"{self.last} {self.first}")
a=input("FIRST NAME: ")
b= input("LAST NAME: ")
person = Person(a,b)
person.reverse()