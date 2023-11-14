import csv
import requests


response = requests.get("https://jsonplaceholder.typicode.com/todos")
data = response.json()

# 1.1. Перетворення даних із json у csv
with open('data.csv', mode="w", newline="") as filename:
    writer = csv.writer(filename)
    writer.writerow(["userId", "id", "title", "completed"])
    for item in data:
        writer.writerow(item.values())
    print("Файл створено!")

# 1.2. Функція, яка добавляє новий запис у csv файл
def write_to_csv(userId: int, id: int, title: str, completed: bool):
    with open("data.csv", mode="a", newline="") as filename:
        writer = csv.writer(filename)
        writer.writerow([userId, id, title, completed])
        print("Дані успішно додано!")


write_to_csv(11, 201, 'test task', False)
