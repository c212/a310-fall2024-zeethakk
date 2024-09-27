from s001 import Given

class Heap(Given): # exactly as before
  def __init__(self, key):
    super().__init__(key)
  def size(self): # same as before
    if self.left == None and self.right == None:
      return 1
    elif self.left == None:
      return 1 + self.right.size()
    elif self.right == None:
      return 1 + self.left.size()
    else:
      return 1 + self.right.size() + self.left.size()
  
  def insert(self, value): # one line added
    path = "{0:b}".format(self.size() + 1)
    # print(self.size() + 1, "---> ", path)
    self.helper(path[1:], value)
    self.clean() # this is the new line <---(this is it)---
  
  def helper(self, path, value): # same as before
    if path == "1":
      self.right = Heap(value)
    elif path == "0":
      self.left = Heap(value)
    else:
      nextStep = path[0]
      if nextStep == '0':
        self.left.helper(path[1:], value)
      else:
        self.right.helper(path[1:], value)
  
  def clean(self): # this is a new method
    if self.left != None: self.left.clean() 
    if self.right !=  None: self.right.clean() 
    if self.left == None and self.right == None: # leaf
      pass
    elif self.right == None: # only one child, on the left
      if self.key > self.left.key:
        (self.left.key, self.key) = (self.key, self.left.key)
    else: # two children, do you understand why?
      if self.key <= self.left.key and self.key <= self.right.key:
        pass
      elif self.left.key < self.right.key:
        (self.left.key, self.key) = (self.key, self.left.key)
      elif self.left.key > self.right.key:
        (self.right.key, self.key) = (self.key, self.right.key)
      else:
        pass

# start testing to see how smaller numbers percolate up
print("-------------", 25) 
a = Heap(25)
a.display()
for i in range(24, 20, -1):
  print("------------- insert ", i)
  a.insert(i) 
  a.display()