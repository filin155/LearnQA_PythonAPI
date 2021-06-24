import requests

url = 'https://playground.learnqa.ru/ajax/api/compare_query_type'

methods = ['GET', 'POST', 'PUT', 'DELETE', 'HEAD', '']

for method in methods:
    if method == '':
        response = requests.get(url)
        print(f"Для {methods[0]} запроса отсутствует параметр method и получен ответ: {response.text}")
        continue

    response = requests.get(url, params={'method': method})
    print(f"Для {methods[0]} запроса method={method} и получен ответ {response.text}")
print()


for method in methods:
    if method == '':
        response = requests.post(url)
        print(f"Для {methods[1]} запроса отсутствует параметр method и получен ответ: {response.text}")
        continue

    response = requests.post(url, params={'method': method})
    print(f"Для {methods[1]} запроса method={method} и получен ответ {response.text}")
print()


for method in methods:
    if method == '':
        response = requests.put(url)
        print(f"Для {methods[2]} запроса отсутствует параметр method и получен ответ: {response.text}")
        continue

    response = requests.put(url, params={'method': method})
    print(f"Для {methods[2]} запроса method={method} и получен ответ {response.text}")
print()


for method in methods:
    if method == '':
        response = requests.delete(url)
        print(f"Для {methods[3]} запроса отсутствует параметр method и получен ответ: {response.text}")
        continue

    response = requests.delete(url, params={'method': method})
    print(f"Для {methods[3]} запроса method={method} и получен ответ {response.text}")
print()
