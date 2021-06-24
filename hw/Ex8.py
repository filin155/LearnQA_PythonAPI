import requests
import time


url = 'https://playground.learnqa.ru/ajax/api/longtime_job'

status_text_not_ready = 'Job is NOT ready'
status_text_ready = 'Job is ready'

response = requests.get(url)
parsed_response_text = response.json()

token = parsed_response_text["token"]
timer = parsed_response_text["seconds"]

payload = {"token": token}

response_before_timer_end = requests.get(url, params=payload)
first_response_text = response_before_timer_end.json()


try:
    if first_response_text["status"] == status_text_not_ready:
        print(f"статус верный:  {first_response_text['status']}")
    else:
        print(f"Статус отличный от: {status_text_not_ready} \nпришедший стату: {first_response_text['status']}")
except KeyError:
    print(first_response_text["error"])


time.sleep(timer + 1)


response_after_timer_end = requests.get(url, params=payload)
second_response_text = response_after_timer_end.json()


try:
    if second_response_text["status"] == status_text_ready:
        print(f"статус верный:  {second_response_text['status']} \nПоле result: {second_response_text['result']}")
    else:
        print(f"Статус отличный от: {status_text_ready} \nпришедший стату: {second_response_text['status']}")
except KeyError:
        print(second_response_text["error"])













