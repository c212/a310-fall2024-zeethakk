from s001 import Given

class Heap(Given): # we inherit from the previous stage code
  
  def __init__(self, key): # notice the constructor chaining
    super().__init__(key)
  # display is inherited (along with its recursive helper)
  
  def size(self): # necessary to determine new insert location
    if self.left == None and self.right == None:
      return 1
    elif self.left == None:
      return 1 + self.right.size() 
    elif self.right == None:
      return 1 + self.left.size()
    else:
      return 1 + self.right.size() + self.left.size()
  
  def insert(self, value): # this is the insert function
    path = "{0:b}".format(self.size() + 1)
    # it uses the binary representation of heap size to locate
    self.helper(path[1:], value)
    
  def helper(self, path, value): # helper for insert
    # if path is one character long: time to add
    if path == "1": # insert leaf as the right child
      self.right = Heap(value)
    elif path == "0": # insert leaf as left child
      self.left = Heap(value)
    else: # otherwise recursively move down the path
      nextStep = path[0]
      if nextStep == '0':
        self.left.helper(path[1:], value)
      else:
        self.right.helper(path[1:], value)

print("-------------", 100) # insert 100 in empty tree
a = Heap(100)
a.display()
for i in range(25, 20, -1): 
  # then keep inserting 25, 24, ... 22, 21 and stop at 20 (w/out 20)
  print("------------- insert ", i)
  a.insert(i) 
  a.display()
  # note that at this stage no promotion occurs for smaller numbers