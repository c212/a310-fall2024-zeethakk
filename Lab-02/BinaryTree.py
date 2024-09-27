class BinaryTree:
    def __init__(self, value, left, right):
        (self.value, self.left, self.right) = (value, left, right)
    def show(self):
        if self.left == None:
            left = " . "
        else: 
            left = self.left.show()    

        if self.right == None:
            right = " . "
        else: 
            right = self.right.show() 

        return "(" + left + " " + str(self.value) + " " + right + ")"


print("---------------------------Class BinaryTree---------------------------")
a = BinaryTree(4, None, None)
print(a.show())

a = BinaryTree(6, a, None)
print(a.show())

a = BinaryTree(10, BinaryTree(1, None, a), None)
print(a.show())