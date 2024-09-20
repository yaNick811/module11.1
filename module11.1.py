import requests

# 1. Отправляем GET-запрос к веб-сайту
response = requests.get('https://api.github.com')

# 2. Выводим статус код ответа
print("Статус код:", response.status_code)

# 3. Выводим содержимое ответа в формате JSON
print("Содержимое ответа в формате JSON:")
print(response.json())

# 4. Отправляем POST-запрос с данными формы
data = {'key1': 'value1', 'key2': 'value2'}
response = requests.post('https://httpbin.org/post', data=data)

# 5. Выводим содержимое ответа в формате JSON
print("Содержимое POST-ответа в формате JSON:")
print(response.json())

# 6. Отправляем GET-запрос с параметрами
params = {'q': 'requests+language:python'}
response = requests.get('https://api.github.com/search/repositories', params=params)

# 7. Выводим содержимое ответа в формате JSON
print("Содержимое ответа с параметрами в формате JSON:")
print(response.json())