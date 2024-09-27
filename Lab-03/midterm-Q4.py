class BstNode:
    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



class BST(BstNode):
    def __init__(self, name):
        super().__init__(name)
    def insert(self, value):
        a = BST(value)
        a.right = self.right
        self.right = a

# a = BstNode(3)
# a.left = BstNode(5)
# a.left.right = BstNode(1)
# a.display()

# print("------------")
# b = BstNode(7)
# b.left = BstNode(4)
# a.right = b
# a.display()

# print("------------")
# b = BstNode(2)
# b.right = a.right
# a.right = b
# a.display()





class BST(BstNode):
    def __init__(self, name):
        super().__init__(name)
    
    def insert(self, value):
        if self.key == value:
            return
        elif self.key < value:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
        else:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
    
    def find(self, value):
        if self.key == value:
            return True
        elif self.key < value:
            if self.right is None:
                return False
            else:
                return self.right.find(value)
        else:
            if self.left is None:
                return False
            else:
                return self.left.find(value)
    
    def remove(self, value):
        if self.key == value:
            if self.right is None:
                return self.left
            if self.left is None:
                return self.right
            else:
                num = find_largest(self.left)
                self.key = num
                self.left = self.left.remove(num)
        elif self.key < value:
            if self.right:
                self.right = self.right.remove(value)
        else:
            if self.left:
                self.left = self.left.remove(value)
        return self

def find_largest(bst):
    if bst.right is None:
        return bst.key
    else:
        return find_largest(bst.right)

    
a = BST(8)
for num in [1, 9, 7, 2, 6, 4, 5]:
    a.insert(num)
print("Consider this tree")
a.display()
print("If i remove the root:")
a = a.remove(8)
a.display()



# import numpy as np
# a_list = list(np.random.randint(0,100,10))
# print(a)

# a = BST(33)
# for num in a_list:
#     a.insert(num)
    
# a.display()
# a.remove(33)
# a.display()
     