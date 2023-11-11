from abc import ABC, abstractmethod


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinarySearchTree(ABC):
    @abstractmethod
    def insert(self, value):
        pass

    @abstractmethod
    def search(self, value):
        pass

    @abstractmethod
    def find_min(self):
        pass

    @abstractmethod
    def delete(self, value):
        pass


class MyBinarySearchTree(BinarySearchTree):
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = Node(value)
        else:
            self._insert(value, self.root)

    def _insert(self, value, current_node):
        if value < current_node.value:
            if current_node.left is None:
                current_node.left = Node(value)
            else:
                self._insert(value, current_node.left)
        else:
            if current_node.right is None:
                current_node.right = Node(value)
            else:
                self._insert(value, current_node.right)

    def search(self, value):
        if self.root is None:
            return None
        else:
            return self._search(value, self.root).value

    def _search(self, value, current_node):
        if current_node is None:
            return None
        if current_node.value == value:
            return current_node
        elif value < current_node.value:
            return self._search(value, current_node.left)
        else:
            return self._search(value, current_node.right)

    def find_min(self):
        if self.root is None:
            return None
        else:
            return self._find_min(self.root)

    def _find_min(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node

    def delete(self, value):
        if self.root is None:
            return
        else:
            self._delete(value, self.root)

    def _delete(self, value, current_node):
        if value == current_node.value:
            if current_node.left is None and current_node.right is None:
                # листок
                self.root = None
            elif current_node.left is None:
                # один дочірній вузол (правий)
                current_node = current_node.right
            elif current_node.right is None:
                # один дочірній вузол (лівий)
                current_node = current_node.left
            else:
                # два дочірніх вузла
                successor = self._find_min(current_node.right)
                current_node.value = successor.value
                self._delete(successor.value, current_node.right)
        elif value < current_node.value:
            self._delete(value, current_node.left)
        else:
            self._delete(value, current_node.right)


tree = MyBinarySearchTree()

# додаємо вузли до дерева
for value in [12, 19, 8, 4, 10, 5, 21, 11, 15, 9, 1, 14, 16]:
    tree.insert(value)

# перевіряємо наявність вузла в дереві
if tree.search(tree.root.value) is not None:  # True
    print(tree.search(tree.root.value))  # 12
else:
    print("Value not found")

if tree.search(tree.root.left.value) is not None:  # True
    print(tree.search(tree.root.left.value))  # 8
else:
    print("Value not found")
