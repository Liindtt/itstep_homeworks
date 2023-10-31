from abc import ABC, abstractmethod

class Computer:
    def __init__(self):
        self._processor = None
        self._memory = None
        self._storage = None
        self._graphics_card = None
        self._operating_system = None

    def __str__(self):
        return f"=================================\n" \
               f"Processor: {self._processor}\nMemory: {self._memory}\nStorage: {self._storage}\n" \
               f"Graphics card: {self._graphics_card}\nOperating system: {self._operating_system}" \
               f"\n=================================\n"


class Builder(ABC):
    @abstractmethod
    def add_processor(self, processor):
        pass

    @abstractmethod
    def add_memory(self, memory):
        pass

    @abstractmethod
    def add_storage(self, storage):
        pass

    @abstractmethod
    def add_graphics_card(self, graphics_card):
        pass

    @abstractmethod
    def add_operating_system(self, operating_system):
        pass


class ComputerBuilder(Builder):
    def __init__(self):
        self.computer = Computer()

    def add_processor(self, processor):
        self.computer._processor = processor

    def add_memory(self, memory):
        self.computer._memory = memory

    def add_storage(self, storage):
        self.computer._storage = storage

    def add_graphics_card(self, graphics_card):
        self.computer._graphics_card = graphics_card

    def add_operating_system(self, operating_system):
        self.computer._operating_system = operating_system

    def get_computer(self) -> Computer:
        return self.computer

class Director:
    def __init__(self, builder_: ComputerBuilder):
        self._builder = builder_

    def build_minimal_computer(self, specs: dict):
        self._builder.add_processor(specs['processor'])
        self._builder.add_memory(specs['memory'])
        self._builder.add_storage(specs['storage'])
        self._builder.add_graphics_card(specs['graphics_card'])

    def build_full_computer(self, specs: dict):
        self._builder.add_processor(specs['processor'])
        self._builder.add_memory(specs['memory'])
        self._builder.add_storage(specs['storage'])
        self._builder.add_graphics_card(specs['graphics_card'])
        self._builder.add_operating_system(specs['operating_system'])


specs1 = {
    'processor': 'AMD Ryzen 5 5600G',
    'memory': '8GB',
    'storage': '512GB SSD',
    'graphics_card': 'AMD Radeon Vega 7',
}

specs2 = {
    'processor': 'Intel Core i5-11400F',
    'memory': '16GB',
    'storage': '1TB SSD',
    'graphics_card': 'RTX4060 8GB',
    'operating_system': 'Windows 11',
}


builder = ComputerBuilder()
director = Director(builder)
director.build_minimal_computer(specs1)
comp_min = builder.get_computer()
print(comp_min)

builder2 = ComputerBuilder()
director2 = Director(builder2)
director2.build_full_computer(specs2)
comp_min2 = builder2.get_computer()
print(comp_min2)

