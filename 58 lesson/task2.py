# Describe username descriptor
class UsernameDescriptor:
    def __get__(self, instance, owner):
        return instance.username_

    def __set__(self, instance, value):
        new_value = value.lower()
        if not (4 <= len(new_value) <= 10) and isinstance(value[0], str) and \
                all(char.isalnum() or char == "_" for char in value):
            raise ValueError("Username must to contains 4-10 symbols (include only letters and digits and underscore), "
                             "and can't begin with digit")
        instance.username_ = value

# Describe password descriptor
class PasswordDescriptor:
    def __get__(self, instance, owner):
        return instance.password_

    def __set__(self, instance, value):
        if not (isinstance(value, str)):    # validation before
            raise ValueError("Password must be string type!")
        if len(value) < 8:
            raise ValueError("Password length can't be less that 8 symbols")
        instance.password_ = value

# Main class
class User:
    username = UsernameDescriptor()  # first descriptor instance
    password = PasswordDescriptor()  # second descriptor instance

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    # printing info about current object
    def validation(self):
        print(f"User created!")
        print(f"{self.username = }")
        print(f"{self.password = }")


try:
    user1 = User("lin", "5768uyg$%^&")
    user1.validation()
except ValueError as error:
    print(f"User was not created!")
    print(f"ValueError: {error}")
print()

try:
    user2 = User("Lindtt", "qwerty1234")
    user2.validation()
except ValueError as error:
    print(f"User was not created!")
    print(f"ValueError: {error}")
print()

try:
    user3 = User("Lindtt", "576")
    user3.validation()
except ValueError as error:
    print(f"User was not created!")
    print(f"ValueError: {error}")
