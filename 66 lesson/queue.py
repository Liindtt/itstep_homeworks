class Task:
    def __init__(self, task_id: int, name: str, priority: int):
        self.task_id = task_id
        self.name = name
        self.priority = priority
        self.next = None    # вказує на наступний елемент

    def __repr__(self):
        return f"--------------------------------------------------------\n" \
               f"№{self.task_id}\nЗадача: {self.name}\nПріоритет: {self.priority}\n"

class Queue:
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
        self._completed_tasks = 0

    def enqueue(self, task_id, name, priority):
        new_node = Task(task_id, name, priority)
        if self._size == 0:
            self._head = self._tail = new_node
        else:
            curr_node = self._head
            if priority < curr_node.priority:
                new_node.next = self._head
                self._head = new_node
            else:
                while curr_node.next is not None and curr_node.next.priority <= priority:
                    curr_node = curr_node.next
                new_node.next = curr_node.next
                curr_node.next = new_node
        self._size += 1

    def dequeue(self):
        if self._size == 0:
            raise IndexError
        current = self._head
        self._head = current.next
        self._size -= 1
        self._completed_tasks += 1
        if self._size == 0:
            self._tail = None
        return self

    @property
    def size(self):
        return self._size

    @property
    def completed_tasks(self):
        return self._completed_tasks

    def iter(self):
        current = self._head
        while current:
            print(current, end="")
            current = current.next


q = Queue()
q.enqueue(1, "Підготувати звіт про продажі", 3)
q.enqueue(2, "Відправити заказ клієнту A", 1)
q.enqueue(3, "Сформувати презентацію для команди", 3)
q.enqueue(4, "Зателефонувати постачальнику щодо поставки товару.", 2)
q.enqueue(5, "Відправити заказ клієнту B", 1)
q.enqueue(6, "Замовити нове обладнання для офісу.", 2)
q.iter()
print("\n")
print(f"Розмір черги: {q.size}")
print("\n")

q.dequeue()
q.dequeue()
q.iter()
print("\n")
print(f"Розмір черги: {q.size}")
print(f"Виконано завдань: {q.completed_tasks}")


