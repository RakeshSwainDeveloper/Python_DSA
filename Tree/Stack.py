class Stack:
    def __init__(self,limit = 10):
        self.stk = []
        self.limit = limit

    def isEmpty(self):
        return len(self.stk) <= 0
    def push(self,item):
        if len(self.stk) >= self.limit:
            print('Stack overflow')
        else:
            self.stk.append(item)
        print('stack after push ',self.stk)
    def pop(self):
        if len(self.stk) <= 0:
            print('Stack Underflow')
            return 0
        else:
            return self.stk.pop()
    def peek(self):
        if len(self.stk) <= 0:
            print('Stack Underflow')
            return 0
        else:
            return self.stk[-1]
    def size(self):
        return len(self.stk)

# our_stk = Stack(5)
# our_stk.push(12)
# our_stk.push(13)
# our_stk.push(14)
# our_stk.push(15)
# our_stk.push(16)

# our_stk.push(17)
# print(our_stk.peek())
# print(our_stk.pop())
# print(our_stk.peek())

class DynamicStack:
    def __init__(self,limit = 10):
        self.stk = limit*[]
        self.limit = limit
    def isEmpty(self):
        return len(self.stk) <= 0
    def resize(self):
        newStack = list(self.stk)
        self.limit = 2 * self.limit
        self.stk = newStack
    def push(self,item):
        if len(self.stk)  >= self.limit:
            self.resize()
        self.stk.append(item)
        print('stack afet push ',self.stk)
    def pop(self):
        if len(self.stk) <= 0:
            print('Stack Underflow')
            return 0
        else :
            return self.stk.pop()
    def peek(self):
        if len(self.stk) <= 0:
            print('Stack UnderFLow')
            return 0
        else:
            return self.stk[-1]
    def size(self):
        return len(self.stk)

our_stack = DynamicStack(5)
our_stack.push(1)
our_stack.push(2)
print('-------------------',our_stack.size())
our_stack.push(3)
our_stack.push(4)
our_stack.push(5)
our_stack.push(6)
our_stack.push(7)
our_stack.push(8)
print(our_stack.peek())
print(our_stack.pop())
print(our_stack.peek())
print('-------------------  ',our_stack.size())


def is_balanced(expression):
    stack = []  # Stack to store opening brackets
    matching_brackets = {')': '(', '}': '{', ']': '['}  # Mapping of closing -> opening

    for char in expression:
        if char in "({[":  # Push opening brackets onto stack
            stack.append(char)
        elif char in ")}]":  # Process closing brackets
            if not stack or stack.pop() != matching_brackets[char]:
                return False  # Mismatch or empty stack

    return len(stack) == 0  # Stack should be empty if balanced


# Test Cases
print(is_balanced("{[()()]}"))
print(is_balanced("{[(])}"))
print(is_balanced("{[}"))
print(is_balanced("((()))"))


