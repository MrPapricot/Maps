import os
import random
import sys
import pygame
import requests

pt = ''
flag = False


def createMap(x, y, z, l):
    global pt
    slide = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&z={z}&l={l}"
    api_server = "http://static-maps.yandex.ru/1.x/"

    params = {
        "ll": ",".join([str(x), str(y)]),
        "l": l,
        'z': z,
    }
    if pt:
        params['pt'] = pt

    response = requests.get(api_server, params=params)
    if not response:
        print("Ошибка выполнения запроса:")
        print(slide)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = 'Data/maps/map.png'
    with open(map_file, "wb") as file:
        file.write(response.content)
    return 'Data/maps/map.png'


def find_toponim(adress):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={adress}&format=json"

    global pt, flag
    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        if flag:
            try:
                toponym_address += ', ' + toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
            except BaseException:
                toponym_address += ', почтовый индекс не найден'
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        # Печатаем извлечённые из ответа поля:
        x, y = toponym_coodrinates.split()
        pt = ",".join([x, y, 'org'])
        return toponym_coodrinates, toponym_address
    else:
        print("Ошибка выполнения запроса:")
        print(geocoder_request)
        print("Http статус:", response.status_code, "(", response.reason, ")")


def click_map(x, y, delta):
    geocoder_request = f"http://geocode-maps.yandex.ru/1.x/?apikey=40d1649f-0493-4b70-98ba-98533de7710b&geocode={','.join([str(x), str(y)])}&spn={delta},{delta}&format=json"

    global pt, flag
    # Выполняем запрос.
    response = requests.get(geocoder_request)
    if response:
        # Преобразуем ответ в json-объект
        json_response = response.json()

        # Получаем первый топоним из ответа геокодера.
        # Согласно описанию ответа, он находится по следующему пути:
        toponym = json_response["response"]["GeoObjectCollection"]["featureMember"][0]["GeoObject"]
        # Полный адрес топонима:
        toponym_address = toponym["metaDataProperty"]["GeocoderMetaData"]["text"]
        if flag:
            try:
                toponym_address += ', ' + toponym["metaDataProperty"]["GeocoderMetaData"]["Address"]["postal_code"]
            except BaseException:
                toponym_address += ', почтовый индекс не найден'
        # Координаты центра топонима:
        toponym_coodrinates = toponym["Point"]["pos"]
        # Печатаем извлечённые из ответа поля:
        x, y = toponym_coodrinates.split()
        pt = ",".join([x, y, 'org'])
        return toponym_address
    else:
        return ''