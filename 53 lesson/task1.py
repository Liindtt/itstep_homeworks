class Printer:
    def does(self):
        return 'print'


class Lamp:
    def does(self):
        return 'lamp'


class Car:
    def does(self):
        return 'ride'


class Robot:
    def __init__(self):
        self.print = Printer()
        self.lamp = Lamp()
        self.ride = Car()

    def do_it(self):
        print(f"Робот виконує такі функції: {self.lamp.does()}, {self.print.does()}, {self.ride.does()}")


robot = Robot()
robot.do_it()
