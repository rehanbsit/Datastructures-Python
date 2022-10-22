from exceptions import NoneElementException, EmptyStackException


class Stack:

    def __init__(self):
        self.total = 0
        self.elements = []

    def size(self):
        return self.total

    def push(self, element):
        if element is not None:
            self.elements.append(element)
            self.total += 1
        else:
            raise NoneElementException()

    def pop(self):
        if self.total > 0:
            self.total -= 1
            return self.elements.pop()
        else:
            raise EmptyStackException()

    def peek(self):
        if self.total > 0:
            return self.elements[-1]
        else:
            raise EmptyStackException()

    def empty(self):
        return True if self.total == 0 else False


if __name__ == '__main__':
    stack = Stack()
    print(stack.pop())
    stack.push(10)
    stack.push(9)
    stack.push(8)
    stack.push(7)
    stack.push(6)
    stack.push(5)
    print(stack.size())
    print(stack.pop())
    print(stack.peek())
    print(stack.empty())
