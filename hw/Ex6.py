import requests

response = requests.get("https://playground.learnqa.ru/api/long_redirect")

print(f"колличество редиректов: {len(response.history)}")
print(f"конечный url: {response.url}")