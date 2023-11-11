import time

def log_call(file="log.txt"):
    def decorator(func):
        def wrapper(self, *args, **kwargs):
            start_time = time.time()
            func(self, *args, **kwargs)
            end_time = time.time()

            with open(file, "a") as f:
                f.write(f"{func.__name__} {end_time - start_time}\n")

        return wrapper

    return decorator

class MyClass:

    @log_call(file="test.log")
    def info(self):
        print("This is my method")


my_class = MyClass()
my_class.info()
