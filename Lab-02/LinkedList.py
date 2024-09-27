class LinkedList:
    def __init__(self, num, next):
        self.num = num
        self.next = next
        # self.head = None
    def show(self):
        temp = self
        result = ""
        while (temp):
            # print(temp.num)
            result = result + "|" + temp.num + "|"
            temp = temp.next
        print(result)

# NOTE: how to test this?
print("---------------------------Class LinkedList---------------------------")
a = LinkedList("Peanut", None)
a = LinkedList("Butter", a) 
a.show()