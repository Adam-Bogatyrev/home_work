import requests
import json

url = 'https://jsonplaceholder.typicode.com/todos/'
response = requests.get(url)
data = response.json()

output_file_path = 'todos.json'
with open(output_file_path, 'w') as json_file:
    json.dump(data, json_file, indent=2)

with open(output_file_path, 'r') as json_file:
    loaded_data = json.load(json_file)

for index, item in enumerate(loaded_data, start=1):
    json_item_path = f'todo_{index}.json'
    with open(json_item_path, 'w') as item_file:
        json.dump(item, item_file, indent=2)

print(f"Данные записаны в {output_file_path}")
print(f"Чтение данных из {output_file_path}")
print(f"Каждый словарь записан в отдельный JSON файл (todo_1.json, todo_2.json, ...)")