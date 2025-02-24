import hashlib
import random
import requests
from requests.exceptions import ConnectTimeout, ReadTimeout
from urllib.parse import urlencode

merchant_id= 'e52704cd-75ca-4bdb-88e1-717e6448c0c1'
secret_1 = "c6c3ef6d54c3ea03b433703057597c66"
secret_2 = "5fc226858a0a8c8ae6a02f2731c7f8b5"
api_key = "OGVjNjU2NDktNzRhMC00MDRiLWIyNzAtY2E5OWZiZjRkMDE5OldRKFpUVComMWVVV1Z6b3plKlFrcjBQR2RVQGs0QVdO"

def create_invoice(amount):
    currency = 'RUB' # Валюта заказа
    secret = secret_1
    order_id = str(random.randint(1111111,9999999))
    desc = 'Оплата в боте' # Описание заказа
    lang = 'ru' # Язык формы

    sign = f':'.join([
        str(merchant_id),
        str(amount),
        str(currency),
        str(secret),
        str(order_id)
    ])

    params = {
        'merchant_id': merchant_id,
        'amount': amount,
        'currency': currency,
        'order_id': order_id,
        'sign': hashlib.sha256(sign.encode('utf-8')).hexdigest(),
        'desc': desc,
        'lang': lang
    }

    url = "https://aaio.io/merchant/pay?" + urlencode(params)
    id = order_id
    return {'url':url,'id':id}

def is_payed(order_id):
    url = 'https://aaio.io/api/info-pay'

    params = {
        'merchant_id': merchant_id,
        'order_id': order_id
    }

    headers = {
        'Accept': 'application/json',
        'X-Api-Key': api_key
    }

    try:
        response = requests.post(url, data=params, headers=headers, timeout=(15, 60))
    except ConnectTimeout:
        print('ConnectTimeout')  # Не хватило времени на подключение к сайту
    except ReadTimeout:
        print('ReadTimeout')  # Не хватило времени на выполнение запроса

    if (response.status_code in [200, 400, 401]):
        try:
            response_json = response.json()  # Парсинг результата
        except:
            print('Не удалось пропарсить ответ')

        if (response_json['type'] == 'success'):
            return response_json['status'] == 'success'
        else:
            print('Ошибка: ' + response_json['message'])  # Вывод ошибки
    else:
        print('Response code: ' + str(response.status_code))  # Вывод неизвестного кода ответа