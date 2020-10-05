import requests


def get_updates(url):
    response = requests.get(f'{url}/getUpdates')
    return response.json()


def last_update(response_json):
    massages = response_json['result']
    return massages[len(massages)-1]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def send_message(id, text):
    params = {'chat_id': id, 'text': text}
    response = requests.post(f'{url}/sendMessage', data=params)
    print(f'{url}/sendMessage')
    print('Send Message')
    return response


with open('TemporaryFiles/bot.txt', 'r') as bot:
    token = bot.readline()
url = f'https://api.telegram.org/bot{token}'

chat_id = get_chat_id(last_update(get_updates(url)))
send_message(chat_id, 'Hello!')
