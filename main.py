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
    return pygame.image.load('Data/maps/map.png')


# Инициализируем pygame
pygame.init()
screen = pygame.display.set_mode((600, 450))
# Рисуем картинку, загружаемую из только что созданного файла.
ind = 0
# Переключаем экран и ждем закрытия окна.
names = []
mapImage = createMap(60, 60, 5, 'map')
pygame.display.flip()
run = True
while run:
    screen.fill(pygame.Color('black'))
    screen.blit(mapImage, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.flip()
pygame.quit()
os.remove('Data/maps/map.png')
