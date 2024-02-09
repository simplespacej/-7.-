class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None

    def size(self):
        return len(self.items)

def is_balanced(s):
    stack = Stack()
    pairs = {'(': ')', '[': ']', '{': '}'}

    for char in s:
        if char in pairs:
            stack.push(char)
        elif char in pairs.values():
            if stack.is_empty() or pairs[stack.pop()] != char:
                return "Несбалансированно"
    return "Сбалансированно" if stack.is_empty() else "Несбалансированно"

print(is_balanced("(((([{}]))))"))
print(is_balanced("[([])((([[[]]])))]{()}"))
print(is_balanced("{{[()]}}"))
print(is_balanced("}{"))
print(is_balanced("{{[(])]}}"))
print(is_balanced("[[{())}]"))