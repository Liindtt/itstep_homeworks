import requests
import json

response = requests.get("https://jsonplaceholder.typicode.com/todos")
json_text = response.text
python_text = json.loads(json_text)

users_tasks_completed = {}
users_tasks_uncompleted = []

# прохід по кожному юзеру в словнику
for user in python_text:
    if user["completed"]:
        if user["userId"] not in users_tasks_completed:
            users_tasks_completed[user["userId"]] = 1
        else:
            users_tasks_completed[user["userId"]] += 1
    else:
        users_tasks_uncompleted.append(user)

# 1.1. Користувач, що найбільше виконав завдань
for user_keys, user_values in users_tasks_completed.items():
    if user_values == max(users_tasks_completed.values()):
        print(f"Користувач з найбільшою к-стю виконаних завдань {user_values}: #{user_keys}")

# 1.2. Додавання юзерів у яких завдання невиконані
with open('data.json', mode="w") as filename:
    json_string = json.dumps(users_tasks_uncompleted, indent=2)
    filename.write(json_string)

# 1.3. Десереалізуєм дані й відсортовуємо по id, якщо id > 100
with open("data.json", "r") as filename:
    new_data = json.load(filename)
    new_data_list = [user for user in new_data if user['id'] > 100]
    for item in new_data_list:
        print(item)

