class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append_to_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node

    def append_to_start(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_a_location(self, data: int, value: int):
        left = self.head
        new_node = Node(value)
        while left is not None:
            if left.data == data:
                new_node.next = left.next
                left.next = new_node
            left = left.next

    def delete_from_end(self):
        if not self.head.next:
            self.head = None
            return
        current = self.head
        while current.next.next:
            current = current.next
        current.next = None

    def delete_from_start(self):
        if self.head:
            self.head = self.head.next

    def delete_value(self, data, count_dels):
        current = self.head
        left = None
        dels = 0
        while current:
            if current.data == data:
                if count_dels < dels:
                    if left:
                        left.next = current.next
                    else:
                        self.head = current.next
                    dels += 1
                else:
                    break
            left = current
            current = current.next

    def replace_value(self, old_value, new_vlue, replace_all=False):
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_vlue
                if not replace_all:
                    break
            current = current.next

    def length(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def iter(self):
        current = self.head
        while current:
            print(f"Node({current.data})", end=" ")
            current = current.next
        print()


lst = LinkedList()
lst.append_to_end(50)
lst.append_to_end(40)

while True:
    menu_input = int(input("============================ Меню ============================\n"
                           "1| Додати елемент у хвіст списку\n"
                           "2| Додати елемент до списку на початок\n"
                           "3| Вставити новий елемент із деяким значенням безпосередньо після елемента із даними, "
                           "що є у списку\n"
                           "4| Видалити елемент з хвоста списку\n"
                           "5| Видалити елемент з голови списку\n"
                           "6| Видалити елемент із деяким значенням у списку\n"
                           "7| Замінити значення у списку на нове значення\n"
                           "8| Визначте розмір списку\n"
                           "9| Показати вміст списку\n"
                           "0| Вихід\n\n"
                           "\tВиберіть бажану операцію >> "))

    if menu_input == 1:
        user_value = int(input("Введіть число яке бажаєте добавити в кінець списку: "))
        lst.append_to_end(user_value)
        print()
    elif menu_input == 2:
        user_value = int(input("Введіть число яке бажаєте добавити на початок списку: "))
        lst.append_to_start(user_value)
        print()
    elif menu_input == 3:
        user_num = int(input("Введіть значення для нового елемента: "))
        user_position = int(input("Введіть елемент, після якого хочете вставити значення: "))
        lst.insert_at_a_location(user_position, user_num)
        print()
    elif menu_input == 4:
        lst.delete_from_end()
        print()
    elif menu_input == 5:
        lst.delete_from_start()
        print()
    elif menu_input == 6:
        user_value = int(input("Введіть значення елементу: "))
        user_count_dels = int(input("Введіть к-сть можливих видалень: "))
        lst.delete_value(user_value, user_count_dels)
        print()
    elif menu_input == 7:
        user_old_value = input("Введіть значення, яке потрібно замінити: ")
        user_new_value = input("Введіть нове значення: ")
        replace_all = input("Замінити всі входження? (так/ні): ").lower().rstrip()
        replace_all = replace_all == "так"
        lst.replace_value(user_old_value, user_new_value, replace_all)
        print()
    elif menu_input == 8:
        print(f"\nДовжина зв'язного списку = {lst.length()}")
        print()
    elif menu_input == 9:
        print("\nВміст списку: ")
        lst.iter()
        print()
    elif menu_input == 0:
        break
    else:
        print("\nОперації з таким номером не існує!")
