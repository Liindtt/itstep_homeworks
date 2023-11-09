from abc import ABC, abstractmethod


class Command(ABC):
    @abstractmethod
    def execute(self):
        ...

    @abstractmethod
    def undo(self):
        ...


class Order:
    def __init__(self):
        self.is_placed = False

    def place_order(self):
        self.is_placed = True
        print("Замовлення розміщено")

    def cancel_order(self):
        self.is_placed = False
        print("Замовлення відмінено")


class PlaceOrderCommand(Command):
    def __init__(self, order):
        self.order = order

    def execute(self):
        self.order.place_order()

    def undo(self):
        self.order.cancel_order()


class CommandController:
    def __init__(self):
        self.commands = []

    def execute_command(self, command):
        command.execute()
        self.commands.append(command)

    def undo_list_command(self):
        if self.commands:
            last_command = self.commands.pop()
            last_command.undo()
        else:
            print("Немає команд для відміни")


order1 = Order()
place_order_command = PlaceOrderCommand(order1)

controller = CommandController()
controller.execute_command(place_order_command)  # Розміщення замовлення
controller.undo_list_command()  # Скасування останнього замовлення



