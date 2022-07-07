class Stack:
    def __init__(self):
        self.__stack_list = []

    def push(self, val):
        self.__stack_list.append(val)

    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

stack_object_1=Stack()
stack_object_2=Stack()

stack_object_1.push(45)
stack_object_1.push(46)

stack_object_2.push(25)
stack_object_2.push(26)
stack_object_2.push(stack_object_1.pop())

print(stack_object_1.pop())
print()
print(stack_object_2.pop())
print(stack_object_2.pop())
print(stack_object_2.pop())

