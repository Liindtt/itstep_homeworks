from abc import ABC, abstractmethod

# Інтерфейс патерну "Репозиторій" для зберігання даних
class Repository(ABC):
    @abstractmethod
    def add(self, obj):
        raise NotImplementedError

    @abstractmethod
    def remove(self, obj):
        raise NotImplementedError

    @abstractmethod
    def get_data(self):
        raise NotImplementedError

# Моделі
class Car:
    def __init__(self, vendor_name: str, car_year: int, model: str, cost: int, sale_price: int):
        self.vendor_name = vendor_name
        self.car_year = car_year
        self.model = model
        self.cost = cost
        self.sale_price = sale_price

    def __repr__(self):
        return f"• Назва виробника: {self.vendor_name}\n" \
               f"• Рік випуску: {self.car_year}\n" \
               f"• Модель: {self.model}\n" \
               f"• Собівартість: {self.cost}$\n" \
               f"• Потенційна ціна продажу: {self.sale_price}$\n"


class Employee:
    def __init__(self, first_name: str, second_name: str, post: str):
        self.first_name = first_name
        self.second_name = second_name
        self.post = post
        self.personal_sales = []

    def __repr__(self):
        return f"• Прізвище та ім'я: {self.second_name} {self.first_name}\n" \
               f"• Посада: {self.post}\n" \
               f"• Продажі: {[f'Машина: {sale.car.vendor_name} {sale.car.model} {sale.car.car_year}року, Ціна: {sale.real_price}$' for sale in self.personal_sales]}\n"


class Sale:
    def __init__(self, employee: Employee, car: Car, real_price: int):
        self.employee = employee
        self.car = car
        self.real_price = real_price

    def __repr__(self):
        return f"Співробітник: {self.employee.first_name} {self.employee.second_name}\n" \
               f"Автомобіль: {self.car.vendor_name} {self.car.model}, {self.car.car_year} року\n" \
               f"Реальна ціна продажу: {self.real_price}$\n"

class CarRepository(Repository):
    def __init__(self):
        self.cars = []

    def add(self, car: Car):
        self.cars.append(car)

    def remove(self, car):
        for item in self.cars:
            if item.vendor_name == car.vendor_name and item.car_year == car.car_year and item.model == car.model:
                self.cars.remove(item)

    def get_data(self):
        return self.cars

class EmployeeRepository(Repository):
    def __init__(self):
        self.employees = []

    def add(self, employee):
        self.employees.append(employee)

    def remove(self, employee):
        for item in self.employees:
            if item.first_name == employee.first_name and \
                    item.second_name == employee.second_name and item.post == employee.post:
                self.employees.remove(item)

    def get_data(self):
        return self.employees

class SaleRepository(Repository):
    def __init__(self):
        self.sales = []

    def add(self, sale):
        self.sales.append(sale)

    def remove(self, sale):
        for item in self.sales:
            if item.employee == sale.employee and item.car == sale.car and item.real_price == sale.real_price:
                self.sales.remove(item)

    def get_data(self):
        return self.sales

# Контролер
class MotorShow:
    def __init__(self):
        self.cars = CarRepository()
        self.employees = EmployeeRepository()
        self.sales = SaleRepository()

    def add_employee(self, new_employee: Employee):
        self.employees.add(new_employee)

    def remove_employee(self, new_employee: Employee):
        self.employees.remove(new_employee)

    def add_car(self, new_car: Car):
        self.cars.add(new_car)

    def remove_car(self, new_car: Car):
        self.cars.remove(new_car)

    def add_sale(self, new_sale: Sale):
        new_sale.employee.personal_sales.append(new_sale)
        self.sales.add(new_sale)

    def remove_sale(self, new_sale: Sale):
        new_sale.employee.personal_sales.remove(new_sale)
        self.sales.remove(new_sale)

    def get_employees(self):
        return self.employees.get_data()

    def get_cars(self):
        return self.cars.get_data()

    def get_sales(self):
        return self.sales.get_data()


# Створення Автосалону
controller = MotorShow()

# Додавання співробітників
employee1 = Employee("Іванов", "Іван", "Продавець")
employee2 = Employee("Николайчук", "Ярослав", "Продавець")
controller.add_employee(employee1)
controller.add_employee(employee2)

# Додавання машин
car1 = Car("Volkswagen", 2023, "Tiguan", 50000, 60000)
car2 = Car("Nissan", 2018, "Qashqai", 20000, 28000)
controller.add_car(car1)
controller.add_car(car2)

# Додавання продажів
sale1 = Sale(employee2, car1, 56000)
sale2 = Sale(employee2, car2, 27000)
controller.add_sale(sale1)
controller.add_sale(sale2)

# Тіло програми
while True:
    print("""===============================================================
1 | Повну інформацію про співробітників фірми та його продажі.
2 | Повну інформацію про автомобілі.
3 | Повну інформація про продажі та їх сумарний прибуток.
    
9 | Вихід.
===============================================================""")
    choice = int(input("Виберіть опцію: "))
    if choice == 1:
        for value in controller.get_employees():
            print(value)
    elif choice == 2:
        for value in controller.get_cars():
            print(value)
    elif choice == 3:
        # тестування на видалення продажу
        controller.remove_sale(sale2)
        summary_product = 0
        for value in controller.get_sales():
            summary_product += value.real_price - value.car.cost
            print(value)
        print(f"Сумарний прибуток: {summary_product}$")
    elif choice == 9:
        break
    else:
        print("Такої операції не існує, спробуйте знову")
