import json
from ctypes import Array


class SortStrategy:
    def sort(self, array: Array) -> None:
        raise NotImplementedError


class BubbleSortStrategy(SortStrategy):
    def sort(self, array: Array) -> None:
        for i in range(len(array) - 1, -1, -1):
            for j in range(0, i):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


class ReverseBubbleSortStrategy(SortStrategy):
    def sort(self, array: Array) -> None:
        for i in range(len(array) - 1, -1, -1):
            for j in range(0, i):
                if array[j] < array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]


class Array:
    def __init__(self, elements: list[int]) -> None:
        if not all(isinstance(x, int) for x in elements):
            raise ValueError("Список 'elements' має містити лише цілі числа")
        self.elements = elements

    def __setitem__(self, index: int, value: int) -> None:
        self.elements[index] = value

    def __getitem__(self, index: int) -> int:
        return self.elements[index]

    def __len__(self) -> int:
        return len(self.elements)

    def is_all_of_type(self, user_type: type) -> bool:
        return all(user_type == type(x) for x in self.elements)

    def print_to_json_file(self, filename: str) -> None:
        with open(filename, "w") as f:
            json.dump(self.elements, f)

    def print_to_txt_file(self, filename: str) -> None:
        with open(filename, "w") as f:
            for x in self.elements:
                f.write(str(x) + "\n")

    def print_to_console(self) -> None:
        for x in self.elements:
            print(x, end=" ")
        print()

    def sort(self, strategy: SortStrategy) -> None:
        strategy.sort(self)

    def add_element(self, element: int) -> None:
        self.elements.append(element)
        print("Додано елемент {} до масиву".format(element))

    def remove_element(self) -> None:
        if not self.elements:
            raise IndexError("Массив пустий")
        element = self.elements.pop(0)
        print("Видалено елемент {} з початку масиву".format(element))

    def get_average(self) -> float:
        if not self.elements:
            return 0
        return sum(self.elements) / len(self.elements)

    def sort_by_direction(self, direction: str) -> None:
        if direction == "ascending":
            self.sort(BubbleSortStrategy())
        elif direction == "descending":
            self.sort(ReverseBubbleSortStrategy())
        else:
            raise ValueError("Невідомий напрямок сортування: {}".format(direction))


array = Array([1, 2, 3, 4, 5])
print(array.is_all_of_type(int))
array.print_to_json_file("array.json")
array.print_to_txt_file("array.txt")
array.print_to_console()
array.sort_by_direction("descending")
array.print_to_console()
print(array.get_average())
array.add_element(6)
array.print_to_console()
print(array.get_average())
array.remove_element()
array.print_to_console()
print(array.get_average())
