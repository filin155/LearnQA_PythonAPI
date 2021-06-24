from json.decoder import JSONDecodeError
import requests

# Простой запрос
#
# payload = {"name": "user"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# print(response.text)


# Преобразовали ответ в json
#
# payload = {"name": "user"}
# response = requests.get("https://playground.learnqa.ru/api/hello", params=payload)
# parsed_response_text = response.json()
# print(parsed_response_text["answer"])


# Если неуверены что ответ именно в формате json
#
# payload = {"name": "user"}
# response = requests.get("https://playground.learnqa.ru/api/get_text")
#
# try:
#     parsed_response_text = response.json()
#     print(parsed_response_text)
# except:
#     print("Response is not a JSON format")



# Проверка типа запроса
# у get запросов данные передаются с помощью params, у post запросов с помощью data
# payload = {"param1": "value1"}
#
# response = requests.get("https://playground.learnqa.ru/api/check_type", params=payload)
# print(response.text)
#
# response = requests.post("https://playground.learnqa.ru/api/check_type", data=payload)
# print(response.text)


# Статус коды
#
# response = requests.get("https://playground.learnqa.ru/api/check_type")
# print(response.status_code)
# print()
#
# response = requests.get("https://playground.learnqa.ru/api/get_500")
# print(response.status_code)
# print(response.text)
# print()
#
# response = requests.get("https://playground.learnqa.ru/api/tes")
# print(response.status_code)
# print(response.text)
# print()
#
# response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=True)
# first_response = response.history[0]
# second_response = response
# print(f"{first_response.url} \n {second_response.url} \n {response.status_code}")
# print()
#
# response = requests.get("https://playground.learnqa.ru/api/get_301", allow_redirects=False)
# print(response.status_code)
# print()



# Заголовки
#
# headers = {"some_headers":"123"}
# response = requests.get("https://playground.learnqa.ru/api/show_all_headers", headers=headers);
# print(response.text)
# print(response.headers)


# Куки
#
# payload = {"login": "secret_login", "password": "secret_pass"}
# response = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)
# print(response.text)
# print(response.status_code)
# print(dict(response.cookies))
#
# print(response.headers)



payload = {"login": "secret_login", "password": "secret_pass2"}
response1 = requests.post("https://playground.learnqa.ru/api/get_auth_cookie", data=payload)

cookie_value = response1.cookies.get('auth_cookie')

cookies = {}
if cookie_value is not None:
    cookies.update({'auth_cookie': cookie_value})

response2 = requests.post("https://playground.learnqa.ru/api/check_auth_cookie", cookies=cookies)

print(response2.text)






























