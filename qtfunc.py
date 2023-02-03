import os
import random
import sys
import pygame
import requests


def createMap(x, y, z, l):
    slide = f"http://static-maps.yandex.ru/1.x/?ll={x},{y}&z={z}&l={l}"
    response = requests.get(slide)
    if not response:
        print("Ошибка выполнения запроса:")
        print(slide)
        print("Http статус:", response.status_code, "(", response.reason, ")")
        sys.exit(1)
    map_file = 'Data/maps/map.png'
    with open(map_file, "wb") as file:
        file.write(response.content)
    return 'Data/maps/map.png'