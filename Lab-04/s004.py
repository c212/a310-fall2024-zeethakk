from s001 import Given

class Heap(Given):
  def __init__(self, key):
    super().__init__(key)
  
  def size(self):
    if self.left == None and self.right == None:
      return 1
    elif self.left == None:
      return 1 + self.right.size();
    elif self.right == None:
      return 1 + self.left.size()
    else:
      return 1 + self.right.size() + self.left.size()
  
  def insert(self, value):
    path = "{0:b}".format(self.size() + 1)
    self.helper(path[1:], value)
    self.clean()
  
  def helper(self, path, value):
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
  
  def clean(self): # clean used by insert, so we need clean for remove now
    if self.left != None: self.left.clean()
    if self.right !=  None: self.right.clean()
    if self.left == None and self.right == None:
      pass
    elif self.right == None:
      if self.key > self.left.key:
        (self.left.key, self.key) = (self.key, self.left.key)
    elif self.left == None:
      if self.key > self.right.key:
        (self.right.key, self.key) = (self.key, self.right.key)
    else:
      if self.key <= self.left.key and self.key <= self.right.key:
        pass
      elif self.left.key < self.right.key:
        (self.left.key, self.key) = (self.key, self.left.key)
      else:
        (self.right.key, self.key) = (self.key, self.right.key)
  
  # new code added here
  def removeTop(self):
    print("Removing the top.")
    path = "{0:b}".format(self.size()) # find path to the last element
    value = self.helperRemove(path[1:]) # pull the value from that node
    self.key = value # and place it in the root, then cut value from tree
    p = self
    last = path[-1]
    for c in path[1:-1]:
      if c == "0":
        p = p.left
      else:
        p = p.right
    if last == "0":
      p.left = None
    else:
      p.right = None
    # self.clean() # we need to percolate the value down if needed
    return self
  
  # new helper method, helping with remove
  def helperRemove(self, path):
    if path == "1": return self.right.key
    elif path == "0": return self.left.key
    else:
      nextStep = path[0]
      if nextStep == '0':
        return self.left.helperRemove(path[1:])
      else:
        return self.right.helperRemove(path[1:])
  # this looks very similar to the previous helper

# start testing
print("First some insertions, starting from the empty heap...\n-------------", 25) 
a = Heap(25)
a.display()
for i in range(24, 18, -1):
  print("------------- insert ", i)
  a.insert(i) 
  a.display()
# new test, removing the top five times
print("Now we start removing the top...")
for i in range(5):
  a = a.removeTop()
  a.display()