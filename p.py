import requests
import json


a = int(input('enter user`s id: '))
b = int(input('enter balance: '))

def balance(a):
    url2 = "your_key&method=getdata&user={}".format(a)
    res = requests.get(url2)
    print(res.text)

def new(a,b):
    check_user = "your_key&method=getdata&user={}".format(a)
    res_check_user = requests.get(check_user)
    data = res_check_user.json()

    if data[0]['id'] == None:
        print('not found')
    else:
        url = "your_key&method=setbalance&user={}&balance={}".format(a,b)
        res = requests.get(url)

        balance(a)
new(a, b)
