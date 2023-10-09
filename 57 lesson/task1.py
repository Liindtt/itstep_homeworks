class Book:
    def __init__(self, title, author):
        self._attributes = {"title": title, "author": author}

    def __getattr__(self, name: str):
        print(f"Call __getattr__ {name}")
        if name in self._attributes:
            return self._attributes[f"{name}"]
        else:
            raise AttributeError(f"Book has no attribute '{name}'")

    def __setattr__(self, name, value):
        print(f"Call __setattr__ with {name=}, {value=}")
        if name == "_attributes":
            super().__setattr__(name, value)
        else:
            self._attributes[f"{name}"] = value

    def __delattr__(self, item):
        del self._attributes[item]

    def __getattribute__(self, name):
        print(f"Call __getattribute__ with {name=}")
        if name in ('_attributes', '__dict__'):
            return super().__getattribute__(name)
        else:
            raise AttributeError("that attribute does not exist")


book = Book("Python Programming", "John Zelle")
print(book.__dict__)
print(f"{book.title = }")
print(f"{book.author = }")w
# print(f"{book.year = }")

book.year = 2016
print(book.__dict__)
print(f"{book.year}")
print("----------------------------")

book2 = Book("Python", "John Zelle")
del book2.author
print(book2.__dict__)
print("\n")

print("1-------------------")
book = Book("Python Programming", "John Zelle")
print("2-------------------")
book.year = 2016
print("3-------------------")
print(book.__dict__)
print("4-------------------")
print("book.year=", book.year)
