class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None    # вказує на попередній елемент

    def __repr__(self):
        return f"Node({self.data})"


class Stack:
    def __init__(self, max_size=-1):
        self.head = None
        self.static_max_size = max_size
        self.max_size = max_size

    def push(self, data):
        if self.max_size == 0:
            raise Exception("Stack is overflow!")
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.max_size -= 1

    def pop(self):
        if self.is_empty():
            raise Exception("Stack is empty!")
        else:
            value = self.head.data
            self.head = self.head.next
            self.max_size += 1
            return value

    def is_empty(self):
        return self.head is None

    def is_full(self):
        return self.max_size == 0

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def clear(self):
        self.head = None
        self.max_size = self.static_max_size

    def peek(self):
        if self.head:
            print(self.head.data)

    def iter(self):
        current = self.head
        while current:
            if current.next is None:
                print(current, end="")
                break
            print(current, "-->", end=" ")
            current = current.next

def check_brackets(string):
    stack = Stack()
    for char in string:
        if char == "(":
            stack.push(char)
        elif char == ")":
            if not stack.pop():
                return False
    return stack.is_empty()


s = Stack(3)
s.push("idk")
s.push("idk2")
s.push("idk3")
s.iter()
s.clear()
s.iter()
print("\n")

s.push("?")
s.push("??")
s.iter()
print("\n")

print(f"Розмір стеку: {s.size()}")
print()

s.peek()
print()

s.clear()
print(f"Стек пустий?: {s.is_empty()}")
print(f"Стек переповнений?: {s.is_full()}")
print()

print(check_brackets("((()))"))
print(check_brackets("(()()())"))
print(check_brackets("((())"))
# print(check_brackets("())("))   # Повертає помилку з pop(), бо стек пустий на 3 ітерації
