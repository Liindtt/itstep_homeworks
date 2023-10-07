class Book:
    def __init__(self, title, author):
        self._attributes = {"title": title, "author": author}

    def __getattr__(self, name:str):
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


book = Book("Python Programming", "John Zelle")
print(book.__dict__)
print(f"{book.title = }")
print(f"{book.author = }")
# print(f"{book.year = }")

book.year = 2016
print(book.__dict__)
print(f"{book.year}")
print("----------------------------")

book2 = Book("Python", "John Zelle")
del book2.author
print(book2.__dict__)
