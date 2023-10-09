class Dynamic:
    def __init__(self):
        self._attributes = {}

    def __delattr__(self, item):
        del self._attributes[item]

    def __setattr__(self, name, value):
        print(f"Call __setattr__ with {name=}, {value=}")
        if name == "_attributes":
            print(name)
            super().__setattr__(name, value)
        else:
            self._attributes[f"{name}"] = value

    def __getattr__(self, name: str):
        print(f"Call __getattr__ {name}")
        if name in self._attributes:
            return self._attributes[f"{name}"]
        else:
            raise AttributeError(f"{__class__.__name__} has no attribute '{name}'")

    def __getattribute__(self, name):
        if name == "__private_attr":
            raise AttributeError(f"sorry, but that '{name}' attribute is blocked")
        else:
            return super().__getattribute__(name)


tmp = Dynamic()
print(tmp.__dict__)
tmp.name = "Yaroslav"
tmp.surname = "Nykolaichuk"
print(tmp.__dict__)
print(tmp.name)
