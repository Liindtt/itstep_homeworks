from time import sleep


class User:
    def __init__(self, name: str, phone_number: str = 0):
        self.name = name.title()
        self.phone_number = phone_number  # +38___ _______
        self.number_of_bought_hotdogs = 0
        self.user_discount = 0

    def increment_number_of_bought_hotdogs(self):
        self.number_of_bought_hotdogs += 1

    def discount_for_user(self):
        if self.number_of_bought_hotdogs >= 3:
            self.user_discount = 10
        elif self.number_of_bought_hotdogs >= 10:
            self.user_discount = 10
        return self.user_discount

    def __repr__(self):
        return f"Name: {self.name}, Phone: {self.phone_number}, Bought hotdogs: {self.number_of_bought_hotdogs}, " \
               f"Discount: {self.discount_for_user()}%"

class HotDog:
    def __init__(self, name: str, bread: str, sausage: str, toppings: list, price: int):
        self.name = name
        self.bread = bread
        self.sausage = sausage
        self.toppings = toppings
        self.price = price

    def __repr__(self):
        return f"{self.name}"


class Order:
    def __init__(self, hotdog: HotDog, payment_method: str, discount: int):
        self.hotdog = hotdog
        self.payment_method = payment_method
        self.order_cost = hotdog.price - (hotdog.price * discount / 100)
        self.number_of_order = 1

    def __repr__(self):
        return f"Хотдог: {self.hotdog}, Додатки: {self.hotdog.toppings}, " \
               f"Розрахунок: {self.payment_method}, Ціна: {self.order_cost}"

    def save_order_to_file(self):
        num = self.number_of_order
        with open("all_orders.txt", mode="w") as filename:
            filename.write(f"Замовлення №{num}" + self.__repr__())
            self.number_of_order += 1


class Ingredients:
    def __init__(self):
        self.ingredients = {}

    def add_ingredient(self, name: str, price: int):
        if name in self.ingredients:
            raise ValueError(f"Інгредієнт '{name}' уже є у нашому списку!")
        self.ingredients[f"{name}"] = price

    def remove_ingredients(self, name: str):
        if name in self.ingredients:
            del self.ingredients[f"{name}"]
        else:
            raise ValueError(f"Такого інгредієнта '{name}' у нас немає, або він закінчився")

    def show_all_ingredients(self):
        print("==============================")
        for key, value in self.ingredients.items():
            print(f"Інгредієнт: {key}, К-сть: {value}")


class Store:
    def __init__(self, hotdog: list, ingredients: Ingredients):
        self.classic_hotdogs = hotdog
        self.list_ingredients = ingredients
        self.user_list = []
        self.all_orders = []

    def get_classic_hotdog(self, name):
        for hotdog in self.classic_hotdogs:
            if hotdog.name == name:
                return hotdog
        return None

    def get_user_from_base(self, phone_number):
        for user in self.user_list:
            if user.phone_number == phone_number:
                return user
        return None

    def get_statistic(self):
        count_hotdogs = len(self.all_orders)  # 1 замовлення = 1 хотдог
        total_price = 0
        for order in self.all_orders:
            total_price += order.order_cost
        return count_hotdogs, total_price

    def print_all_ingredients(self):
        for key in self.list_ingredients.ingredients.keys():
            print(f"{key.title()}")

    def print_classic_hotdogs(self):
        for hotdog in self.classic_hotdogs:
            print(f"{hotdog.name}, Ціна: {hotdog.price}")

    def create_order(self):
        while True:
            print("============================")
            print("Вітаємо у нашому кіоску!")
            self.print_classic_hotdogs()
            print("============================")
            current_hotdog_name = input(f"Який хотдог бажаєте?: ").title().rstrip().lstrip()

            if current_hotdog_name in [hotdog.name for hotdog in
                                       self.classic_hotdogs]:  # я зробив тільки реалізацію по готових хотдогах
                user_ingredients = input("Бажаєте якійсь додатки? (так/ні) ").lower().rstrip().lstrip()
                user_hotdog = self.get_classic_hotdog(current_hotdog_name)
                if user_ingredients == "так":
                    self.print_all_ingredients()
                    while True:
                        user_curr_ingredients = input("Які саме додатки бажаєте? "
                                                      "('вихід' для виходу) ").lower().rstrip().lstrip()
                        if user_curr_ingredients in self.list_ingredients.ingredients.keys():
                            user_hotdog.toppings.append(user_curr_ingredients)
                        if user_curr_ingredients == "вихід":
                            break
                else:
                    continue
                user_card = input("У вас є карта постійно клієнта? (так/ні) ").lower().rstrip().lstrip().lstrip()
                if user_card == "так":
                    user_num_phone = input("Введіть свій номер телефону, +38___ _______: ").rstrip()
                    curr_user = self.get_user_from_base(user_num_phone)
                    if curr_user is not None:
                        print("Так, ви у нас зареєстровані)")
                        user_payment_method = input(f"Як будете розраховуватись? "
                                                    f"(карта/готівка): ").lower().rstrip().lstrip()
                        user_order = Order(user_hotdog, user_payment_method, curr_user.discount_for_user())
                        print(f"З вас {user_order.order_cost}")
                        self.all_orders.append(user_order)
                        print(user_order)
                        print(f"{curr_user.name}, очікуйте ваше замовлення!")
                        sleep(5)
                        print(f"{curr_user.name}, ось ваше замовлення, гарного дня вам!")
                        user_order.save_order_to_file()
                        break
                    else:
                        continue
                elif user_card == "ні":
                    print("Тоді швиденько реєструємося)")
                    user_num_phone = input("Введіть свій номер телефону, +38___ _______: ").rstrip().lstrip()
                    user_name = input("Введіть своє ім'я: ")
                    self.user_list.append(User(user_name, user_num_phone))
                    print("Тепер у вас є картка постійного клієнта!")
                    curr_user = self.get_user_from_base(user_num_phone)
                    user_hotdog = self.get_classic_hotdog(current_hotdog_name)
                    user_payment_method = input(f"З вас {user_hotdog.price} гривень\nЯк будете розраховуватись? "
                                                f"(карта/готівка): ").lower().rstrip().lstrip()
                    user_order = Order(user_hotdog, user_payment_method, curr_user.discount_for_user())
                    self.all_orders.append(user_order)
                    print(f"{curr_user.name}, очікуйте ваше замовлення!")
                    sleep(5)
                    print(f"{curr_user.name}, ось ваше замовлення, смачного!")
                    user_order.save_order_to_file()
                    break
            else:
                print("Такого хотдога у нас немає, на жаль")


classic_hotdogs = [
    HotDog("Класичний", "булка", "сосиска варена", ["мариновані огірки"], 50),
    HotDog("Австрійський", "булка", "сосиска з сиром", ["сир"], 60),
    HotDog("Мисливський", "булка", "мисливська ковбаска", ["мариновані огірки", "цибуля", "тушкована капуста"], 75)
]
some_ingredients = ["кетчуп", "гірчиця", "майонез", "томат", "огірок", "перець", "халапеньйо", "сир"]
classic_ingredients = Ingredients()
for item in some_ingredients:
    classic_ingredients.add_ingredient(item, 20)

# початковий користувач для тестування знижки
store = Store(classic_hotdogs, classic_ingredients)
user1 = User("yaroslav", "0683630976")
user1.number_of_bought_hotdogs = 5
store.user_list.append(user1)

while True:
    store.create_order()
    sleep(2)
    tmp_input = input("Бажаєте зробити ще одне замовлення? (так/ні): ").lower().rstrip().lstrip()
    if tmp_input == "так":
        store.create_order()
    elif tmp_input == "ні":
        print("Дякуємо, що завітали до нас, гарного дня вам!")
        break

count_sells_hotdogs, profit = store.get_statistic()
print(f"К-сть проданих хот-догів: {count_sells_hotdogs}, Прибуток: {profit}грн.")
