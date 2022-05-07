import requests
from requests.structures import CaseInsensitiveDict
import time
import random
import json

messages = ["Парни кто в сети", "Здарова", "Чо как дела?", "Гоу фармить поинты", "чем длинее смс тем больше баллов?",
            "я тут в ванне засел", "каникулы реально кайф", "делать реально нечего", "все равно нефиг делать",
            "блин мб доставку ролл заказать)))", "залил только два к баксов в биток хз зачем", "скоро хеллуин парни",
            "вайтлист дают сто проц или раффл", "вайтслист дадут же?", "лвл кайф", "ура новый лвл",
            "фреско ниже  чем ты думал", "пау пау белый", "окей,,,", "честно вообще не шарю", "заебался фармить",
            "честно хз", "когда матчи лч", "кто шарит за футбол", "кто мск?", "как вам альбом кизы и тейпа?",
            "песня айс разными голосами", "когда дропы норм кто знает?", "как думаете долго фармить надо будет?",
            "тут кто вообще в сети", "посоветуйте сериал пж", "ща ченить из инета скопирую", "мб поэтому прочитать",
            "пипец парни", "да уж", "мне кажется я на бота похож", "я может чуть не по теме пишу, но пофиг, фарм",
            "бл девушка бросила", "у кого есть доступ в эссеншиалс", "вчера кстати поднял норм",
            "классный монолог получается", "че какой у кого лвл", "что-то устал фармить уже",
            "кто шарит за бинанс хорошо", "Я помню чудное мгновенье", "Помогите вывести с бинанса в лс",
            "Так легче будет", "Сегодня будет дроп интересный?", "У кого сколько аккаунтов?", "Кто расскажет?",
            "Что такое флипать?", "Веселуха какая", "Просто", "Да я просто не шарю", "Срочно", "Я слушаю", "Понял",
            "Щас так и сделаю", "Спасибо я понял", "Кто нибудь может в личку рассказать что тут нужно делать?",
            "Я вспомнил что посмотреть!", "Пасаны помогите найти бабушку!"]

token = 'OTE5OTA2ODk4ODI2OTE5OTQ2.Yk1Jvw.Ovd37NP6H_z3sdsQAAuAhyoHHP8'
channelId = '969237025968496730'
userId = 'CryptoKornakova'
timestop = float(65)


def retrieve_messages(channelId, token):
    url = f"https://discord.com/api/v9/channels/{channelId}/messages?limit=10"

    headers = CaseInsensitiveDict()
    headers["authorization"] = token

    resp = requests.get(url, headers=headers)
    # print (resp.text)
    return json.loads(resp.text)


def razbor_message(text, userId):  # get message_id
    for i in range(0, len(text)):
        if (text[i]['author']['username']) == str(userId):
            return (text[i]['id'])
            break

        # razbor_message(text,userId)


def delete_message(channelId, token, messageId):
    url = f"https://discord.com/api/v9/channels/{channelId}/messages/{messageId}"
    headers = CaseInsensitiveDict()
    headers["authorization"] = token
    resp = requests.delete(url, headers=headers)
    print(resp.status_code)


def send_message(channelId, token, messages, userId, timestop):
    headers = CaseInsensitiveDict()
    headers["authorization"] = token
    headers["Content-Type"] = "application/json"

    url = f'https://discord.com/api/v9/channels/{channelId}/messages'

    while True:
        random_index = random.randint(0, len(messages) - 1)
        data = '{"content": "' + messages[random_index] + '","tts": "false"}'
        data = data.encode()
        resp = requests.post(url, headers=headers, data=data)
        # print(resp.status_code)
        text = retrieve_messages(channelId, token)
        messageId = razbor_message(text, userId)
        delete_message(channelId, token, messageId)
        time.sleep(timestop)


send_message(channelId, token, messages, userId, timestop)