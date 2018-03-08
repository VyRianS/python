#!/usr/bin/python3.6

# CLASSES

class MyClass:

  # Data attributes will OVERRIDE class methods
  # Best to have a convention for class methods
  # Maybe start method name with a _

  # this variable is shared by ALL instances of this class
  # unbound_list = []

  # Default initialization method
  # Will be called when class is instantialized
  def __init__(self, realpart, imagpart):
    self.r = realpart
    self.i = imagpart

  def f(self):
    return 'Helloworld!'

class Reverse:

  def __init__(self,data):
    self.data = data
    self.index = len(data)

  # Use __iter__(self) to return the object with a __next__(self) for iteration
  def __iter__(self):
    return self

  def __next__(self):
    if self.index == 0:
      raise StopIteration
    self.index -= 1
    return self.data[self.index]

if __name__ == '__main__':
  x = Reverse('spam')
  iter(x)
  for char in x:
    print(char)