class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node({self.data}, {self.next.data if self.next else None})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def iter(self):
        current = self.head
        while current:
            print(current, end=" ")
            current = current.next
        print()

    def append(self, data):
        new_node = Node(data)
        if self.tail is None:
            self.head = self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node

    def prepend(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def delete_head(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None

    def delete_tail(self):
        if self.is_empty():
            return
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None

    def traverse_forward(self):
        current = self.head
        while current:
            print(current.data, end="-->")
            current = current.next
        print("None")

    def traverse_backward(self):
        current = self.tail
        while current:
            print(current.data, end="-->")
            current = current.prev
        print("None")

    def delete_by_value(self, value):
        current = self.head
        while current:
            if current.data == value:
                if current == self.head:
                    self.delete_head()
                elif current == self.tail:
                    self.delete_tail()
                else:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                return
            current = current.next

    def insert_at_index(self, data, index):
        if index < 0:
            return
        if index == 0:
            self.prepend(data)
            return
        current = self.head
        i = 0
        while current and i < index:
            current = current.next
            i += 1
        if current:
            new_node = Node(data)
            new_node.prev = current.prev
            new_node.next = current
            current.prev.next = new_node
            current.prev = new_node

    def clear(self):
        self.head = self.tail = None

def print_menu():
    print("==========================================\n"
          "1| Додати елемент в голову\n"
          "2| Додати елемент в хвіст\n"
          "3| Видалити елемент з голови\n"
          "4| Видалити елемент з хвоста\n"
          "5| Видалити елемент за значенням\n"
          "6| Додати новий елемент за індексом\n"
          "7| Прохід по списку від голови до хвоста\n"
          "8| Прохід по списку від хвоста до голови\n"
          "9| Повне очищення списку\n"
          "0| Вихід\n"
          "==========================================")


if __name__ == "__main__":
    dll = DoublyLinkedList()
    while True:
        print_menu()
        choice = int(input(">>> Виберіть опцію: "))
        if choice == 1:
            data = int(input("Введіть значення: "))
            dll.prepend(data)
            dll.iter()
        elif choice == 2:
            data = int(input("Введіть значення: "))
            dll.append(data)
            dll.iter()
        elif choice == 3:
            dll.delete_head()
            dll.iter()
        elif choice == 4:
            dll.delete_tail()
            dll.iter()
        elif choice == 5:
            data = int(input("Введіть значення для видалення: "))
            dll.delete_by_value(data)
            dll.iter()
        elif choice == 6:
            data = int(input("Введіть значення: "))
            index = int(input("Введіть індекс: "))
            dll.insert_at_index(data, index)
            dll.iter()
        elif choice == 7:
            dll.traverse_forward()
            dll.iter()
        elif choice == 8:
            dll.traverse_backward()
            dll.iter()
        elif choice == 9:
            dll.clear()
            dll.iter()
        elif choice == 0:
            break
        else:
            print("Невірний вибір. Спробуйте ще раз.")
