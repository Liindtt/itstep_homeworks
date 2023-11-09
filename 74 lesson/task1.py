class Store:
    def __init__(self):
        self.categories = []

    def add_category(self, name):
        category = Category(name)
        self.categories.append(category)
        return category

    def get_all_products_price(self):
        all_products_price = 0
        for category in self.categories:
            all_products_price += category.products.price
        return all_products_price


class Category:
    def __init__(self, name):
        self.name = name
        self.subcategories = []

    def add_subcategory(self, name):
        subcategory = SubCategory(name)
        self.subcategories.append(subcategory)
        return subcategory

    def remove_subcategory(self, name):
        for subcategory in self.subcategories:
            if subcategory.name == name:
                self.subcategories.remove(subcategory)

    def get_all_category_price(self):
        category_products_price = 0
        for subcategory in self.subcategories:
            category_products_price += subcategory.products.price
        return category_products_price

    def __repr__(self):
        return f"Назва категорії: {self.name}\n Підкатегорії: {self.subcategories}\n"


class SubCategory:
    def __init__(self, name):
        self.name = name
        self.products = []

    def add_product(self, product_name, price):
        product = Product(product_name, price)
        self.products.append(product)
        return product

    def remove_product(self, name):
        for product in self.products:
            if product.name == name:
                self.products.remove(product)

    def __repr__(self):
        return f"\n\tПідкатегорія: {self.name}\n\t\t Товар: {self.products}\n"


class Product:
    def __init__(self, product_name, price):
        self.name = product_name
        self.price = price

    def get_price(self):
        return self.price

    def __repr__(self):
        return f"\n\t\t\tТовар: {self.name}, Ціна: {self.price}$"


store = Store()
electronics = store.add_category("Електроніка")
furniture = store.add_category("Меблі")

smartphones = electronics.add_subcategory("Смартфони")
laptops = electronics.add_subcategory("Ноутбуки")

smartphones.add_product("Iphone 14 Pro", 980)
smartphones.add_product("Realme 6", 330)
smartphones.add_product("Xiaomi Redmi Note 9 Pro", 280)

laptops.add_product("Acer Nitro 5", 740)
laptops.add_product("Lenovo IdeaPad 3", 660)

print(electronics)

laptops.remove_product("Lenovo IdeaPad 3")
print(electronics)
