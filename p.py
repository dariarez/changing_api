import requests
import json


a = int(input('введіть id користувача: '))
b = int(input('введіть баланс: '))

def balance(a):
    url2 = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={}".format(a)
    res = requests.get(url2)
    print(res.text)

def new(a,b):
    check_user = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=getdata&user={}".format(a)
    res_check_user = requests.get(check_user)
    data = res_check_user.json()

    if data[0]['id'] == None:
        print('not found')
    else:
        url = "https://coderlog.top/api/goit/?key=5b15bdfa142761a1c65f50e046b6f7f5&method=setbalance&user={}&balance={}".format(a,b)
        res = requests.get(url)

        balance(a)
new(a, b)