class LoginRequired:
    def __init__(self, permission):
        self.user_permission = permission

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            if self.user_permission == "admin":
                func(*args, **kwargs)
            else:
                raise ValueError(f"Немає доступу для користувача {self.user_permission}")
            return

        return wrapper


@LoginRequired(permission="gg")
def data():
    print("secret data")


data()
