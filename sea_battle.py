import pygame
import sys
import random
import numpy as np
import os


def frame(screen):
    """функция внешняя рамка и основная надпись"""
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (1115, 0), 5)
    pygame.draw.line(screen, (0, 0, 0), (0, 0), (0, 750), 5)
    pygame.draw.line(screen, (0, 0, 0), (1113, 0), (1113, 750), 4)
    pygame.draw.line(screen, (0, 0, 0), (0, 748), (1115, 748), 5)
    smail_def = pygame.image.load('picture/осн.png')
    screen.blit(smail_def, (185, 20))
    smail_def = pygame.image.load('picture/victory.png')
    screen.blit(smail_def, (30, 20))
    smail_def = pygame.image.load('picture/звук.png')
    screen.blit(smail_def, (965, 53))
    smail_def = pygame.image.load('picture/spk.png')
    screen.blit(smail_def, (190, 695))


def notebook_sheet(screen):
    """функция тетрадный лист"""
    for i in range(0, 1115, 30):
        pygame.draw.line(screen, (106, 90, 205), (i, 0), (i, 745), 1)
    for i in range(0, 750, 30):
        pygame.draw.line(screen, (106, 90, 205), (3, i), (1111, i), 1)


def sound(screen):
    """функция вкл/откл звука"""
    global flag_sound
    if flag_sound:
        pygame.draw.line(screen, (255, 0, 0), (975, 60), (1055, 125), 6)
        pygame.draw.line(screen, (255, 0, 0), (1055, 60), (975, 125), 6)
        flag_sound = False
    elif not flag_sound:
        pygame.Surface.fill(screen, (255, 250, 250), (970, 55, 90, 75))
        notebook_sheet(screen)
        smail_def = pygame.image.load('picture/звук.png')
        screen.blit(smail_def, (965, 53))
        flag_sound = True
    pygame.display.update((970, 55, 90, 75))


def button(screen):
    """функция отображения кнопок"""
    pygame.Surface.fill(screen, (230, 230, 250), (630, 270, 363, 62))
    smail_def = pygame.image.load('picture/новичок.png')
    screen.blit(smail_def, (630, 270))
    pygame.Surface.fill(screen, (230, 230, 250), (630, 360, 363, 62))
    smail_def = pygame.image.load('picture/мастер.png')
    screen.blit(smail_def, (630, 360))
    pygame.Surface.fill(screen, (230, 230, 250), (630, 450, 363, 62))
    smail_def = pygame.image.load('picture/профи.png')
    screen.blit(smail_def, (630, 450))


def text(screen, size, content, point, color_content):
    txt = pygame.font.SysFont('Arial Black', size)
    text_1 = txt.render(content, True, color_content)
    screen.blit(text_1, point)


def choice_difficulty_level(screen, number):
    """выбор уровня сложности"""
    button(screen)
    if number == 1:
        pygame.Surface.fill(screen, (0, 0, 128), (630, 270, 362, 62))
        pygame.Surface.fill(screen, (230, 230, 250), (650, 283, 325, 36))
        smail_def = pygame.image.load('picture/новичок.png')
        screen.blit(smail_def, (630, 270))
        pygame.display.update((630, 270, 363, 242))
        return 'beginner'
    elif number == 2:
        pygame.Surface.fill(screen, (0, 0, 128), (630, 360, 362, 62))
        pygame.Surface.fill(screen, (230, 230, 250), (650, 373, 325, 36))
        smail_def = pygame.image.load('picture/мастер.png')
        screen.blit(smail_def, (630, 360))
        pygame.display.update((630, 270, 363, 242))
        return 'master'
    elif number == 3:
        pygame.Surface.fill(screen, (0, 0, 128), (630, 450, 362, 62))
        pygame.Surface.fill(screen, (230, 230, 250), (650, 463, 325, 36))
        smail_def = pygame.image.load('picture/профи.png')
        screen.blit(smail_def, (630, 450))
        pygame.display.update((630, 270, 363, 242))
        return 'professional'


def grid(screen, x_start, x_end, y_start, y_end):
    """функция игровое поле 10 х 10"""
    cnt = 0
    list_letter = ('picture/а.png', 'picture/б.png', 'picture/в.png', 'picture/г.png', 'picture/д.png',
                   'picture/е.png', 'picture/ж.png', 'picture/з.png', 'picture/и.png', 'picture/к.png')
    list_number = ('picture/1.png', 'picture/2.png', 'picture/3.png', 'picture/4.png', 'picture/5.png',
                   'picture/6.png', 'picture/7.png', 'picture/8.png', 'picture/9.png', 'picture/10.png')
    for i in range(x_start, x_end, 30):
        pygame.draw.line(screen, (72, 61, 139), (i, y_start), (i, y_end), 2)
        if cnt < 10:
            if cnt == 6:
                smail_def = pygame.image.load(list_letter[cnt])
                screen.blit(smail_def, (i, y_start - 45))
            else:
                smail_def = pygame.image.load(list_letter[cnt])
                screen.blit(smail_def, (i + 5, y_start - 45))
            cnt += 1
    cnt = 0
    for i in range(y_start, y_end, 30):
        pygame.draw.line(screen, (72, 61, 139), (x_start, i), (x_end, i), 2)
        if cnt < 10:
            if cnt == 9:
                smail_def = pygame.image.load(list_number[cnt])
                screen.blit(smail_def, (x_start - 42, i - 12))
            else:
                smail_def = pygame.image.load(list_number[cnt])
                screen.blit(smail_def, (x_start - 25, i - 12))
            cnt += 1


def placement_ships(screen):
    """функция отображения кораблей для выбора при установке"""
    smail_def = pygame.image.load('picture/линкор.png')
    screen.blit(smail_def, (480, 300))
    smail_def = pygame.image.load('picture/н.линкор.png')
    screen.blit(smail_def, (613, 290))
    smail_def = pygame.image.load('picture/крейсер.png')
    screen.blit(smail_def, (480, 360))
    smail_def = pygame.image.load('picture/н.крейсер.png')
    screen.blit(smail_def, (606, 348))
    smail_def = pygame.image.load('picture/крейсер.png')
    screen.blit(smail_def, (480, 420))
    smail_def = pygame.image.load('picture/н.крейсер.png')
    screen.blit(smail_def, (606, 408))
    smail_def = pygame.image.load('picture/эсминец.png')
    screen.blit(smail_def, (480, 480))
    smail_def = pygame.image.load('picture/н.эсминец.png')
    screen.blit(smail_def, (600, 468))
    smail_def = pygame.image.load('picture/эсминец.png')
    screen.blit(smail_def, (480, 540))
    smail_def = pygame.image.load('picture/н.эсминец.png')
    screen.blit(smail_def, (600, 528))
    smail_def = pygame.image.load('picture/эсминец.png')
    screen.blit(smail_def, (810, 300))
    smail_def = pygame.image.load('picture/н.эсминец.png')
    screen.blit(smail_def, (885, 290))
    smail_def = pygame.image.load('picture/катер.png')
    screen.blit(smail_def, (810, 360))
    smail_def = pygame.image.load('picture/н.катер.png')
    screen.blit(smail_def, (898, 350))
    smail_def = pygame.image.load('picture/катер.png')
    screen.blit(smail_def, (810, 420))
    smail_def = pygame.image.load('picture/н.катер.png')
    screen.blit(smail_def, (898, 410))
    smail_def = pygame.image.load('picture/катер.png')
    screen.blit(smail_def, (810, 480))
    smail_def = pygame.image.load('picture/н.катер.png')
    screen.blit(smail_def, (898, 470))
    smail_def = pygame.image.load('picture/катер.png')
    screen.blit(smail_def, (810, 540))
    smail_def = pygame.image.load('picture/н.катер.png')
    screen.blit(smail_def, (898, 530))


def grout(screen):
    """функция отрисовки кораблей для установки"""
    global list_chek
    pygame.Surface.fill(screen, (255, 250, 250), rect=(470, 270, 630, 340))
    notebook_sheet(screen)
    placement_ships(screen)
    smail_def = pygame.image.load('picture/chek.png')
    if len(list_chek) > 0:
        for i in list_chek:
            screen.blit(smail_def, (i[0], i[1]))
    pygame.display.update((470, 270, 630, 340))


def generator(cell_number, n):
    """функция возможные варианты расстановки корабля относительно выбранной клетки"""
    list_cell = [cell_number]
    for i in range(cell_number, cell_number + n):
        """список вправо"""
        if i in range(10, 101, 10):
            if i not in list_cell:
                list_cell.append(i)
            break
        elif i not in list_cell:
            if 0 < i < 101:
                list_cell.append(i)
    for i in range(cell_number, cell_number - n, -1):
        """список влево"""
        if i in range(1, 92, 10):
            if i not in list_cell:
                list_cell.append(i)
            break
        elif i not in list_cell:
            if 0 < i < 101:
                list_cell.append(i)
    for i in range(cell_number + 10, cell_number + n * 10, 10):
        """список вниз"""
        if 0 < i < 101:
            list_cell.append(i)
    for i in range(cell_number - 10, cell_number - n * 10, -10):
        """список вверх"""
        if 0 < i < 101:
            list_cell.append(i)
    list_cell = sorted(list_cell)  # общий список всех клеток
    return list_cell


def reduction(list_ship, list_probability_ship, n):
    """функция сокращает возможные варианты расстановки корабля относительно  выбранных клеток"""
    difference_horizon_temp = set()
    difference = abs(list_ship[0] - list_ship[1])
    if len(list_ship) == 2:
        if difference < n:
            difference_horizon_temp = (set(range(list_ship[0] - (n - 1), list_ship[0] + n))
                                       & set(range(list_ship[1] - (n - 1), list_ship[1] + n)))
        elif difference >= 10:
            difference_horizon_temp = (set(range(list_ship[0] - (n - 1) * 10, list_ship[0] + n * 10, 10))
                                       & set(range(list_ship[1] - (n - 1) * 10, list_ship[1] + n * 10, 10)))
    if len(list_ship) == 3:
        if difference < n:
            difference_horizon_temp = (set(range(list_ship[0] - (n - 1), list_ship[0] + n))
                                       & set(range(list_ship[1] - (n - 1), list_ship[1] + n))
                                       & set(range(list_ship[2] - (n - 1), list_ship[2] + n)))
        elif difference >= 10:
            difference_horizon_temp = (set(range(list_ship[0] - (n - 1) * 10, list_ship[0] + n * 10, 10))
                                       & set(range(list_ship[1] - (n - 1) * 10, list_ship[1] + n * 10, 10))
                                       & set(range(list_ship[2] - (n - 1) * 10, list_ship[2] + n * 10, 10)))
    difference_horizon = list(difference_horizon_temp & set(list_probability_ship))
    return sorted(difference_horizon)


def ban_cell(list_ship):
    """функция формирует список запрещенных клеток для установки корабля"""
    list_ban_cell = []
    temp = set()
    list_ship = sorted(list_ship)
    for i in list_ship:
        temp.add(i - 1)
        temp.add(i - 11)
        temp.add(i - 10)
        temp.add(i - 9)
        temp.add(i + 1)
        temp.add(i + 11)
        temp.add(i + 10)
        temp.add(i + 9)
    temp = sorted(list(temp))
    for i in temp:
        if i not in list_ship:
            if 0 < i < 101:
                if list_ship[0] in range(1, 92, 10):
                    if i in range(10, 101, 10):
                        continue
                    else:
                        list_ban_cell.append(i)
                elif list_ship[0] in range(10, 101, 10) or list_ship[-1] in range(10, 101, 10):
                    if i in range(1, 92, 10):
                        continue
                    else:
                        list_ban_cell.append(i)
                else:
                    list_ban_cell.append(i)
    list_ban_cell = sorted(list(list_ban_cell))
    return list_ban_cell


def installation_options(screen, list_probability_ship):
    """Функция отображения на игровом поле вариантов установки корабля"""
    global cell
    surf = pygame.Surface((32, 32))
    surf.set_alpha(100)
    for i in list_probability_ship:
        x_start = cell[i][0]
        y_start = cell[i][1]
        pygame.Surface.fill(surf, (176, 224, 230))
        pygame.draw.rect(surf, (25, 25, 112), (0, 0, 32, 32), 4)
        screen.blit(surf, (x_start, y_start))
        pygame.display.update((120, 300, 300, 300))


def number_shots_remaining(screen):
    """функция отображает количество оставшихся выстрелов"""
    global flag_my_shot, flag_enemy_shot, number_moves
    global list_my_shot, list_injured_my_ships, list_killed_my_ships
    global list_enemy_shot, list_injured_enemy_ships, list_killed_enemy_ships
    pygame.Surface.fill(screen, (255, 250, 250), rect=(380, 620, 60, 50))
    pygame.Surface.fill(screen, (255, 250, 250), rect=(800, 620, 60, 50))
    notebook_sheet(screen)
    if flag_my_shot:
        col = str(100 - len(list(set(list_my_shot) | set(list_injured_enemy_ships) | set(list_killed_enemy_ships))))
        text(screen, 30, col, (800, 622), (0, 128, 0))
        number_moves = col
        col = str(100 - len(list(set(list_enemy_shot) | set(list_injured_my_ships) | set(list_killed_my_ships))))
        text(screen, 30, col, (380, 622), (255, 0, 0))
    elif flag_enemy_shot:
        col = str(100 - len(list(set(list_my_shot) | set(list_injured_enemy_ships) | set(list_killed_enemy_ships))))
        text(screen, 30, col, (800, 622), (255, 0, 0))
        col = str(100 - len(list(set(list_enemy_shot) | set(list_injured_my_ships) | set(list_killed_my_ships))))
        text(screen, 30, col, (380, 622), (0, 128, 0))
    pygame.display.update((380, 620, 60, 50))
    pygame.display.update((800, 620, 60, 50))


def check_function(list_ship, n):
    list_1 = []
    list_10 = []
    for i in range(len(list_ship) - 1):
        for j in range(1, len(list_ship)):
            if abs(list_ship[i] - list_ship[j]) == 1:
                list_1.append(list_ship[i])
                list_1.append(list_ship[j])
            elif abs(list_ship[i] - list_ship[j]) == 10:
                list_10.append(list_ship[i])
                list_10.append(list_ship[j])
    list_1 = set(list_1)
    list_10 = set(list_10)
    if len(list_1) >= n and len(list_10) >= n:
        return list(set(list_1) | set(list_10))
    elif len(list_1) < n <= len(list_10):
        return list_10
    elif len(list_10) < n <= len(list_1):
        return list_1
    else:
        return []


def choice_battleship(screen, cell_number):
    """установка линкора 4 клетки"""
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship, list_my_battleship, list_chek
    global flag_battleship, flag_automatic
    global flag_del_battleship, flag_clear_field, flag_delete_ship
    x_start = cell[cell_number][0]
    y_start = cell[cell_number][1]
    if len(list_battleship) == 0 and (cell_number not in list_my_ship) and (cell_number not in list_ban_cell):
        list_probability_ship = generator(cell_number, 4)
        list_probability_ship = list(set(list_probability_ship) - set(list_ban_cell) - set(list_my_ship))
        list_probability_ship = check_function(list_probability_ship, 4)
        if len(list_probability_ship) >= 4:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            list_my_ship.append(cell_number)
            list_battleship.append(cell_number)
            if not flag_automatic:
                installation_options(screen, list_probability_ship)
    elif (len(list_battleship) == 1 and cell_number in list_probability_ship
          and cell_number not in list_battleship and cell_number not in list_ban_cell):
        list_my_ship.append(cell_number)
        list_battleship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 4)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][1]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            installation_options(screen, list(set(list_probability_ship) - set(list_ban_cell)))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
    elif (len(list_battleship) == 2 and cell_number in list_probability_ship
          and cell_number not in list_battleship and cell_number not in list_ban_cell):
        list_my_ship.append(cell_number)
        list_battleship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 4)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][1]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            installation_options(screen, list(set(list_probability_ship) - set(list_ban_cell)))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
    elif (len(list_battleship) == 3 and cell_number in list_probability_ship
          and cell_number not in list_battleship and cell_number not in list_ban_cell):
        list_my_ship.append(cell_number)
        list_battleship.append(cell_number)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][1]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        list_my_battleship = list_battleship.copy()
        list_battleship = []
        list_probability_ship = []
        flag_battleship = True
        flag_del_battleship = False
        flag_clear_field = True
        flag_delete_ship = False
        if not flag_automatic:
            pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
            smail_def = pygame.image.load('picture/очистить.png')
            screen.blit(smail_def, (420, 636))
            pygame.display.update((420, 636, 270, 50))
        list_chek.append((750, 295))
        if not flag_automatic:
            grout(screen)


def choice_cruiser(screen, cell_number, flag):
    """установка крейсера 3 клетки"""
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship, list_chek, flag_automatic
    global flag_cruiser_1, flag_cruiser_2, list_my_cruiser_1, list_my_cruiser_2
    global flag_del_cruiser_1, flag_del_cruiser_2, flag_clear_field, flag_delete_ship
    x_start = cell[cell_number][0]
    y_start = cell[cell_number][1]
    if len(list_battleship) == 0 and (cell_number not in list_my_ship) and (cell_number not in list_ban_cell):
        list_probability_ship = generator(cell_number, 3)
        list_probability_ship = list(set(list_probability_ship) - set(list_ban_cell) - set(list_my_ship))
        list_probability_ship = check_function(list_probability_ship, 3)
        if len(list_probability_ship) >= 3:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            list_battleship.append(cell_number)
            list_my_ship.append(cell_number)
            if not flag_automatic:
                installation_options(screen, list_probability_ship)
    elif (len(list_battleship) == 1 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 3)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][1]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            installation_options(screen, list(set(list_probability_ship) - set(list_ban_cell)))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
    elif (len(list_battleship) == 2 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][1]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        if flag == 1:
            flag_cruiser_1 = True
            list_my_cruiser_1 = list_battleship.copy()
            flag_del_cruiser_1 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((750, 355))
            if not flag_automatic:
                grout(screen)
        elif flag == 2:
            flag_cruiser_2 = True
            list_my_cruiser_2 = list_battleship.copy()
            flag_del_cruiser_2 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((750, 415))
            if not flag_automatic:
                grout(screen)
        list_battleship = []
        list_probability_ship = []


def choice_destroyer(screen, cell_number, flag):
    """установка эсминца 2 клетки"""
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship, flag_automatic
    global flag_destroyer_1, flag_destroyer_2, flag_destroyer_3
    global list_my_destroyer_1, list_my_destroyer_2, list_my_destroyer_3
    global flag_del_destroyer_1, flag_del_destroyer_2, flag_del_destroyer_3, flag_clear_field, flag_delete_ship
    x_start = cell[cell_number][0]
    y_start = cell[cell_number][1]
    if len(list_battleship) == 0 and (cell_number not in list_my_ship) and (cell_number not in list_ban_cell):
        list_probability_ship = generator(cell_number, 2)
        list_probability_ship = list(set(list_probability_ship) - set(list_ban_cell) - set(list_my_ship))
        list_probability_ship = check_function(list_probability_ship, 2)
        if len(list_probability_ship) >= 2:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
            list_battleship.append(cell_number)
            list_my_ship.append(cell_number)
            if not flag_automatic:
                installation_options(screen, list_probability_ship)
    elif (len(list_battleship) == 1 and cell_number in list_probability_ship and cell_number not in list_battleship
          and cell_number not in list_ban_cell):
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        if not flag_automatic:
            delete_1(screen)
            for i in list_my_ship:
                x_start = cell[i][0]
                y_start = cell[i][1]
                pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        else:
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        if flag == 1:
            flag_destroyer_1 = True
            list_my_destroyer_1 = list_battleship.copy()
            flag_del_destroyer_1 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((750, 475))
            if not flag_automatic:
                grout(screen)
        elif flag == 2:
            flag_destroyer_2 = True
            list_my_destroyer_2 = list_battleship.copy()
            flag_del_destroyer_2 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((750, 535))
            if not flag_automatic:
                grout(screen)
        elif flag == 3:
            flag_destroyer_3 = True
            list_my_destroyer_3 = list_battleship.copy()
            flag_del_destroyer_3 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((1035, 295))
            if not flag_automatic:
                grout(screen)
        list_battleship = []
        list_probability_ship = []


def choice_boat(screen, cell_number, flag):
    """установка катера 1 клетка"""
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship
    global flag_boat_1, flag_boat_2, flag_boat_3, flag_boat_4
    global list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4
    global flag_del_boat_1, flag_del_boat_2, flag_del_boat_3, flag_del_boat_4, flag_clear_field, flag_delete_ship
    x_start = cell[cell_number][0]
    y_start = cell[cell_number][1]
    if len(list_battleship) == 0 and (cell_number not in list_my_ship) and (cell_number not in list_ban_cell):
        pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
        pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        pygame.display.update((x_start - 5, y_start - 5, 40, 40))
        list_battleship.append(cell_number)
        list_my_ship.append(cell_number)
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        if flag == 1:
            flag_boat_1 = True
            list_my_boat_1 = list_battleship.copy()
            flag_del_boat_1 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((1035, 355))
            if not flag_automatic:
                grout(screen)
        elif flag == 2:
            flag_boat_2 = True
            list_my_boat_2 = list_battleship.copy()
            flag_del_boat_2 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((1035, 415))
            if not flag_automatic:
                grout(screen)
        elif flag == 3:
            flag_boat_3 = True
            list_my_boat_3 = list_battleship.copy()
            flag_del_boat_3 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((1035, 475))
            if not flag_automatic:
                grout(screen)
        elif flag == 4:
            flag_boat_4 = True
            list_my_boat_4 = list_battleship.copy()
            flag_del_boat_4 = False
            flag_clear_field = True
            flag_delete_ship = False
            if not flag_automatic:
                pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                smail_def = pygame.image.load('picture/очистить.png')
                screen.blit(smail_def, (420, 636))
                pygame.display.update((420, 636, 270, 50))
            list_chek.append((1035, 535))
            if not flag_automatic:
                grout(screen)
        list_battleship = []
        list_probability_ship = []


def delete_ship(screen, flag_clear_field, flag_delete_ship):
    global list_chek
    pygame.Surface.fill(screen, (255, 250, 250), (30, 200, 1065, 490))
    notebook_sheet(screen)
    smail_def = pygame.image.load('picture/мой флот.png')
    screen.blit(smail_def, (165, 200))
    smail_def = pygame.image.load('picture/расставить корабли.png')
    screen.blit(smail_def, (540, 200))
    grid(screen, 120, 421, 300, 601)
    placement_ships(screen)
    pygame.Surface.fill(screen, (230, 230, 250), (90, 636, 274, 52))
    smail_def = pygame.image.load('picture/расставить.png')
    screen.blit(smail_def, (90, 636))
    pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 274, 52))
    if flag_clear_field and not flag_delete_ship:
        smail_def = pygame.image.load('picture/очистить.png')
    elif not flag_clear_field and flag_delete_ship:
        smail_def = pygame.image.load('picture/удалить.png')
    screen.blit(smail_def, (420, 636))
    pygame.Surface.fill(screen, (230, 230, 250), (750, 636, 274, 52))
    smail_def = pygame.image.load('picture/дальше_2.png')
    screen.blit(smail_def, (750, 636))
    pygame.display.update((30, 200, 1065, 490))
    list_chek = []


def delete_1(screen):
    pygame.Surface.fill(screen, (255, 250, 250), rect=(120, 300, 300, 300))
    frame(screen)
    grid(screen, 120, 421, 300, 601)
    pygame.display.update((120, 300, 300, 300))


def automatic_placement_ships(screen):
    global flag_clear_field, flag_delete_ship
    global cell, list_my_ship, list_ban_cell, list_battleship, list_probability_ship
    global flag_battleship, flag_cruiser_1, flag_cruiser_2, flag_destroyer_1, flag_destroyer_2, flag_destroyer_3
    global flag_boat_1, flag_boat_2, flag_boat_3, flag_boat_4
    global list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1, \
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4
    if (not flag_battleship and not flag_cruiser_1 and not flag_cruiser_2 and not flag_destroyer_1
            and not flag_destroyer_2 and not flag_destroyer_3 and not flag_boat_1 and not flag_boat_2
            and not flag_boat_3 and not flag_boat_1):
        try:
            """Выбор случайного места установки линкора"""
            cell_number = random.randint(1, 100)
            choice_battleship(screen, cell_number)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
            choice_battleship(screen, cell_number)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
            choice_battleship(screen, cell_number)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
            choice_battleship(screen, cell_number)
            """Выбор случайного места установки крейсера_1 и крейсера_2"""
            for i in range(1, 3):
                cell_number = list(set(range(1, 101)) - set(list_my_ship) - set(list_ban_cell))
                cell_number = random.choice(cell_number)
                choice_cruiser(screen, cell_number, i)
                cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                                 - set(list_my_ship) - set(list_ban_cell)))
                choice_cruiser(screen, cell_number, i)
                cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                                 - set(list_my_ship) - set(list_ban_cell)))
                choice_cruiser(screen, cell_number, i)
            """Выбор случайного места установки эсминца_1, эсминца_2, эсминца_3"""
            for i in range(1, 4):
                cell_number = list(set(range(1, 101)) - set(list_my_ship) - set(list_ban_cell))
                cell_number = random.choice(cell_number)
                choice_destroyer(screen, cell_number, i)
                cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                                 - set(list_my_ship) - set(list_ban_cell)))
                choice_destroyer(screen, cell_number, i)
            """Выбор случайного места установки катера_1, катера_2, катера_3, катера_4"""
            for i in range(1, 5):
                cell_number = list(set(range(1, 101)) - set(list_my_ship) - set(list_ban_cell))
                cell_number = random.choice(cell_number)
                choice_boat(screen, cell_number, i)
        except IndexError:
            delete_ship(screen, flag_clear_field, flag_delete_ship)
            list_my_ship = []  # список моих кораблей
            list_ban_cell = []  # список запрещенных клеток для установки корабля
            list_battleship = []  # список координат установки линкора
            list_probability_ship = []  # список вариатов установки корабля
            list_my_battleship = []  # координаты моего линкора
            list_my_cruiser_1 = []  # координаты моего крейсера_1
            list_my_cruiser_2 = []  # координаты моего крейсера_2
            list_my_destroyer_1 = []  # координаты моего эсминца_1
            list_my_destroyer_2 = []  # координаты моего эсминца_2
            list_my_destroyer_3 = []  # координаты моего эсминца_3
            list_my_boat_1 = []  # координаты моего катера_1
            list_my_boat_2 = []  # координаты моего катера_2
            list_my_boat_3 = []  # координаты моего катера_3
            list_my_boat_4 = []  # координаты моего катера_4
            flag_battleship = False  # установлен ли линкор : True - да , False - нет
            flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
            flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
            flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
            flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
            flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
            flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
            flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
            flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
            flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
            automatic_placement_ships(screen)
        grout(screen)


def automatic_placement_enemy_ships():
    global list_enemy_ships, list_ban_cell, list_battleship, list_probability_ship
    global list_enemy_battleship, list_enemy_cruiser_1, list_enemy_cruiser_2
    global list_enemy_destroyer_1, list_enemy_destroyer_2, list_enemy_destroyer_3
    global list_enemy_boat_1, list_enemy_boat_2, list_enemy_boat_3, list_enemy_boat_4
    list_ban_cell = []
    list_battleship = []
    list_probability_ship = []
    try:
        """Выбор случайного места установки линкора"""
        cell_number = random.randint(1, 100)
        list_enemy_ships.append(cell_number)
        list_battleship.append(cell_number)
        list_probability_ship = generator(cell_number, 4)
        cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
        list_enemy_ships.append(cell_number)
        list_battleship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 4)
        cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
        list_enemy_ships.append(cell_number)
        list_battleship.append(cell_number)
        list_probability_ship = reduction(list_battleship, list_probability_ship, 4)
        cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)))
        list_enemy_ships.append(cell_number)
        list_battleship.append(cell_number)
        list_enemy_battleship = list_battleship.copy()
        temp = ban_cell(list_battleship)
        for i in temp:
            list_ban_cell.append(i)
        list_ban_cell = list(set(list_ban_cell))
        list_battleship = []
        list_probability_ship = []
        """Выбор случайного места установки крейсера_1 и крейсера_2"""
        for i in range(1, 3):
            cell_number = list(set(range(1, 101)) - set(list_enemy_ships) - set(list_ban_cell))
            cell_number = random.choice(cell_number)
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            list_probability_ship = generator(cell_number, 3)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                             - set(list_enemy_ships) - set(list_ban_cell)))
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            list_probability_ship = reduction(list_battleship, list_probability_ship, 3)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                             - set(list_enemy_ships) - set(list_ban_cell)))
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            if i == 1:
                list_enemy_cruiser_1 = list_battleship.copy()
            elif i == 2:
                list_enemy_cruiser_2 = list_battleship.copy()
            temp = ban_cell(list_battleship)
            for j in temp:
                list_ban_cell.append(j)
            list_ban_cell = list(set(list_ban_cell))
            list_battleship = []
            list_probability_ship = []
        """Выбор случайного места установки эсминца_1, эсминца_2, эсминца_3"""
        for i in range(1, 4):
            cell_number = list(set(range(1, 101)) - set(list_enemy_ships) - set(list_ban_cell))
            cell_number = random.choice(cell_number)
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            list_probability_ship = generator(cell_number, 2)
            cell_number = random.choice(list(set(list_probability_ship) - set(list_battleship)
                                             - set(list_enemy_ships) - set(list_ban_cell)))
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            if i == 1:
                list_enemy_destroyer_1 = list_battleship.copy()
            elif i == 2:
                list_enemy_destroyer_2 = list_battleship.copy()
            elif i == 3:
                list_enemy_destroyer_3 = list_battleship.copy()
            temp = ban_cell(list_battleship)
            for j in temp:
                list_ban_cell.append(j)
            list_ban_cell = list(set(list_ban_cell))
            list_battleship = []
            list_probability_ship = []
        """Выбор случайного места установки катера_1, катера_2, катера_3, катера_4"""
        for i in range(1, 5):
            cell_number = list(set(range(1, 101)) - set(list_enemy_ships) - set(list_ban_cell))
            cell_number = random.choice(cell_number)
            list_enemy_ships.append(cell_number)
            list_battleship.append(cell_number)
            if i == 1:
                list_enemy_boat_1 = list_battleship.copy()
            elif i == 2:
                list_enemy_boat_2 = list_battleship.copy()
            elif i == 3:
                list_enemy_boat_3 = list_battleship.copy()
            elif i == 4:
                list_enemy_boat_4 = list_battleship.copy()
            temp = ban_cell(list_battleship)
            for j in temp:
                list_ban_cell.append(j)
            list_ban_cell = list(set(list_ban_cell))
            list_battleship = []
            list_probability_ship = []
        k = random.randint(1, 11)
        n = 10 // k
        set_1 = {1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91}
        tmp = set(list_enemy_ships) & set_1
        if len(tmp) > n:
            list_enemy_ships = []
            list_ban_cell = []
            list_battleship = []
            list_probability_ship = []
            list_enemy_battleship = []
            list_enemy_cruiser_1 = []
            list_enemy_cruiser_2 = []
            list_enemy_destroyer_1 = []
            list_enemy_destroyer_2 = []
            list_enemy_destroyer_3 = []
            list_enemy_boat_1 = []
            list_enemy_boat_2 = []
            list_enemy_boat_3 = []
            list_enemy_boat_4 = []
            automatic_placement_enemy_ships()
    except IndexError:
        list_enemy_ships = []
        list_ban_cell = []
        list_battleship = []
        list_probability_ship = []
        list_enemy_battleship = []
        list_enemy_cruiser_1 = []
        list_enemy_cruiser_2 = []
        list_enemy_destroyer_1 = []
        list_enemy_destroyer_2 = []
        list_enemy_destroyer_3 = []
        list_enemy_boat_1 = []
        list_enemy_boat_2 = []
        list_enemy_boat_3 = []
        list_enemy_boat_4 = []
        automatic_placement_enemy_ships()
        k = random.randint(1, 11)
        n = 10 // k
        set_1 = {1, 12, 23, 34, 45, 56, 67, 78, 89, 100, 10, 19, 28, 37, 46, 55, 64, 73, 82, 91}
        tmp = set(list_enemy_ships) & set_1
        if len(tmp) > n:
            list_enemy_ships = []
            list_ban_cell = []
            list_battleship = []
            list_probability_ship = []
            list_enemy_battleship = []
            list_enemy_cruiser_1 = []
            list_enemy_cruiser_2 = []
            list_enemy_destroyer_1 = []
            list_enemy_destroyer_2 = []
            list_enemy_destroyer_3 = []
            list_enemy_boat_1 = []
            list_enemy_boat_2 = []
            list_enemy_boat_3 = []
            list_enemy_boat_4 = []
            automatic_placement_enemy_ships()


def new_list_ban_cell():
    list_ban_cell_new = []
    if len(list_my_battleship) == 4:
        temp = ban_cell(list_my_battleship)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_cruiser_1) == 3:
        temp = ban_cell(list_my_cruiser_1)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_cruiser_2) == 3:
        temp = ban_cell(list_my_cruiser_2)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_destroyer_1) == 2:
        temp = ban_cell(list_my_destroyer_1)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_destroyer_2) == 2:
        temp = ban_cell(list_my_destroyer_2)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_destroyer_3) == 2:
        temp = ban_cell(list_my_destroyer_3)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_boat_1) == 1:
        temp = ban_cell(list_my_boat_1)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_boat_2) == 1:
        temp = ban_cell(list_my_boat_2)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_boat_3) == 1:
        temp = ban_cell(list_my_boat_3)
        for i in temp:
            list_ban_cell_new.append(i)
    if len(list_my_boat_4) == 1:
        temp = ban_cell(list_my_boat_4)
        for i in temp:
            list_ban_cell_new.append(i)
    list_ban_cell_new = list(set(list_ban_cell_new))
    return list_ban_cell_new


def del_choice_ship(screen):
    global cell, flag_automatic
    global flag_battleship, flag_cruiser_1, flag_cruiser_2, flag_destroyer_1, flag_destroyer_2, \
        flag_destroyer_3, flag_boat_1, flag_boat_2, flag_boat_3, flag_boat_4
    global flag_del_battleship, flag_del_cruiser_1, flag_del_cruiser_2, flag_del_destroyer_1, flag_del_destroyer_2, \
        flag_del_destroyer_3, flag_del_boat_1, flag_del_boat_2, flag_del_boat_3, flag_del_boat_4
    global list_my_ship, list_ban_cell, list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1, \
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4
    global flag_clear_field, flag_delete_ship, list_battleship
    flag_clear_field = True
    flag_delete_ship = False
    flag_automatic = False
    if flag_del_battleship:  # удаление линкора
        flag_del_battleship = False
        flag_battleship = False
        for i in list_my_battleship:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_battleship = []
        list_battleship = []
        if (750, 295) in list_chek:
            list_chek.remove((750, 295))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_cruiser_1:  # удаление крейсера_1
        flag_del_cruiser_1 = False
        flag_cruiser_1 = False
        for i in list_my_cruiser_1:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_cruiser_1 = []
        list_battleship = []
        if (750, 355) in list_chek:
            list_chek.remove((750, 355))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_cruiser_2:  # удаление крейсера_2
        flag_del_cruiser_2 = False
        flag_cruiser_2 = False
        for i in list_my_cruiser_2:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_cruiser_2 = []
        list_battleship = []
        if (750, 415) in list_chek:
            list_chek.remove((750, 415))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_destroyer_1:  # удаление эсминца_1
        flag_del_destroyer_1 = False
        flag_destroyer_1 = False
        for i in list_my_destroyer_1:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_destroyer_1 = []
        list_battleship = []
        if (750, 475) in list_chek:
            list_chek.remove((750, 475))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_destroyer_2:  # удаление эсминца_2
        flag_del_destroyer_2 = False
        flag_destroyer_2 = False
        for i in list_my_destroyer_2:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_destroyer_2 = []
        list_battleship = []
        if (750, 535) in list_chek:
            list_chek.remove((750, 535))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_destroyer_3:  # удаление эсминца_3
        flag_del_destroyer_3 = False
        flag_destroyer_3 = False
        for i in list_my_destroyer_3:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_destroyer_3 = []
        list_battleship = []
        if (1035, 295) in list_chek:
            list_chek.remove((1035, 295))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_boat_1:  # удаление катера_1
        flag_del_boat_1 = False
        flag_boat_1 = False
        for i in list_my_boat_1:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_boat_1 = []
        list_battleship = []
        if (1035, 355) in list_chek:
            list_chek.remove((1035, 355))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_boat_2:  # удаление катера_2
        flag_del_boat_2 = False
        flag_boat_2 = False
        for i in list_my_boat_2:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_boat_2 = []
        list_battleship = []
        if (1035, 415) in list_chek:
            list_chek.remove((1035, 415))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_boat_3:  # удаление катера_3
        flag_del_boat_3 = False
        flag_boat_3 = False
        for i in list_my_boat_3:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_boat_3 = []
        list_battleship = []
        if (1035, 475) in list_chek:
            list_chek.remove((1035, 475))
        list_ban_cell = new_list_ban_cell()
    elif flag_del_boat_4:  # удаление катера_4
        flag_del_boat_4 = False
        flag_boat_4 = False
        for i in list_my_boat_4:
            list_my_ship.remove(i)
        for i in list_battleship:
            list_my_ship.remove(i)
        list_my_boat_4 = []
        list_battleship = []
        if (1035, 535) in list_chek:
            list_chek.remove((1035, 535))
        list_ban_cell = new_list_ban_cell()
    pygame.Surface.fill(screen, (255, 250, 250), (30, 200, 1065, 490))
    notebook_sheet(screen)
    smail_def = pygame.image.load('picture/мой флот.png')
    screen.blit(smail_def, (165, 200))
    smail_def = pygame.image.load('picture/расставить корабли.png')
    screen.blit(smail_def, (540, 200))
    grid(screen, 120, 421, 300, 601)
    placement_ships(screen)
    pygame.Surface.fill(screen, (230, 230, 250), (90, 636, 274, 52))
    smail_def = pygame.image.load('picture/расставить.png')
    screen.blit(smail_def, (90, 636))
    pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 274, 52))
    smail_def = pygame.image.load('picture/очистить.png')
    screen.blit(smail_def, (420, 636))
    pygame.Surface.fill(screen, (230, 230, 250), (750, 636, 274, 52))
    smail_def = pygame.image.load('picture/дальше_2.png')
    screen.blit(smail_def, (750, 636))
    for i in list_chek:
        smail_def = pygame.image.load('picture/chek.png')
        screen.blit(smail_def, i)
    for i in list_my_ship:
        x_start = cell[i][0]
        y_start = cell[i][1]
        pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
        pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
    pygame.display.update((30, 200, 1065, 490))


def my_shot(screen, cell_number):
    global cell, cell_2, flag_sound, flag_game, flag_my_victory
    global flag_my_shot, flag_enemy_shot
    global list_enemy_ships, list_killed_enemy_ships, list_my_shot, list_injured_enemy_ships, number_whole_ships
    if cell_number not in list_my_shot and cell_number not in list_killed_enemy_ships \
            and cell_number not in list_injured_enemy_ships:
        if flag_sound:
            pygame.mixer.music.play()
        if flag_my_shot and not flag_enemy_shot:
            x_start = cell_2[cell_number][0]
            y_start = cell_2[cell_number][1]
        else:
            x_start = cell[cell_number][0]
            y_start = cell[cell_number][1]
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 20, 5)
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start - 15), (x_start + 16, y_start + 8), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start + 24), (x_start + 16, y_start + 47), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start - 15, y_start + 16), (x_start + 8, y_start + 16), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 24, y_start + 16), (x_start + 47, y_start + 16), 5)
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(800)
        smail = pygame.image.load('picture/взрыв.png')
        screen.blit(smail, (x_start - 10, y_start - 5))
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(1000)
        pygame.Surface.fill(screen, (255, 250, 250), rect=(500, 245, 370, 380))
        notebook_sheet(screen)
        grid(screen, 540, 841, 300, 601)
        if cell_number in list_enemy_ships:
            list_injured_enemy_ships.append(cell_number)
            if len(list(set(list_enemy_battleship) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_battleship:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_battleship)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_cruiser_1) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_cruiser_1:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_cruiser_1)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_cruiser_2) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_cruiser_2:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_cruiser_2)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_destroyer_1) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_destroyer_1:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_destroyer_1)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_destroyer_2) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_destroyer_2:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_destroyer_2)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_destroyer_3) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_destroyer_3:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_destroyer_3)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_boat_1) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_boat_1:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_boat_1)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_boat_2) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_boat_2:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_boat_2)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_boat_3) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_boat_3:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_boat_3)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
            if len(list(set(list_enemy_boat_4) - set(list_injured_enemy_ships))) == 0:
                for j in list_enemy_boat_4:
                    list_killed_enemy_ships.append(j)
                temp = ban_cell(list_enemy_boat_4)
                for i in temp:
                    list_my_shot.append(i)
                list_my_shot = list(set(list_my_shot))
        else:
            list_my_shot.append(cell_number)
            flag_my_shot = False
            flag_enemy_shot = True
        for i in list_injured_enemy_ships:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        list_killed_enemy_ships = list(set(list_killed_enemy_ships))
        for i in list_killed_enemy_ships:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_my_shot:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
    pygame.display.update((500, 245, 370, 380))
    if len(list_killed_enemy_ships) == 20:
        flag_game = False
        flag_my_victory = True
        write_statistics()
        pygame.time.wait(2000)


def beginner_enemy_shot(screen):
    global cell, cell_2, flag_sound, flag_game, flag_enemy_victory, flag_my_shot_injured
    global flag_my_shot, flag_enemy_shot, handicap_beginner
    global list_my_ship, list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1, \
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4, \
        list_killed_my_ships, list_injured_my_ships, list_enemy_shot, list_killed_enemy_ships, number_whole_ships
    global flag_local_battleship, flag_local_cruiser_1, flag_local_cruiser_2, flag_local_destroyer_1, \
        flag_local_destroyer_2, flag_local_destroyer_3, flag_local_boat_1,\
        flag_local_boat_2, flag_local_boat_3, flag_local_boat_4
    if flag_enemy_shot:
        if not flag_my_shot_injured:
            cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot) - set(list_killed_my_ships)
                                             - set(list_injured_my_ships)))
            if cell_number in list_my_ship and handicap_beginner > 0:
                while cell_number in list_my_ship:
                    cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot)
                                                     - set(list_killed_my_ships) - set(list_injured_my_ships)))
                handicap_beginner -= 1
            x_start = cell[cell_number][0]
            y_start = cell[cell_number][1]
        else:
            if len(list_injured_my_ships) == 1:
                tmp = generator(list_injured_my_ships[0], 2)
                cell_number = random.choice(list(set(tmp) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            elif len(list_injured_my_ships) == 2:
                tmp = generator(list_injured_my_ships[0], 3)
                tmp_1 = reduction(list_injured_my_ships, tmp, 3)
                cell_number = random.choice(list(set(tmp_1) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            elif len(list_injured_my_ships) == 3:
                tmp = generator(list_injured_my_ships[0], 4)
                tmp_1 = reduction(list_injured_my_ships, tmp, 4)
                cell_number = random.choice(list(set(tmp_1) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            else:
                cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
        if flag_sound:
            pygame.mixer.music.play()
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 20, 5)
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start - 15), (x_start + 16, y_start + 8), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start + 24), (x_start + 16, y_start + 47), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start - 15, y_start + 16), (x_start + 8, y_start + 16), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 24, y_start + 16), (x_start + 47, y_start + 16), 5)
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(800)
        smail = pygame.image.load('picture/взрыв.png')
        screen.blit(smail, (x_start - 10, y_start - 5))
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(1000)
        if cell_number in list_my_ship:
            flag_my_shot_injured = True
            list_injured_my_ships.append(cell_number)
            if flag_local_battleship and len(list(set(list_my_battleship) - set(list_injured_my_ships))) == 0:
                for j in list_my_battleship:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_battleship)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_battleship = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_cruiser_1 and len(list(set(list_my_cruiser_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_cruiser_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_cruiser_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_cruiser_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_cruiser_2 and len(list(set(list_my_cruiser_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_cruiser_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_cruiser_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_cruiser_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_1 and len(list(set(list_my_destroyer_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_2 and len(list(set(list_my_destroyer_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_3 and len(list(set(list_my_destroyer_3) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_3:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_3)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_3 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_1 and len(list(set(list_my_boat_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_2 and len(list(set(list_my_boat_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_3 and len(list(set(list_my_boat_3) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_3:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_3)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_3 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_4 and len(list(set(list_my_boat_4) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_4:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_4)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_4 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
        else:
            list_enemy_shot.append(cell_number)
            flag_my_shot = True
            flag_enemy_shot = False
        pygame.Surface.fill(screen, (255, 250, 250), rect=(90, 260, 350, 360))
        notebook_sheet(screen)
        grid(screen, 120, 421, 300, 601)
        for i in list_my_ship:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        for i in list_injured_my_ships:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        list_killed_my_ships = list(set(list_killed_my_ships))
        for i in list_killed_my_ships:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_enemy_shot:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
    pygame.display.update((90, 260, 350, 360))
    if len(list_killed_my_ships) == 20:
        flag_enemy_victory = True
        flag_game = False
        write_statistics()
        pygame.Surface.fill(screen, (255, 250, 250), rect=(500, 245, 370, 380))
        notebook_sheet(screen)
        grid(screen, 540, 841, 300, 601)
        for i in list_enemy_ships:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        list_victory_enemy = list((set(list_killed_enemy_ships) | set(list_injured_enemy_ships)))
        for i in list_victory_enemy:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_my_shot:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.display.update((500, 245, 370, 380))
        pygame.time.wait(3000)


def master_enemy_shot(screen):
    global cell, cell_2, flag_sound, flag_game, flag_enemy_victory, flag_my_shot_injured
    global flag_my_shot, flag_enemy_shot
    global list_my_ship, list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1, \
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4, \
        list_killed_my_ships, list_injured_my_ships, list_enemy_shot, list_killed_enemy_ships, number_whole_ships
    global flag_local_battleship, flag_local_cruiser_1, flag_local_cruiser_2, flag_local_destroyer_1, \
        flag_local_destroyer_2, flag_local_destroyer_3, flag_local_boat_1,\
        flag_local_boat_2, flag_local_boat_3, flag_local_boat_4
    if flag_enemy_shot:
        if not flag_my_shot_injured:
            one_list = [1, 4, 7, 10, 13, 16, 19, 22, 25, 28, 31, 34, 37, 40, 43, 46, 49, 52, 55, 58, 61, 64, 67,
                        70, 73, 76, 79, 82, 85, 88, 91, 94, 97, 100]
            if len(list(set(one_list) - set(list_enemy_shot)
                        - set(list_killed_my_ships) - set(list_injured_my_ships))) > 0:
                cell_number = random.choice(list(set(one_list) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
            else:
                cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
            x_start = cell[cell_number][0]
            y_start = cell[cell_number][1]
        else:
            if len(list_injured_my_ships) == 1:
                tmp = generator(list_injured_my_ships[0], 2)
                cell_number = random.choice(list(set(tmp) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            elif len(list_injured_my_ships) == 2:
                tmp = generator(list_injured_my_ships[0], 3)
                tmp_1 = reduction(list_injured_my_ships, tmp, 3)
                cell_number = random.choice(list(set(tmp_1) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            elif len(list_injured_my_ships) == 3:
                tmp = generator(list_injured_my_ships[0], 4)
                tmp_1 = reduction(list_injured_my_ships, tmp, 4)
                cell_number = random.choice(list(set(tmp_1) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            else:
                cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
        if flag_sound:
            pygame.mixer.music.play()
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 20, 5)
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start - 15), (x_start + 16, y_start + 8), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start + 24), (x_start + 16, y_start + 47), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start - 15, y_start + 16), (x_start + 8, y_start + 16), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 24, y_start + 16), (x_start + 47, y_start + 16), 5)
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(800)
        smail = pygame.image.load('picture/взрыв.png')
        screen.blit(smail, (x_start - 10, y_start - 5))
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(1000)
        if cell_number in list_my_ship:
            flag_my_shot_injured = True
            list_injured_my_ships.append(cell_number)
            if flag_local_battleship and len(list(set(list_my_battleship) - set(list_injured_my_ships))) == 0:
                for j in list_my_battleship:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_battleship)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_battleship = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_cruiser_1 and len(list(set(list_my_cruiser_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_cruiser_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_cruiser_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_cruiser_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_cruiser_2 and len(list(set(list_my_cruiser_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_cruiser_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_cruiser_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_cruiser_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_1 and len(list(set(list_my_destroyer_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_2 and len(list(set(list_my_destroyer_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_3 and len(list(set(list_my_destroyer_3) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_3:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_3)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_3 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_1 and len(list(set(list_my_boat_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_2 and len(list(set(list_my_boat_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_3 and len(list(set(list_my_boat_3) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_3:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_3)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_3 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_4 and len(list(set(list_my_boat_4) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_4:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_4)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_4 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
        else:
            list_enemy_shot.append(cell_number)
            flag_my_shot = True
            flag_enemy_shot = False
        pygame.Surface.fill(screen, (255, 250, 250), rect=(90, 260, 350, 360))
        notebook_sheet(screen)
        grid(screen, 120, 421, 300, 601)
        for i in list_my_ship:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        for i in list_injured_my_ships:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        list_killed_my_ships = list(set(list_killed_my_ships))
        for i in list_killed_my_ships:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_enemy_shot:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
    pygame.display.update((90, 260, 350, 360))
    if len(list_killed_my_ships) == 20:
        flag_enemy_victory = True
        flag_game = False
        write_statistics()
        pygame.Surface.fill(screen, (255, 250, 250), rect=(500, 245, 370, 380))
        notebook_sheet(screen)
        grid(screen, 540, 841, 300, 601)
        for i in list_enemy_ships:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        list_victory_enemy = list((set(list_killed_enemy_ships) | set(list_injured_enemy_ships)))
        for i in list_victory_enemy:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_my_shot:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.display.update((500, 245, 370, 380))
        pygame.time.wait(3000)


def strategy_3():
    global list_enemy_shot, list_killed_my_ships, list_injured_my_ships, flag_strategy_3, flag_strategy_4
    cnt = np.arange(1, 101).reshape((10, 10))
    my_list = []
    shot = list(set(list_enemy_shot) | set(list_killed_my_ships) | set(list_injured_my_ships))
    for i in shot:
        if 1 <= i <= 10:
            cnt[0, i - 1] = 0
        elif i in [10, 20, 30, 40, 50, 60, 70, 80, 90]:
            i = str(i)
            row = int(i[0]) - 1
            column = 9
            cnt[row, column] = 0
        elif i == 100:
            row = 9
            column = 9
            cnt[row, column] = 0
        else:
            i = str(i)
            row = int(i[0])
            column = int(i[1]) - 1
            cnt[row, column] = 0
    for row in cnt:
        len_row = 0
        len_row_max = 0
        for i in row:
            if i == 0:
                if len_row > len_row_max:
                    len_row_max = len_row
                len_row = 0
            else:
                len_row += 1
        if len_row > len_row_max:
            my_list.append(len_row)
        else:
            my_list.append(len_row_max)
    my_list_max_horizont = max(my_list)
    index_my_list = my_list.index(my_list_max_horizont)
    list_shot_1 = cnt[index_my_list: index_my_list + 1]
    cnt_1 = cnt.transpose()
    my_list = []
    for row in cnt_1:
        len_row = 0
        len_row_max = 0
        for i in row:
            if i == 0:
                if len_row > len_row_max:
                    len_row_max = len_row
                len_row = 0
            else:
                len_row += 1
        if len_row > len_row_max:
            my_list.append(len_row)
        else:
            my_list.append(len_row_max)
    my_list_max_vertical = max(my_list)
    index_my_list = my_list.index(my_list_max_vertical)
    list_shot_2 = cnt_1[index_my_list: index_my_list + 1]
    if my_list_max_horizont > my_list_max_vertical:
        list_shot = list_shot_1
    else:
        list_shot = list_shot_2
    len_row = 0
    len_row_max = 0
    list_row = []
    list_row_1 = []
    for i in list_shot[0]:
        if i == 0:
            if len_row > len_row_max:
                len_row_max = len_row
                list_row_1 = list_row.copy()
            len_row = 0
            list_row = []
        else:
            len_row += 1
            list_row.append(i)
    if len_row > len_row_max:
        list_row_1 = list_row.copy()
    cell_number = list_row_1[len(list_row_1) // 2]
    if my_list_max_horizont == my_list_max_vertical == 1:
        flag_strategy_4 = True
        flag_strategy_3 = False
    return cell_number


def professional_enemy_shot(screen):
    global cell, cell_2, flag_sound, flag_game, flag_enemy_victory, flag_my_shot_injured
    global flag_my_shot, flag_enemy_shot
    global list_my_ship, list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1, \
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4, \
        list_killed_my_ships, list_injured_my_ships, list_enemy_shot, list_killed_enemy_ships
    global flag_strategy_1, flag_strategy_2, flag_strategy_3, flag_strategy_4, number_whole_ships
    global flag_local_battleship, flag_local_cruiser_1, flag_local_cruiser_2, flag_local_destroyer_1, \
        flag_local_destroyer_2, flag_local_destroyer_3, flag_local_boat_1,\
        flag_local_boat_2, flag_local_boat_3, flag_local_boat_4
    one_list = []
    cell_number = 0
    if flag_enemy_shot:
        if not flag_my_shot_injured:
            if not flag_strategy_1 and not flag_strategy_2 and not flag_strategy_3 and not flag_strategy_4:
                n = random.randint(0, 1)
                if n == 0:
                    flag_strategy_1 = True
                elif n == 1:
                    flag_strategy_2 = True
            if flag_strategy_1:
                one_list = [4, 8, 13, 17, 22, 26, 30, 31, 35, 39, 44, 48, 53, 57, 62, 66, 70,
                            71, 75, 79, 84, 88, 93, 97]
            elif flag_strategy_2:
                one_list = [4, 8, 13, 17, 21, 25, 29, 32, 36, 40, 44, 48, 53, 57, 61, 65, 69,
                            72, 76, 80, 84, 88, 93, 97]
            if len(list(set(one_list) - set(list_enemy_shot)
                        - set(list_killed_my_ships) - set(list_injured_my_ships))) > 0:
                cell_number = random.choice(list(set(one_list) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
            elif not flag_strategy_3 and len(list(set(one_list) - set(list_enemy_shot)
                                                  - set(list_killed_my_ships) - set(list_injured_my_ships))) == 0:
                flag_strategy_1 = False
                flag_strategy_2 = False
                flag_strategy_3 = True
                cell_number = strategy_3()
            elif flag_strategy_3:
                cell_number = strategy_3()
            if flag_strategy_4:
                cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
            x_start = cell[cell_number][0]
            y_start = cell[cell_number][1]
        else:
            if len(list_injured_my_ships) == 1:
                tmp = generator(list_injured_my_ships[0], 2)
                cell_number = random.choice(list(set(tmp) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            elif len(list_injured_my_ships) == 2:
                tmp = generator(list_injured_my_ships[0], 3)
                tmp_1 = reduction(list_injured_my_ships, tmp, 3)
                cell_number = random.choice(list(set(tmp_1) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            elif len(list_injured_my_ships) == 3:
                tmp = generator(list_injured_my_ships[0], 4)
                tmp_1 = reduction(list_injured_my_ships, tmp, 4)
                cell_number = random.choice(list(set(tmp_1) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
            else:
                cell_number = random.choice(list(set(range(1, 101)) - set(list_enemy_shot)
                                                 - set(list_killed_my_ships) - set(list_injured_my_ships)))
                x_start = cell[cell_number][0]
                y_start = cell[cell_number][1]
        if flag_sound:
            pygame.mixer.music.play()
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 20, 5)
        pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start - 15), (x_start + 16, y_start + 8), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 16, y_start + 24), (x_start + 16, y_start + 47), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start - 15, y_start + 16), (x_start + 8, y_start + 16), 5)
        pygame.draw.line(screen, (0, 0, 128), (x_start + 24, y_start + 16), (x_start + 47, y_start + 16), 5)
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(800)
        smail = pygame.image.load('picture/взрыв.png')
        screen.blit(smail, (x_start - 10, y_start - 5))
        pygame.display.update((x_start - 20, y_start - 20, 70, 70))
        pygame.time.wait(1000)
        if cell_number in list_my_ship:
            flag_my_shot_injured = True
            list_injured_my_ships.append(cell_number)
            if flag_local_battleship and len(list(set(list_my_battleship) - set(list_injured_my_ships))) == 0:
                for j in list_my_battleship:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_battleship)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_battleship = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_cruiser_1 and len(list(set(list_my_cruiser_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_cruiser_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_cruiser_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_cruiser_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_cruiser_2 and len(list(set(list_my_cruiser_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_cruiser_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_cruiser_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_cruiser_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_1 and len(list(set(list_my_destroyer_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_2 and len(list(set(list_my_destroyer_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_destroyer_3 and len(list(set(list_my_destroyer_3) - set(list_injured_my_ships))) == 0:
                for j in list_my_destroyer_3:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_destroyer_3)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_destroyer_3 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_1 and len(list(set(list_my_boat_1) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_1:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_1)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_1 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_2 and len(list(set(list_my_boat_2) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_2:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_2)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_2 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_3 and len(list(set(list_my_boat_3) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_3:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_3)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_3 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
            if flag_local_boat_4 and len(list(set(list_my_boat_4) - set(list_injured_my_ships))) == 0:
                for j in list_my_boat_4:
                    list_killed_my_ships.append(j)
                temp = ban_cell(list_my_boat_4)
                for i in temp:
                    list_enemy_shot.append(i)
                list_enemy_shot = list(set(list_enemy_shot))
                flag_my_shot_injured = False
                flag_local_boat_4 = False
                list_injured_my_ships = []
                number_whole_ships -= 1
        else:
            list_enemy_shot.append(cell_number)
            flag_my_shot = True
            flag_enemy_shot = False
        pygame.Surface.fill(screen, (255, 250, 250), rect=(90, 260, 350, 360))
        notebook_sheet(screen)
        grid(screen, 120, 421, 300, 601)
        for i in list_my_ship:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        for i in list_injured_my_ships:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        list_killed_my_ships = list(set(list_killed_my_ships))
        for i in list_killed_my_ships:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_enemy_shot:
            x_start = cell[i][0]
            y_start = cell[i][1]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
    pygame.display.update((90, 260, 350, 360))
    if len(list_killed_my_ships) == 20:
        flag_enemy_victory = True
        flag_game = False
        write_statistics()
        pygame.Surface.fill(screen, (255, 250, 250), rect=(500, 245, 370, 380))
        notebook_sheet(screen)
        grid(screen, 540, 841, 300, 601)
        for i in list_enemy_ships:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
        list_victory_enemy = list((set(list_killed_enemy_ships) | set(list_injured_enemy_ships)))
        for i in list_victory_enemy:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.draw.line(screen, (255, 0, 0), (x_start - 5, y_start - 5), (x_start + 35, y_start + 35), 5)
            pygame.draw.line(screen, (255, 0, 0), (x_start + 35, y_start - 5), (x_start - 5, y_start + 35), 5)
        for i in list_my_shot:
            x_start = cell_2[i][0]
            y_start = cell_2[i][1]
            pygame.draw.circle(screen, (0, 0, 128), (x_start + 16, y_start + 16), 5, 5)
        pygame.display.update((500, 245, 370, 380))
        pygame.time.wait(3000)


def victory(screen):
    global flag_my_victory, flag_enemy_victory, difficulty_level
    """функция конец игры - выиграл/проиграл"""
    pygame.Surface.fill(screen, (255, 250, 250), (30, 190, 1055, 490))
    notebook_sheet(screen)
    pygame.Surface.fill(screen, (230, 230, 250), (749, 240, 333, 62))
    smail_def = pygame.image.load('picture/статистика.png')
    screen.blit(smail_def, (749, 240))
    pygame.Surface.fill(screen, (230, 230, 250), (749, 360, 333, 62))
    smail_def = pygame.image.load('picture/новая игра.png')
    screen.blit(smail_def, (749, 360))
    pygame.Surface.fill(screen, (230, 230, 250), (749, 480, 333, 62))
    smail_def = pygame.image.load('picture/выход.png')
    screen.blit(smail_def, (749, 480))
    pygame.Surface.fill(screen, (230, 230, 250), (810, 600, 211, 62))
    smail_def = pygame.image.load('picture/файл.png')
    screen.blit(smail_def, (810, 600))
    if flag_my_victory and not flag_enemy_victory:
        list_awards = [['picture/отличник вмф.png', (220, 244), (295, 200)],
                       ['picture/медаль адмирал горшков.png', (150, 244), (325, 200)],
                       ['picture/медаль адмирал кузнецов.png', (150, 244), (325, 200)],
                       ['picture/медаль_нахимова.png', (130, 244), (335, 200)],
                       ['picture/медаль_ушакова.png', (130, 244), (340, 200)],
                       ['picture/орден_нахимова_2.png', (250, 244), (280, 200)],
                       ['picture/орден_нахимова_1.png', (250, 244), (280, 200)],
                       ['picture/орден_ушакова_2.png', (250, 244), (280, 200)],
                       ['picture/орден_ушакова_1.png',  (250, 244), (280, 200)],
                       ['picture/пробел.png', (250, 244), (280, 200)]]
        my_file = open('my_statistic.txt', 'r', encoding='utf-8')
        list_statistic = []
        awards = ''
        size = (250, 244)
        position = (280, 200)
        for line in my_file:
            tmp = list(line.split())
            list_statistic.append(tmp)
        smail_def = pygame.image.load('picture/lenta-13-0.png')
        screen.blit(smail_def, (30, 520))
        for i in list_statistic:
            if i[0] == difficulty_level and i[0] == 'beginner':
                if 3 > int(i[2]):  # до 3х побед
                    awards = list_awards[9][0]
                    size = list_awards[9][1]
                    position = list_awards[9][2]
                elif 3 <= int(i[2]) < 7:  # отличник ВМФ
                    awards = list_awards[0][0]
                    size = list_awards[0][1]
                    position = list_awards[0][2]
                elif 7 <= int(i[2]) < 10:  # медаль адмирал горшков
                    awards = list_awards[1][0]
                    size = list_awards[1][1]
                    position = list_awards[1][2]
                elif 10 <= int(i[2]) < 20:  # медаль адмирал кузнецов
                    awards = list_awards[2][0]
                    size = list_awards[2][1]
                    position = list_awards[2][2]
                elif 20 <= int(i[2]) < 30:  # медаль нахимова
                    awards = list_awards[3][0]
                    size = list_awards[3][1]
                    position = list_awards[3][2]
                elif 30 <= int(i[2]) < 40:  # медаль ушакова
                    awards = list_awards[4][0]
                    size = list_awards[4][1]
                    position = list_awards[4][2]
                elif 40 <= int(i[2]) < 50:  # орден нахимома_2
                    awards = list_awards[5][0]
                    size = list_awards[5][1]
                    position = list_awards[5][2]
                elif 50 <= int(i[2]) < 60:  # орден нахимова_1
                    awards = list_awards[6][0]
                    size = list_awards[6][1]
                    position = list_awards[6][2]
                elif 60 <= int(i[2]) < 70:  # орден ушакова_2
                    awards = list_awards[7][0]
                    size = list_awards[7][1]
                    position = list_awards[7][2]
                elif 70 <= int(i[2]):  # орден ушакова_1
                    awards = list_awards[8][0]
                    size = list_awards[8][1]
                    position = list_awards[8][2]
            elif i[0] == difficulty_level and i[0] == 'master':
                if 2 > int(i[2]):
                    awards = list_awards[9][0]
                    size = list_awards[9][1]
                    position = list_awards[9][2]
                elif 2 <= int(i[2]) < 5:
                    awards = list_awards[0][0]
                    size = list_awards[0][1]
                    position = list_awards[0][2]
                elif 5 <= int(i[2]) < 7:
                    awards = list_awards[1][0]
                    size = list_awards[1][1]
                    position = list_awards[1][2]
                elif 7 <= int(i[2]) < 15:
                    awards = list_awards[2][0]
                    size = list_awards[2][1]
                    position = list_awards[2][2]
                elif 15 <= int(i[2]) < 20:
                    awards = list_awards[3][0]
                    size = list_awards[3][1]
                    position = list_awards[3][2]
                elif 20 <= int(i[2]) < 25:
                    awards = list_awards[4][0]
                    size = list_awards[4][1]
                    position = list_awards[4][2]
                elif 25 <= int(i[2]) < 30:
                    awards = list_awards[5][0]
                    size = list_awards[5][1]
                    position = list_awards[5][2]
                elif 30 <= int(i[2]) < 35:
                    awards = list_awards[6][0]
                    size = list_awards[6][1]
                    position = list_awards[6][2]
                elif 35 <= int(i[2]) < 40:
                    awards = list_awards[7][0]
                    size = list_awards[7][1]
                    position = list_awards[7][2]
                elif 40 <= int(i[2]):
                    awards = list_awards[8][0]
                    size = list_awards[8][1]
                    position = list_awards[8][2]
            elif i[0] == difficulty_level and i[0] == 'professional':
                if 1 > int(i[2]):
                    awards = list_awards[9][0]
                    size = list_awards[9][1]
                    position = list_awards[9][2]
                elif 1 <= int(i[2]) < 3:
                    awards = list_awards[0][0]
                    size = list_awards[0][1]
                    position = list_awards[0][2]
                elif 3 <= int(i[2]) < 5:
                    awards = list_awards[1][0]
                    size = list_awards[1][1]
                    position = list_awards[1][2]
                elif 5 <= int(i[2]) < 7:
                    awards = list_awards[2][0]
                    size = list_awards[2][1]
                    position = list_awards[2][2]
                elif 7 <= int(i[2]) < 10:
                    awards = list_awards[3][0]
                    size = list_awards[3][1]
                    position = list_awards[3][2]
                elif 10 <= int(i[2]) < 15:
                    awards = list_awards[4][0]
                    size = list_awards[4][1]
                    position = list_awards[4][2]
                elif 15 <= int(i[2]) < 20:
                    awards = list_awards[5][0]
                    size = list_awards[5][1]
                    position = list_awards[5][2]
                elif 20 <= int(i[2]) < 25:
                    awards = list_awards[6][0]
                    size = list_awards[6][1]
                    position = list_awards[6][2]
                elif 25 <= int(i[2]) < 30:
                    awards = list_awards[7][0]
                    size = list_awards[7][1]
                    position = list_awards[7][2]
                elif 30 <= int(i[2]):
                    awards = list_awards[8][0]
                    size = list_awards[8][1]
                    position = list_awards[8][2]
        smail_def = pygame.image.load(awards).convert_alpha()
        smail_def = pygame.transform.scale(smail_def, size)
        screen.blit(smail_def, position)
        smail_def = pygame.image.load('picture/ты победил.png')
        screen.blit(smail_def, (140, 430))
        my_file.close()
    elif not flag_my_victory and flag_enemy_victory:
        smail_def = pygame.image.load('picture/корабли.png')
        screen.blit(smail_def, (270, 170))
        smail_def = pygame.image.load('picture/лента.png')
        screen.blit(smail_def, (-10, 400))
        smail_def = pygame.image.load('picture/ты проиграл.png')
        screen.blit(smail_def, (135, 440))


def write_statistics():
    global difficulty_level, flag_my_victory, flag_enemy_victory, number_moves, number_whole_ships
    my_file = open('my_statistic.txt', 'r', encoding='utf-8')
    list_statistic = []
    for line in my_file:
        tmp = list(line.split())
        list_statistic.append(tmp)
    my_file.close()
    my_file = open('my_statistic.txt', 'w', encoding='utf-8')
    for i in list_statistic:
        if i[0] == difficulty_level:
            i[1] = str(int(i[1]) + 1)
            if flag_my_victory and not flag_enemy_victory:
                i[2] = str(int(i[2]) + 1)
                if int(i[3]) < int(number_moves):
                    i[3] = str(number_moves)
                    i[4] = str(number_whole_ships)
        print(*i, file=my_file)
    my_file.close()


def print_statistics(screen):
    global flag_select_beginner, flag_select_master, flag_select_professional
    pygame.Surface.fill(screen, (255, 250, 250), (30, 200, 1055, 490))
    notebook_sheet(screen)
    pygame.Surface.fill(screen, (230, 230, 250), (90, 606, 274, 51))
    smail_def = pygame.image.load('picture/назад.png')
    screen.blit(smail_def, (90, 606))
    pygame.Surface.fill(screen, (230, 230, 250), (420, 606, 274, 51))
    smail_def = pygame.image.load('picture/очистить.png')
    screen.blit(smail_def, (420, 606))
    pygame.Surface.fill(screen, (230, 230, 250), (750, 606, 274, 51))
    smail_def = pygame.image.load('picture/выход_2.png')
    screen.blit(smail_def, (750, 606))
    if flag_select_beginner:
        pygame.Surface.fill(screen, (192, 192, 192), (30, 322, 1055, 46))
    elif flag_select_master:
        pygame.Surface.fill(screen, (192, 192, 192), (30, 412, 1055, 46))
    elif flag_select_professional:
        pygame.Surface.fill(screen, (192, 192, 192), (30, 502, 1055, 46))
    smail_def = pygame.image.load('picture/новичок_2.png')
    screen.blit(smail_def, (90, 322))
    smail_def = pygame.image.load('picture/мастер_2.png')
    screen.blit(smail_def, (90, 412))
    smail_def = pygame.image.load('picture/профессионал.png')
    screen.blit(smail_def, (30, 502))
    smail_def = pygame.image.load('picture/количество игр.png')
    screen.blit(smail_def, (325, 210))
    smail_def = pygame.image.load('picture/количество побед.png')
    screen.blit(smail_def, (505, 210))
    smail_def = pygame.image.load('picture/лучший результат.png')
    screen.blit(smail_def, (675, 210))
    smail_def = pygame.image.load('picture/награда.png')
    screen.blit(smail_def, (910, 230))
    list_awards = [['picture/отличник вмф.png', (60, 80), (960, 305), (960, 395), (960, 485)],
                   ['picture/медаль адмирал горшков.png', (50, 75), (964, 309), (964, 399), (964, 489)],
                   ['picture/медаль адмирал кузнецов.png', (50, 75), (965, 309), (965, 399), (965, 489)],
                   ['picture/медаль_нахимова.png', (50, 75), (965, 309), (965, 399), (965, 489)],
                   ['picture/медаль_ушакова.png', (45, 75), (967, 309), (967, 399), (967, 489)],
                   ['picture/орден_нахимова_2.png', (80, 80), (950, 305), (950, 395), (950, 485)],
                   ['picture/орден_нахимова_1.png', (80, 80), (950, 305), (950, 395), (950, 485)],
                   ['picture/орден_ушакова_2.png', (80, 80), (950, 305), (950, 395), (950, 485)],
                   ['picture/орден_ушакова_1.png', (80, 80), (950, 305), (950, 395), (950, 485)],
                   ['picture/пробел.png', (80, 80), (950, 305), (950, 395), (950, 485)]]
    awards = ''
    size = (80, 80)
    position = (280, 200)
    for i in range(190, 560, 90):
        text(screen, 25, '-' * 131, (30, i), (80, 123, 175))
    for i in range(300, 700, 180):
        for j in range(220, 500, 90):
            pygame.draw.line(screen, (80, 123, 175), (i, j), (i, j + 70), 3)
    for i in range(220, 500, 90):
        pygame.draw.line(screen, (80, 123, 175), (900, i), (900, i + 70), 3)
    my_file = open('my_statistic.txt', 'r', encoding='utf-8')
    for line in my_file:
        tmp = list(line.split())
        if tmp[0] == 'beginner':
            len_tmp = (42 - 14 * len(tmp[1]))
            text(screen, 40, tmp[1], (350 + len_tmp, 315), (0, 255, 0))
            len_tmp = (42 - 14 * len(tmp[2]))
            text(screen, 40, tmp[2], (530 + len_tmp, 315), (255, 0, 0))
            len_tmp = (28 - 14 * len(tmp[3]))
            text(screen, 40, tmp[3], (693 + len_tmp, 315), (0, 255, 0))
            len_tmp = (28 - 14 * len(tmp[4]))
            text(screen, 40, tmp[4], (813 + len_tmp, 315), (70, 130, 180))
            if 3 > int(tmp[2]):
                awards = list_awards[9][0]
                size = list_awards[9][1]
                position = list_awards[9][2]
            elif 3 <= int(tmp[2]) < 7:
                awards = list_awards[0][0]
                size = list_awards[0][1]
                position = list_awards[0][2]
            elif 7 <= int(tmp[2]) < 10:
                awards = list_awards[1][0]
                size = list_awards[1][1]
                position = list_awards[1][2]
            elif 10 <= int(tmp[2]) < 20:
                awards = list_awards[2][0]
                size = list_awards[2][1]
                position = list_awards[2][2]
            elif 20 <= int(tmp[2]) < 30:
                awards = list_awards[3][0]
                size = list_awards[3][1]
                position = list_awards[3][2]
            elif 30 <= int(tmp[2]) < 40:
                awards = list_awards[4][0]
                size = list_awards[4][1]
                position = list_awards[4][2]
            elif 40 <= int(tmp[2]) < 50:
                awards = list_awards[5][0]
                size = list_awards[5][1]
                position = list_awards[5][2]
            elif 50 <= int(tmp[2]) < 60:
                awards = list_awards[6][0]
                size = list_awards[6][1]
                position = list_awards[6][2]
            elif 60 <= int(tmp[2]) < 70:
                awards = list_awards[7][0]
                size = list_awards[7][1]
                position = list_awards[7][2]
            elif 70 <= int(tmp[2]):
                awards = list_awards[8][0]
                size = list_awards[8][1]
                position = list_awards[8][2]
            smail_def = pygame.image.load(awards).convert_alpha()
            smail_def = pygame.transform.scale(smail_def, size)
            screen.blit(smail_def, position)
        elif tmp[0] == 'master':
            len_tmp = (42 - 14 * len(tmp[1]))
            text(screen, 40, tmp[1], (350 + len_tmp, 405), (0, 255, 0))
            len_tmp = (42 - 14 * len(tmp[2]))
            text(screen, 40, tmp[2], (530 + len_tmp, 405), (255, 0, 0))
            len_tmp = (28 - 14 * len(tmp[3]))
            text(screen, 40, tmp[3], (693 + len_tmp, 405), (0, 255, 0))
            len_tmp = (28 - 14 * len(tmp[4]))
            text(screen, 40, tmp[4], (813 + len_tmp, 405), (70, 130, 180))
            if 2 > int(tmp[2]):
                awards = list_awards[9][0]
                size = list_awards[9][1]
                position = list_awards[9][3]
            elif 2 <= int(tmp[2]) < 5:
                awards = list_awards[0][0]
                size = list_awards[0][1]
                position = list_awards[0][3]
            elif 5 <= int(tmp[2]) < 7:
                awards = list_awards[1][0]
                size = list_awards[1][1]
                position = list_awards[1][3]
            elif 7 <= int(tmp[2]) < 15:
                awards = list_awards[2][0]
                size = list_awards[2][1]
                position = list_awards[2][3]
            elif 15 <= int(tmp[2]) < 20:
                awards = list_awards[3][0]
                size = list_awards[3][1]
                position = list_awards[3][3]
            elif 20 <= int(tmp[2]) < 25:
                awards = list_awards[4][0]
                size = list_awards[4][1]
                position = list_awards[4][3]
            elif 25 <= int(tmp[2]) < 30:
                awards = list_awards[5][0]
                size = list_awards[5][1]
                position = list_awards[5][3]
            elif 30 <= int(tmp[2]) < 35:
                awards = list_awards[6][0]
                size = list_awards[6][1]
                position = list_awards[6][3]
            elif 35 <= int(tmp[2]) < 40:
                awards = list_awards[7][0]
                size = list_awards[7][1]
                position = list_awards[7][3]
            elif 40 <= int(tmp[2]):
                awards = list_awards[8][0]
                size = list_awards[8][1]
                position = list_awards[8][3]
            smail_def = pygame.image.load(awards).convert_alpha()
            smail_def = pygame.transform.scale(smail_def, size)
            screen.blit(smail_def, position)
        elif tmp[0] == 'professional':
            len_tmp = (42 - 14 * len(tmp[1]))
            text(screen, 40, tmp[1], (350 + len_tmp, 495), (0, 255, 0))
            len_tmp = (42 - 14 * len(tmp[2]))
            text(screen, 40, tmp[2], (530 + len_tmp, 495), (255, 0, 0))
            len_tmp = (28 - 14 * len(tmp[3]))
            text(screen, 40, tmp[3], (693 + len_tmp, 495), (0, 255, 0))
            len_tmp = (28 - 14 * len(tmp[4]))
            text(screen, 40, tmp[4], (813 + len_tmp, 495), (70, 130, 180))
            if 1 > int(tmp[2]):
                awards = list_awards[9][0]
                size = list_awards[9][1]
                position = list_awards[9][4]
            elif 1 <= int(tmp[2]) < 3:
                awards = list_awards[0][0]
                size = list_awards[0][1]
                position = list_awards[0][4]
            elif 3 <= int(tmp[2]) < 5:
                awards = list_awards[1][0]
                size = list_awards[1][1]
                position = list_awards[1][4]
            elif 5 <= int(tmp[2]) < 7:
                awards = list_awards[2][0]
                size = list_awards[2][1]
                position = list_awards[2][4]
            elif 7 <= int(tmp[2]) < 10:
                awards = list_awards[3][0]
                size = list_awards[3][1]
                position = list_awards[3][4]
            elif 10 <= int(tmp[2]) < 15:
                awards = list_awards[4][0]
                size = list_awards[4][1]
                position = list_awards[4][4]
            elif 15 <= int(tmp[2]) < 20:
                awards = list_awards[5][0]
                size = list_awards[5][1]
                position = list_awards[5][4]
            elif 20 <= int(tmp[2]) < 25:
                awards = list_awards[6][0]
                size = list_awards[6][1]
                position = list_awards[6][4]
            elif 25 <= int(tmp[2]) < 30:
                awards = list_awards[7][0]
                size = list_awards[7][1]
                position = list_awards[7][4]
            elif 30 <= int(tmp[2]):
                awards = list_awards[8][0]
                size = list_awards[8][1]
                position = list_awards[8][4]
            smail_def = pygame.image.load(awards).convert_alpha()
            smail_def = pygame.transform.scale(smail_def, size)
            screen.blit(smail_def, position)
    pygame.display.update((30, 200, 1055, 490))


def clear_statistics():
    global flag_select_beginner, flag_select_master, flag_select_professional
    my_file = open('my_statistic.txt', 'r', encoding='utf-8')
    list_statistic = []
    for line in my_file:
        tmp = list(line.split())
        list_statistic.append(tmp)
    my_file.close()
    my_file = open('my_statistic.txt', 'w', encoding='utf-8')
    if not flag_select_beginner and not flag_select_master and not flag_select_professional:
        list_statistic = [['beginner', '0', '0', '0', '0', '0'],
                          ['master', '0', '0', '0', '0', '0'],
                          ['professional', '0', '0', '0', '0', '0']]
    elif flag_select_beginner and not flag_select_master and not flag_select_professional:
        list_statistic[0] = ['beginner', '0', '0', '0', '0', '0']
    elif not flag_select_beginner and flag_select_master and not flag_select_professional:
        list_statistic[1] = ['master', '0', '0', '0', '0', '0']
    elif not flag_select_beginner and not flag_select_master and flag_select_professional:
        list_statistic[2] = ['professional', '0', '0', '0', '0', '0']
    for i in list_statistic:
        print(*i, file=my_file)
    flag_select_beginner = False
    flag_select_master = False
    flag_select_professional = False
    my_file.close()


def work():
    global flag_sound, flag_selection_menu, difficulty_level, flag_statistics
    global list_my_ship, list_enemy_ships, list_ban_cell, list_probability_ship, list_battleship, list_chek
    global flag_battleship, flag_cruiser_1, flag_cruiser_2, flag_destroyer_1, flag_destroyer_2, flag_destroyer_3
    global flag_boat_1, flag_boat_2, flag_boat_3, flag_boat_4
    global flag_my_shot, flag_enemy_shot, flag_sound, flag_game, flag_my_victory, flag_automatic
    global list_enemy_battleship, list_enemy_cruiser_1, list_enemy_cruiser_2, list_enemy_destroyer_1, \
        list_enemy_destroyer_2, list_enemy_destroyer_3, list_enemy_boat_1, \
        list_enemy_boat_2, list_enemy_boat_3, list_enemy_boat_4, \
        list_killed_enemy_ships, list_injured_enemy_ships, list_my_shot
    global list_my_battleship, list_my_cruiser_1, list_my_cruiser_2, list_my_destroyer_1, \
        list_my_destroyer_2, list_my_destroyer_3, list_my_boat_1, list_my_boat_2, list_my_boat_3, list_my_boat_4, \
        list_killed_my_ships, list_injured_my_ships, list_enemy_shot, flag_strategy_0, flag_strategy_1, \
        flag_strategy_2, flag_strategy_3, flag_strategy_4
    global flag_clear_field, flag_delete_ship, flag_advantage
    global flag_del_battleship, flag_del_cruiser_1, flag_del_cruiser_2, flag_del_destroyer_1, flag_del_destroyer_2, \
        flag_del_destroyer_3, flag_del_boat_1, flag_del_boat_2, flag_del_boat_3, flag_del_boat_4
    global flag_my_victory, flag_enemy_victory, number_moves, number_whole_ships
    global flag_select_beginner, flag_select_master, flag_select_professional
    global screen_1_music, flag_my_shot_injured, handicap_beginner
    global flag_local_battleship, flag_local_cruiser_1, flag_local_cruiser_2, flag_local_destroyer_1, \
        flag_local_destroyer_2, flag_local_destroyer_3, flag_local_boat_1,\
        flag_local_boat_2, flag_local_boat_3, flag_local_boat_4
    pygame.init()
    pygame.display.set_caption(' МОРСКОЙ БОЙ ')
    screen = pygame.display.set_mode((1115, 750))
    screen_music = pygame.mixer.Sound('music/rekviem.mp3')
    screen_music.set_volume(1.0)
    screen_music.play(-1)
    screen_music_1 = ''
    pygame.display.set_icon(pygame.image.load('picture/sea_battle.png'))
    pygame.mixer.music.load('music/click.mp3')
    pygame.Surface.fill(screen, (255, 250, 250))
    frame(screen)
    notebook_sheet(screen)
    smail_def = pygame.image.load('picture/korabl.png')
    screen.blit(smail_def, (0, 200))
    smail_def = pygame.image.load('picture/уровень.png')
    screen.blit(smail_def, (600, 200))
    button(screen)
    pygame.Surface.fill(screen, (230, 230, 250), (632, 570, 363, 62))
    smail_def = pygame.image.load('picture/дальше.png')
    screen.blit(smail_def, (632, 570))
    pygame.display.update()
    flag_selection_menu = True
    flag_main_menu = False  # меню расстановки кораблей
    flag_choice_battleship = False  # флаг выбора места установки линкора
    flag_choice_cruiser_1 = False  # флаг выбора места установки крейсера_1
    flag_choice_cruiser_2 = False  # флаг выбора места установки крейсера_2
    flag_choice_destroyer_1 = False  # флаг выбора места установки эсминца_1
    flag_choice_destroyer_2 = False  # флаг выбора места установки эсминца_2
    flag_choice_destroyer_3 = False  # флаг выбора места установки эсминца_3
    flag_choice_boat_1 = False  # флаг выбора места установки катера_1
    flag_choice_boat_2 = False  # флаг выбора места установки катера_2
    flag_choice_boat_3 = False  # флаг выбора места установки катера_3
    flag_choice_boat_4 = False  # флаг выбора места установки катера_4
    flag_quit = False
    flag_input = False
    f1 = pygame.font.Font(None, 62)
    text_data = ''
    cell_number = 0
    salute = 0
    salute_2 = 0
    bomba = 0
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos_mouse = event.pos
                    if 965 <= pos_mouse[0] <= 1065 and 50 <= pos_mouse[1] <= 135:
                        """вкл/откл звука"""
                        sound(screen)
                        if not flag_sound:
                            screen_music.set_volume(0.0)
                        elif flag_sound:
                            screen_music.set_volume(1.0)
                        if not flag_sound and type(screen_music_1) != str:
                            screen_music_1.set_volume(0.0)
                        elif flag_sound and type(screen_music_1) != str:
                            screen_music_1.set_volume(1.0)
                    elif 632 <= pos_mouse[0] <= 995 and 270 <= pos_mouse[1] <= 332\
                            and flag_selection_menu and not flag_advantage:
                        """кнопка новичок"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        difficulty_level = choice_difficulty_level(screen, 1)
                    elif 632 <= pos_mouse[0] <= 995 and 360 <= pos_mouse[1] <= 422\
                            and flag_selection_menu and not flag_advantage:
                        """кнопка мастер"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        difficulty_level = choice_difficulty_level(screen, 2)
                    elif 632 <= pos_mouse[0] <= 995 and 450 <= pos_mouse[1] <= 512\
                            and flag_selection_menu and not flag_advantage:
                        """кнопка профессионал"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        difficulty_level = choice_difficulty_level(screen, 3)
                    elif 632 <= pos_mouse[0] <= 995 and 570 <= pos_mouse[1] <= 632 and difficulty_level is not None \
                            and flag_selection_menu and not flag_advantage:
                        """кнопка дальше"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (632, 570, 362, 62))
                        pygame.Surface.fill(screen, (230, 230, 250), (650, 583, 327, 36))
                        smail_def = pygame.image.load('picture/дальше.png')
                        screen.blit(smail_def, (632, 570))
                        pygame.display.update((632, 570, 363, 62))
                        pygame.time.wait(150)
                        pygame.Surface.fill(screen, (255, 250, 250), (33, 200, 1050, 490))
                        notebook_sheet(screen)
                        if difficulty_level == 'beginner' and not flag_advantage:
                            flag_advantage = True
                            smail_def = pygame.image.load('picture/преимущество.png')
                            screen.blit(smail_def, (260, 260))
                            input_box = pygame.Rect(480, 435, 151, 60)
                            pygame.draw.rect(screen, (80, 123, 175), input_box, 5)
                            pygame.Surface.fill(screen, (230, 230, 250), (599, 576, 274, 51))
                            smail_def = pygame.image.load('picture/дальше_2.png')
                            screen.blit(smail_def, (599, 576))
                            pygame.Surface.fill(screen, (230, 230, 250), (239, 576, 274, 51))
                            smail_def = pygame.image.load('picture/назад.png')
                            screen.blit(smail_def, (239, 576))
                            smail_def = pygame.image.load('picture/корабль.png')
                            screen.blit(smail_def, (60, 290))
                            smail_def = pygame.image.load('picture/самолет.png')
                            screen.blit(smail_def, (750, 350))
                        else:
                            flag_selection_menu = False
                            flag_main_menu = True
                            flag_clear_field = True
                            smail_def = pygame.image.load('picture/мой флот.png')
                            screen.blit(smail_def, (165, 200))
                            smail_def = pygame.image.load('picture/расставить корабли.png')
                            screen.blit(smail_def, (540, 200))
                            grid(screen, 120, 421, 300, 601)
                            placement_ships(screen)
                            pygame.Surface.fill(screen, (230, 230, 250), (90, 636, 274, 51))
                            smail_def = pygame.image.load('picture/расставить.png')
                            screen.blit(smail_def, (90, 636))
                            pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 274, 51))
                            smail_def = pygame.image.load('picture/очистить.png')
                            screen.blit(smail_def, (420, 636))
                            pygame.Surface.fill(screen, (230, 230, 250), (750, 636, 274, 51))
                            smail_def = pygame.image.load('picture/дальше_2.png')
                            screen.blit(smail_def, (750, 636))
                        pygame.display.update((30, 200, 1055, 490))
                    elif 480 <= pos_mouse[0] <= 630 and 435 <= pos_mouse[1] <= 495 and flag_selection_menu\
                            and difficulty_level == 'beginner' and flag_advantage:
                        """активация прямоугольника ввода в меню ввода преимущества"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (255, 250, 250), (480, 435, 151, 60))
                        notebook_sheet(screen)
                        input_box = pygame.Rect(480, 435, 151, 60)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 5)
                        pygame.display.update((480, 435, 151, 60))
                        flag_input = True
                    elif 239 <= pos_mouse[0] <= 513 and 576 <= pos_mouse[1] <= 627 and flag_selection_menu\
                            and difficulty_level == 'beginner' and flag_advantage:
                        """кнопка назад в меню ввода преимущества"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (240, 576, 272, 50))
                        pygame.Surface.fill(screen, (230, 230, 250), (260, 586, 230, 30))
                        smail_def = pygame.image.load('picture/назад.png')
                        screen.blit(smail_def, (239, 576))
                        pygame.display.update((240, 576, 272, 50))
                        pygame.time.wait(150)
                        pygame.Surface.fill(screen, (255, 250, 250))
                        frame(screen)
                        notebook_sheet(screen)
                        smail_def = pygame.image.load('picture/korabl.png')
                        screen.blit(smail_def, (0, 200))
                        smail_def = pygame.image.load('picture/уровень.png')
                        screen.blit(smail_def, (600, 200))
                        button(screen)
                        pygame.Surface.fill(screen, (230, 230, 250), (632, 570, 363, 62))
                        smail_def = pygame.image.load('picture/дальше.png')
                        screen.blit(smail_def, (632, 570))
                        if not flag_sound:
                            pygame.draw.line(screen, (255, 0, 0), (975, 60), (1055, 125), 6)
                            pygame.draw.line(screen, (255, 0, 0), (1055, 60), (975, 125), 6)
                        pygame.display.update()
                        flag_advantage = False
                        handicap_beginner = 22  # фора для новичка
                        text_data = ''
                        difficulty_level = None  # уровень сложности игры
                    elif 599 <= pos_mouse[0] <= 873 and 576 <= pos_mouse[1] <= 627 and flag_selection_menu\
                            and difficulty_level == 'beginner' and 0 <= handicap_beginner <= 10 and flag_advantage:
                        """кнопка дальше в меню ввода преимущества"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (599, 576, 274, 51))
                        pygame.Surface.fill(screen, (230, 230, 250), (615, 586, 243, 30))
                        smail_def = pygame.image.load('picture/дальше_2.png')
                        screen.blit(smail_def, (599, 576))
                        pygame.display.update((599, 576, 274, 51))
                        pygame.time.wait(150)
                        flag_selection_menu = False
                        flag_main_menu = True
                        flag_clear_field = True
                        flag_advantage = False
                        pygame.Surface.fill(screen, (255, 250, 250), (33, 200, 1050, 490))
                        notebook_sheet(screen)
                        smail_def = pygame.image.load('picture/мой флот.png')
                        screen.blit(smail_def, (165, 200))
                        smail_def = pygame.image.load('picture/расставить корабли.png')
                        screen.blit(smail_def, (540, 200))
                        grid(screen, 120, 421, 300, 601)
                        placement_ships(screen)
                        pygame.Surface.fill(screen, (230, 230, 250), (90, 636, 274, 51))
                        smail_def = pygame.image.load('picture/расставить.png')
                        screen.blit(smail_def, (90, 636))
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 274, 51))
                        smail_def = pygame.image.load('picture/очистить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.Surface.fill(screen, (230, 230, 250), (750, 636, 274, 51))
                        smail_def = pygame.image.load('picture/дальше_2.png')
                        screen.blit(smail_def, (750, 636))
                        pygame.display.update((30, 200, 1055, 490))
                    elif 90 <= pos_mouse[0] <= 364 and 636 <= pos_mouse[1] <= 686 and flag_main_menu:
                        """кнопка расставить"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (90, 637, 273, 49))
                        pygame.Surface.fill(screen, (230, 230, 250), (105, 645, 245, 32))
                        smail_def = pygame.image.load('picture/расставить.png')
                        screen.blit(smail_def, (90, 636))
                        pygame.display.update((90, 636, 274, 52))
                        pygame.time.wait(150)
                        list_my_ship = []  # список моих кораблей
                        list_ban_cell = []  # список запрещенных клеток для установки корабля
                        list_battleship = []  # список координат установки линкора
                        list_probability_ship = []  # список вариатов установки корабля
                        list_my_battleship = []  # координаты моего линкора
                        list_my_cruiser_1 = []  # координаты моего крейсера_1
                        list_my_cruiser_2 = []  # координаты моего крейсера_2
                        list_my_destroyer_1 = []  # координаты моего эсминца_1
                        list_my_destroyer_2 = []  # координаты моего эсминца_2
                        list_my_destroyer_3 = []  # координаты моего эсминца_3
                        list_my_boat_1 = []  # координаты моего катера_1
                        list_my_boat_2 = []  # координаты моего катера_2
                        list_my_boat_3 = []  # координаты моего катера_3
                        list_my_boat_4 = []  # координаты моего катера_4
                        flag_battleship = False  # установлен ли линкор : True - да , False - нет
                        flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
                        flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
                        flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
                        flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
                        flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
                        flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
                        flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
                        flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
                        flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                        flag_quit = False
                        flag_automatic = True
                        flag_clear_field = True
                        flag_delete_ship = False
                        cell_number = 0
                        list_chek = []
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        delete_ship(screen, flag_clear_field, flag_delete_ship)
                        automatic_placement_ships(screen)
                    elif 423 <= pos_mouse[0] <= 692 and 636 <= pos_mouse[1] <= 686 and flag_main_menu:
                        """кнопка удалить / очистить"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (420, 636, 270, 50))
                        pygame.Surface.fill(screen, (230, 230, 250), (435, 645, 245, 32))
                        if flag_clear_field and not flag_delete_ship:
                            smail_def = pygame.image.load('picture/очистить.png')
                        elif not flag_clear_field and flag_delete_ship:
                            smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        pygame.time.wait(150)
                        if flag_clear_field and not flag_delete_ship:
                            list_my_ship = []  # список моих кораблей
                            list_ban_cell = []  # список запрещенных клеток для установки корабля
                            list_battleship = []  # список координат установки линкора
                            list_probability_ship = []  # список вариатов установки корабля
                            list_my_battleship = []  # координаты моего линкора
                            list_my_cruiser_1 = []  # координаты моего крейсера_1
                            list_my_cruiser_2 = []  # координаты моего крейсера_2
                            list_my_destroyer_1 = []  # координаты моего эсминца_1
                            list_my_destroyer_2 = []  # координаты моего эсминца_2
                            list_my_destroyer_3 = []  # координаты моего эсминца_3
                            list_my_boat_1 = []  # координаты моего катера_1
                            list_my_boat_2 = []  # координаты моего катера_2
                            list_my_boat_3 = []  # координаты моего катера_3
                            list_my_boat_4 = []  # координаты моего катера_4
                            flag_battleship = False  # установлен ли линкор : True - да , False - нет
                            flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
                            flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
                            flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
                            flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
                            flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
                            flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
                            flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
                            flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
                            flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
                            flag_choice_battleship = False
                            flag_choice_cruiser_1 = False
                            flag_choice_cruiser_2 = False
                            flag_choice_destroyer_1 = False
                            flag_choice_destroyer_2 = False
                            flag_choice_destroyer_3 = False
                            flag_choice_boat_1 = False
                            flag_choice_boat_2 = False
                            flag_choice_boat_3 = False
                            flag_choice_boat_4 = False
                            flag_quit = False
                            flag_automatic = False
                            flag_clear_field = True
                            flag_delete_ship = False
                            cell_number = 0
                            list_chek = []
                            flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                            flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                            flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                            flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                            flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                            flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                            flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                            flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                            flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                            flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                            delete_ship(screen, flag_clear_field, flag_delete_ship)
                        elif not flag_clear_field and flag_delete_ship:
                            del_choice_ship(screen)
                    elif (750 <= pos_mouse[0] <= 1020 and 636 <= pos_mouse[1] <= 686 and flag_main_menu
                          and len(list_my_ship) == 20 and flag_battleship and flag_cruiser_1 and flag_cruiser_2
                          and flag_destroyer_1 and flag_destroyer_2 and flag_destroyer_3 and flag_boat_1
                          and flag_boat_2 and flag_boat_3 and flag_boat_4):
                        """кнопка дальше"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (750, 636, 270, 50))
                        pygame.Surface.fill(screen, (230, 230, 250), (765, 645, 245, 32))
                        smail_def = pygame.image.load('picture/дальше_2.png')
                        screen.blit(smail_def, (750, 636))
                        pygame.display.update((750, 636, 270, 50))
                        pygame.time.wait(150)
                        list_enemy_ships = []
                        list_ban_cell = []
                        list_battleship = []
                        list_probability_ship = []
                        automatic_placement_enemy_ships()
                        flag_main_menu = False
                        flag_game = True
                        flag_my_shot = True
                        flag_enemy_shot = False
                        flag_quit = False
                        cell_number = 0
                        pygame.mixer.music.load('music/shot.mp3')
                        pygame.Surface.fill(screen, (255, 250, 250), (33, 200, 1050, 490))
                        notebook_sheet(screen)
                        smail_def = pygame.image.load('picture/мой флот.png')
                        screen.blit(smail_def, (165, 200))
                        smail_def = pygame.image.load('picture/вражеский флот.png')
                        screen.blit(smail_def, (515, 200))
                        smail_def = pygame.image.load('picture/количество ходов.png')
                        screen.blit(smail_def, (87, 617))
                        smail_def = pygame.image.load('picture/количество ходов.png')
                        screen.blit(smail_def, (507, 617))
                        number_shots_remaining(screen)
                        grid(screen, 120, 421, 300, 601)
                        for i in list_my_ship:
                            x_start = cell[i][0]
                            y_start = cell[i][1]
                            pygame.Surface.fill(screen, (176, 224, 230), rect=(x_start, y_start, 30, 30))
                            pygame.draw.rect(screen, (25, 25, 112), (x_start, y_start, 32, 32), 4)
                        grid(screen, 540, 841, 300, 601)
                        pygame.Surface.fill(screen, (230, 230, 250), (900, 425, 183, 50))
                        smail_def = pygame.image.load('picture/сдаюсь.png')
                        screen.blit(smail_def, (900, 425))
                        smail_def = pygame.image.load('picture/под.лодка.png')
                        screen.blit(smail_def, (870, 260))
                        smail_def = pygame.image.load('picture/korabl-8.png')
                        screen.blit(smail_def, (870, 500))
                        pygame.display.update((33, 200, 1050, 490))
                        screen_music.stop()
                        screen_music = pygame.mixer.Sound('music/shtorm.mp3')
                        if flag_sound:
                            screen_music.set_volume(1.0)
                        elif not flag_sound:
                            screen_music.set_volume(0.0)
                        screen_music.play(-1)
                    elif 900 <= pos_mouse[0] <= 1083 and 425 <= pos_mouse[1] <= 475 and flag_game:
                        """кнопка сдаться"""
                        pygame.mixer.music.load('music/click.mp3')
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (900, 425, 182, 50))
                        pygame.Surface.fill(screen, (230, 230, 250), (915, 435, 154, 30))
                        smail_def = pygame.image.load('picture/сдаюсь.png')
                        screen.blit(smail_def, (900, 425))
                        pygame.display.update((900, 425, 183, 50))
                        pygame.time.wait(100)
                        pygame.Surface.fill(screen, (230, 230, 250), (900, 425, 182, 50))
                        smail_def = pygame.image.load('picture/сдаюсь.png')
                        screen.blit(smail_def, (900, 425))
                        pygame.display.update((900, 425, 183, 50))
                        flag_game = False
                        flag_my_victory = False
                        flag_enemy_victory = True
                        write_statistics()
                        screen_music.stop()
                        screen_music = pygame.mixer.Sound('music/поражение.mp3')
                        if flag_sound:
                            screen_music.set_volume(1.0)
                        elif not flag_sound:
                            screen_music.set_volume(0.0)
                        screen_music.play(-1)
                    elif 749 <= pos_mouse[0] <= 1082 and 360 <= pos_mouse[1] <= 422 and flag_quit:
                        """кнопка новая игра"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (749, 360, 333, 62))
                        pygame.Surface.fill(screen, (230, 230, 250), (765, 371, 301, 40))
                        smail_def = pygame.image.load('picture/новая игра.png')
                        screen.blit(smail_def, (749, 360))
                        pygame.display.update((749, 360, 333, 62))
                        pygame.time.wait(100)
                        flag_selection_menu = True
                        flag_main_menu = False
                        flag_statistics = False
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                        flag_quit = False
                        flag_strategy_0 = False  # стратегия стрельбы 0
                        flag_strategy_1 = False  # стратегия стрельбы 1
                        flag_strategy_2 = False  # стратегия стрельбы 2
                        flag_strategy_3 = False  # стратегия стрельбы 3
                        flag_strategy_4 = False  # стратегия стрельбы 4
                        cell_number = 0
                        list_my_ship = []  # список моих кораблей
                        list_ban_cell = []  # список запрещенных клеток для установки корабля
                        list_battleship = []  # список координат установки корабля
                        list_probability_ship = []  # список вариатов установки корабля
                        list_enemy_ships = []  # список вражеских кораблей
                        list_enemy_battleship = []  # координаты вражеского линкора
                        list_enemy_cruiser_1 = []  # координаты вражеского крейсера_1
                        list_enemy_cruiser_2 = []  # координаты вражеского крейсера_2
                        list_enemy_destroyer_1 = []  # координаты вражеского эсминца_1
                        list_enemy_destroyer_2 = []  # координаты вражеского эсминца_2
                        list_enemy_destroyer_3 = []  # координаты вражеского эсминца_3
                        list_enemy_boat_1 = []  # координаты вражеского катера_1
                        list_enemy_boat_2 = []  # координаты вражеского катера_2
                        list_enemy_boat_3 = []  # координаты вражеского катера_3
                        list_enemy_boat_4 = []  # координаты вражеского катера_4
                        list_killed_enemy_ships = []  # список вражеских убитых кораблей
                        list_injured_enemy_ships = []  # список раненых вражеских кораблей
                        list_my_shot = []  # список моих выстрелов
                        list_my_ship = []  # список моих кораблей
                        list_my_battleship = []  # координаты моего линкора
                        list_my_cruiser_1 = []  # координаты моего крейсера_1
                        list_my_cruiser_2 = []  # координаты моего крейсера_2
                        list_my_destroyer_1 = []  # координаты моего эсминца_1
                        list_my_destroyer_2 = []  # координаты моего эсминца_2
                        list_my_destroyer_3 = []  # координаты моего эсминца_3
                        list_my_boat_1 = []  # координаты моего катера_1
                        list_my_boat_2 = []  # координаты моего катера_2
                        list_my_boat_3 = []  # координаты моего катера_3
                        list_my_boat_4 = []  # координаты моего катера_4
                        list_killed_my_ships = []  # список моих убитых кораблей
                        list_injured_my_ships = []  # список моих раненых кораблей
                        list_enemy_shot = []
                        list_chek = []
                        flag_battleship = False  # установлен ли линкор : True - да , False - нет
                        flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
                        flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
                        flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
                        flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
                        flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
                        flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
                        flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
                        flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
                        flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
                        flag_my_shot = False  # мой выстрел
                        flag_enemy_shot = False  # вражеский выстрел
                        flag_game = False  # игра
                        flag_my_victory = False  # я победил
                        flag_enemy_victory = False
                        flag_automatic = False
                        flag_my_shot_injured = False
                        number_moves = 0
                        number_whole_ships = 10
                        flag_select_beginner = False  # выбор строки новичок
                        flag_select_master = False  # выбор строки мастер
                        flag_select_professional = False  # выбор строки профессионал
                        flag_local_battleship = True
                        flag_local_cruiser_1 = True
                        flag_local_cruiser_2 = True
                        flag_local_destroyer_1 = True
                        flag_local_destroyer_2 = True
                        flag_local_destroyer_3 = True
                        flag_local_boat_1 = True
                        flag_local_boat_2 = True
                        flag_local_boat_3 = True
                        flag_local_boat_4 = True
                        difficulty_level = None  # уровень сложности игры
                        handicap_beginner = 22  # фора для новичка
                        text_data = ''
                        pygame.Surface.fill(screen, (255, 250, 250))
                        frame(screen)
                        notebook_sheet(screen)
                        smail_def = pygame.image.load('picture/korabl.png')
                        screen.blit(smail_def, (0, 200))
                        smail_def = pygame.image.load('picture/уровень.png')
                        screen.blit(smail_def, (600, 200))
                        button(screen)
                        pygame.Surface.fill(screen, (230, 230, 250), (632, 570, 363, 62))
                        smail_def = pygame.image.load('picture/дальше.png')
                        screen.blit(smail_def, (632, 570))
                        screen_music.stop()
                        screen_music_1.stop()
                        screen_music = pygame.mixer.Sound('music/rekviem.mp3')
                        if flag_sound:
                            screen_music.set_volume(1.0)
                        elif not flag_sound:
                            pygame.draw.line(screen, (255, 0, 0), (975, 60), (1055, 125), 6)
                            pygame.draw.line(screen, (255, 0, 0), (1055, 60), (975, 125), 6)
                            screen_music.set_volume(0.0)
                        screen_music.play(-1)
                        pygame.display.update()
                    elif (749 <= pos_mouse[0] <= 1082 and 480 <= pos_mouse[1] <= 542 and flag_quit)\
                            or (750 <= pos_mouse[0] <= 1024 and 606 <= pos_mouse[1] <= 657 and flag_statistics):
                        """кнопка выход"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_quit:
                            pygame.Surface.fill(screen, (0, 0, 128), (749, 480, 333, 62))
                            pygame.Surface.fill(screen, (230, 230, 250), (765, 491, 301, 40))
                            smail_def = pygame.image.load('picture/выход.png')
                            screen.blit(smail_def, (749, 480))
                            pygame.display.update((749, 480, 333, 62))
                        elif flag_statistics:
                            pygame.Surface.fill(screen, (0, 0, 128), (750, 606, 274, 51))
                            pygame.Surface.fill(screen, (230, 230, 250), (770, 616, 232, 30))
                            smail_def = pygame.image.load('picture/выход_2.png')
                            screen.blit(smail_def, (750, 606))
                            pygame.display.update((750, 606, 274, 51))
                        pygame.time.wait(150)
                        pygame.quit()
                        sys.exit()
                    elif 749 <= pos_mouse[0] <= 1082 and 240 <= pos_mouse[1] <= 302 and flag_quit:
                        """кнопка статистика"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (749, 240, 333, 62))
                        pygame.Surface.fill(screen, (230, 230, 250), (765, 251, 301, 40))
                        smail_def = pygame.image.load('picture/статистика.png')
                        screen.blit(smail_def, (749, 240))
                        pygame.display.update((749, 240, 333, 62))
                        pygame.time.wait(150)
                        flag_quit = False
                        flag_statistics = True
                        print_statistics(screen)
                        screen_music_1.stop()
                    elif 90 <= pos_mouse[0] <= 364 and 606 <= pos_mouse[1] <= 657 and flag_statistics:
                        """кнопка назад"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (90, 607, 274, 49))
                        pygame.Surface.fill(screen, (230, 230, 250), (110, 616, 232, 30))
                        smail_def = pygame.image.load('picture/назад.png')
                        screen.blit(smail_def, (90, 606))
                        pygame.display.update((90, 606, 274, 51))
                        flag_statistics = False
                    elif 810 <= pos_mouse[0] <= 1021 and 600 <= pos_mouse[1] <= 662 and flag_quit:
                        """кнопка файл"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (810, 600, 211, 62))
                        pygame.Surface.fill(screen, (230, 230, 250), (832, 612, 167, 38))
                        smail_def = pygame.image.load('picture/файл.png')
                        screen.blit(smail_def, (810, 600))
                        pygame.display.update((810, 600, 211, 62))
                        pygame.time.wait(150)
                        pygame.Surface.fill(screen, (230, 230, 250), (810, 600, 211, 62))
                        smail_def = pygame.image.load('picture/файл.png')
                        screen.blit(smail_def, (810, 600))
                        pygame.display.update((810, 600, 211, 62))
                        os.startfile('description.txt')
                    elif 90 <= pos_mouse[0] <= 235 and 322 <= pos_mouse[1] <= 368 and flag_statistics:
                        """строка новичок"""
                        flag_select_beginner = True  # выбор строки новичок
                        flag_select_master = False
                        flag_select_professional = False
                        print_statistics(screen)
                    elif 90 <= pos_mouse[0] <= 235 and 412 <= pos_mouse[1] <= 458 and flag_statistics:
                        """строка мастер"""
                        flag_select_master = True  # выбор строки мастер
                        flag_select_beginner = False
                        flag_select_professional = False
                        print_statistics(screen)
                    elif 30 <= pos_mouse[0] <= 291 and 502 <= pos_mouse[1] <= 548 and flag_statistics:
                        """строка профессионал"""
                        flag_select_professional = True  # выбор строки профессионал
                        flag_select_beginner = False
                        flag_select_master = False
                        print_statistics(screen)
                    elif 420 <= pos_mouse[0] <= 694 and 606 <= pos_mouse[1] <= 657 and flag_statistics:
                        """кнопка очистить"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (0, 0, 128), (420, 607, 273, 49))
                        pygame.Surface.fill(screen, (230, 230, 250), (435, 616, 246, 30))
                        smail_def = pygame.image.load('picture/очистить.png')
                        screen.blit(smail_def, (420, 606))
                        pygame.display.update((420, 606, 274, 51))
                        pygame.time.wait(150)
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 606, 274, 50))
                        smail_def = pygame.image.load('picture/очистить.png')
                        screen.blit(smail_def, (420, 606))
                        pygame.display.update((420, 606, 274, 51))
                        clear_statistics()
                        print_statistics(screen)
                    elif 480 <= pos_mouse[0] <= 750 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        """выбор установки линкора"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_battleship:
                            flag_choice_battleship = True
                        flag_del_battleship = True  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(470, 290, 320, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((470, 290, 320, 50))
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 480 <= pos_mouse[0] <= 750 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        """выбор установки крейсера 1"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_cruiser_1:
                            flag_choice_cruiser_1 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = True  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(470, 350, 320, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((470, 350, 320, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 480 <= pos_mouse[0] <= 750 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        """выбор установки крейсера 2"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_cruiser_2:
                            flag_choice_cruiser_2 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = True  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(470, 410, 320, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((470, 410, 320, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 480 <= pos_mouse[0] <= 750 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        """выбор установки эсминца 1"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_destroyer_1:
                            flag_choice_destroyer_1 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = True  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(470, 470, 320, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((470, 470, 320, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 480 <= pos_mouse[0] <= 750 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        """выбор установки эсминца 2"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_destroyer_2:
                            flag_choice_destroyer_2 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = True  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(470, 530, 320, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((470, 530, 320, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 800 <= pos_mouse[0] <= 1090 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        """выбор установки эсминца 3"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_destroyer_3:
                            flag_choice_destroyer_3 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = True  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(800, 290, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((800, 290, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 800 <= pos_mouse[0] <= 1090 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        """выбор установки катера 1"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_boat_1:
                            flag_choice_boat_1 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = True  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(800, 350, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((800, 350, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 800 <= pos_mouse[0] <= 1090 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        """выбор установки катера 2"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_boat_2:
                            flag_choice_boat_2 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = True  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(800, 410, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((800, 410, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_3 = False
                        flag_choice_boat_4 = False
                    elif 800 <= pos_mouse[0] <= 1090 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        """выбор установки катера 3"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_boat_3:
                            flag_choice_boat_3 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = True  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(800, 470, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((800, 470, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_4 = False
                    elif 800 <= pos_mouse[0] <= 1090 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        """выбор установки катера 4"""
                        if flag_sound:
                            pygame.mixer.music.play()
                        if flag_clear_field:
                            flag_clear_field = False
                        flag_delete_ship = True
                        pygame.Surface.fill(screen, (230, 230, 250), (420, 636, 270, 50))
                        smail_def = pygame.image.load('picture/удалить.png')
                        screen.blit(smail_def, (420, 636))
                        pygame.display.update((420, 636, 270, 50))
                        cell_number = 0
                        if len(list_battleship) == 0 and not flag_boat_4:
                            flag_choice_boat_4 = True
                        flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
                        flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
                        flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
                        flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
                        flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
                        flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
                        flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
                        flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
                        flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
                        flag_del_boat_4 = True  # флаг удаления катера_4 : True - да , False - нет
                        grout(screen)
                        input_box = pygame.Rect(800, 530, 290, 50)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 2)
                        pygame.display.update((800, 530, 290, 50))
                        flag_choice_battleship = False
                        flag_choice_cruiser_1 = False
                        flag_choice_cruiser_2 = False
                        flag_choice_destroyer_1 = False
                        flag_choice_destroyer_2 = False
                        flag_choice_destroyer_3 = False
                        flag_choice_boat_1 = False
                        flag_choice_boat_2 = False
                        flag_choice_boat_3 = False
                    elif 120 <= pos_mouse[0] <= 150 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 1
                    elif 150 <= pos_mouse[0] <= 180 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 2
                    elif 180 <= pos_mouse[0] <= 210 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 3
                    elif 210 <= pos_mouse[0] <= 240 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 4
                    elif 240 <= pos_mouse[0] <= 270 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 5
                    elif 270 <= pos_mouse[0] <= 300 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 6
                    elif 300 <= pos_mouse[0] <= 330 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 7
                    elif 330 <= pos_mouse[0] <= 360 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 8
                    elif 360 <= pos_mouse[0] <= 390 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 9
                    elif 390 <= pos_mouse[0] <= 420 and 300 <= pos_mouse[1] <= 330 and flag_main_menu:
                        cell_number = 10
                    elif 120 <= pos_mouse[0] <= 150 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 11
                    elif 150 <= pos_mouse[0] <= 180 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 12
                    elif 180 <= pos_mouse[0] <= 210 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 13
                    elif 210 <= pos_mouse[0] <= 240 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 14
                    elif 240 <= pos_mouse[0] <= 270 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 15
                    elif 270 <= pos_mouse[0] <= 300 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 16
                    elif 300 <= pos_mouse[0] <= 330 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 17
                    elif 330 <= pos_mouse[0] <= 360 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 18
                    elif 360 <= pos_mouse[0] <= 390 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 19
                    elif 390 <= pos_mouse[0] <= 420 and 330 <= pos_mouse[1] <= 360 and flag_main_menu:
                        cell_number = 20
                    elif 120 <= pos_mouse[0] <= 150 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 21
                    elif 150 <= pos_mouse[0] <= 180 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 22
                    elif 180 <= pos_mouse[0] <= 210 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 23
                    elif 210 <= pos_mouse[0] <= 240 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 24
                    elif 240 <= pos_mouse[0] <= 270 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 25
                    elif 270 <= pos_mouse[0] <= 300 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 26
                    elif 300 <= pos_mouse[0] <= 330 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 27
                    elif 330 <= pos_mouse[0] <= 360 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 28
                    elif 360 <= pos_mouse[0] <= 390 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 29
                    elif 390 <= pos_mouse[0] <= 420 and 360 <= pos_mouse[1] <= 390 and flag_main_menu:
                        cell_number = 30
                    elif 120 <= pos_mouse[0] <= 150 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 31
                    elif 150 <= pos_mouse[0] <= 180 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 32
                    elif 180 <= pos_mouse[0] <= 210 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 33
                    elif 210 <= pos_mouse[0] <= 240 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 34
                    elif 240 <= pos_mouse[0] <= 270 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 35
                    elif 270 <= pos_mouse[0] <= 300 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 36
                    elif 300 <= pos_mouse[0] <= 330 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 37
                    elif 330 <= pos_mouse[0] <= 360 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 38
                    elif 360 <= pos_mouse[0] <= 390 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 39
                    elif 390 <= pos_mouse[0] <= 420 and 390 <= pos_mouse[1] <= 420 and flag_main_menu:
                        cell_number = 40
                    elif 120 <= pos_mouse[0] <= 150 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 41
                    elif 150 <= pos_mouse[0] <= 180 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 42
                    elif 180 <= pos_mouse[0] <= 210 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 43
                    elif 210 <= pos_mouse[0] <= 240 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 44
                    elif 240 <= pos_mouse[0] <= 270 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 45
                    elif 270 <= pos_mouse[0] <= 300 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 46
                    elif 300 <= pos_mouse[0] <= 330 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 47
                    elif 330 <= pos_mouse[0] <= 360 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 48
                    elif 360 <= pos_mouse[0] <= 390 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 49
                    elif 390 <= pos_mouse[0] <= 420 and 420 <= pos_mouse[1] <= 450 and flag_main_menu:
                        cell_number = 50
                    elif 120 <= pos_mouse[0] <= 150 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 51
                    elif 150 <= pos_mouse[0] <= 180 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 52
                    elif 180 <= pos_mouse[0] <= 210 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 53
                    elif 210 <= pos_mouse[0] <= 240 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 54
                    elif 240 <= pos_mouse[0] <= 270 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 55
                    elif 270 <= pos_mouse[0] <= 300 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 56
                    elif 300 <= pos_mouse[0] <= 330 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 57
                    elif 330 <= pos_mouse[0] <= 360 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 58
                    elif 360 <= pos_mouse[0] <= 390 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 59
                    elif 390 <= pos_mouse[0] <= 420 and 450 <= pos_mouse[1] <= 480 and flag_main_menu:
                        cell_number = 60
                    elif 120 <= pos_mouse[0] <= 150 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 61
                    elif 150 <= pos_mouse[0] <= 180 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 62
                    elif 180 <= pos_mouse[0] <= 210 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 63
                    elif 210 <= pos_mouse[0] <= 240 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 64
                    elif 240 <= pos_mouse[0] <= 270 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 65
                    elif 270 <= pos_mouse[0] <= 300 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 66
                    elif 300 <= pos_mouse[0] <= 330 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 67
                    elif 330 <= pos_mouse[0] <= 360 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 68
                    elif 360 <= pos_mouse[0] <= 390 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 69
                    elif 390 <= pos_mouse[0] <= 420 and 480 <= pos_mouse[1] <= 510 and flag_main_menu:
                        cell_number = 70
                    elif 120 <= pos_mouse[0] <= 150 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 71
                    elif 150 <= pos_mouse[0] <= 180 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 72
                    elif 180 <= pos_mouse[0] <= 210 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 73
                    elif 210 <= pos_mouse[0] <= 240 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 74
                    elif 240 <= pos_mouse[0] <= 270 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 75
                    elif 270 <= pos_mouse[0] <= 300 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 76
                    elif 300 <= pos_mouse[0] <= 330 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 77
                    elif 330 <= pos_mouse[0] <= 360 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 78
                    elif 360 <= pos_mouse[0] <= 390 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 79
                    elif 390 <= pos_mouse[0] <= 420 and 510 <= pos_mouse[1] <= 540 and flag_main_menu:
                        cell_number = 80
                    elif 120 <= pos_mouse[0] <= 150 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 81
                    elif 150 <= pos_mouse[0] <= 180 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 82
                    elif 180 <= pos_mouse[0] <= 210 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 83
                    elif 210 <= pos_mouse[0] <= 240 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 84
                    elif 240 <= pos_mouse[0] <= 270 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 85
                    elif 270 <= pos_mouse[0] <= 300 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 86
                    elif 300 <= pos_mouse[0] <= 330 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 87
                    elif 330 <= pos_mouse[0] <= 360 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 88
                    elif 360 <= pos_mouse[0] <= 390 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 89
                    elif 390 <= pos_mouse[0] <= 420 and 540 <= pos_mouse[1] <= 570 and flag_main_menu:
                        cell_number = 90
                    elif 120 <= pos_mouse[0] <= 150 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 91
                    elif 150 <= pos_mouse[0] <= 180 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 92
                    elif 180 <= pos_mouse[0] <= 210 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 93
                    elif 210 <= pos_mouse[0] <= 240 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 94
                    elif 240 <= pos_mouse[0] <= 270 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 95
                    elif 270 <= pos_mouse[0] <= 300 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 96
                    elif 300 <= pos_mouse[0] <= 330 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 97
                    elif 330 <= pos_mouse[0] <= 360 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 98
                    elif 360 <= pos_mouse[0] <= 390 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 99
                    elif 390 <= pos_mouse[0] <= 420 and 570 <= pos_mouse[1] <= 600 and flag_main_menu:
                        cell_number = 100
                    elif 540 <= pos_mouse[0] <= 570 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 1
                    elif 570 <= pos_mouse[0] <= 600 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 2
                    elif 600 <= pos_mouse[0] <= 630 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 3
                    elif 630 <= pos_mouse[0] <= 660 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 4
                    elif 660 <= pos_mouse[0] <= 690 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 5
                    elif 690 <= pos_mouse[0] <= 720 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 6
                    elif 720 <= pos_mouse[0] <= 750 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 7
                    elif 750 <= pos_mouse[0] <= 780 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 8
                    elif 780 <= pos_mouse[0] <= 810 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 9
                    elif 810 <= pos_mouse[0] <= 840 and 300 <= pos_mouse[1] <= 330 and flag_game and flag_my_shot:
                        cell_number = 10
                    elif 540 <= pos_mouse[0] <= 570 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 11
                    elif 570 <= pos_mouse[0] <= 600 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 12
                    elif 600 <= pos_mouse[0] <= 630 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 13
                    elif 630 <= pos_mouse[0] <= 660 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 14
                    elif 660 <= pos_mouse[0] <= 690 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 15
                    elif 690 <= pos_mouse[0] <= 720 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 16
                    elif 720 <= pos_mouse[0] <= 750 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 17
                    elif 750 <= pos_mouse[0] <= 780 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 18
                    elif 780 <= pos_mouse[0] <= 810 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 19
                    elif 810 <= pos_mouse[0] <= 840 and 330 <= pos_mouse[1] <= 360 and flag_game and flag_my_shot:
                        cell_number = 20
                    elif 540 <= pos_mouse[0] <= 570 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 21
                    elif 570 <= pos_mouse[0] <= 600 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 22
                    elif 600 <= pos_mouse[0] <= 630 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 23
                    elif 630 <= pos_mouse[0] <= 660 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 24
                    elif 660 <= pos_mouse[0] <= 690 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 25
                    elif 690 <= pos_mouse[0] <= 720 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 26
                    elif 720 <= pos_mouse[0] <= 750 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 27
                    elif 750 <= pos_mouse[0] <= 780 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 28
                    elif 780 <= pos_mouse[0] <= 810 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 29
                    elif 810 <= pos_mouse[0] <= 840 and 360 <= pos_mouse[1] <= 390 and flag_game and flag_my_shot:
                        cell_number = 30
                    elif 540 <= pos_mouse[0] <= 570 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 31
                    elif 570 <= pos_mouse[0] <= 600 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 32
                    elif 600 <= pos_mouse[0] <= 630 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 33
                    elif 630 <= pos_mouse[0] <= 660 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 34
                    elif 660 <= pos_mouse[0] <= 690 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 35
                    elif 690 <= pos_mouse[0] <= 720 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 36
                    elif 720 <= pos_mouse[0] <= 750 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 37
                    elif 750 <= pos_mouse[0] <= 780 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 38
                    elif 780 <= pos_mouse[0] <= 810 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 39
                    elif 810 <= pos_mouse[0] <= 840 and 390 <= pos_mouse[1] <= 420 and flag_game and flag_my_shot:
                        cell_number = 40
                    elif 540 <= pos_mouse[0] <= 570 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 41
                    elif 570 <= pos_mouse[0] <= 600 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 42
                    elif 600 <= pos_mouse[0] <= 630 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 43
                    elif 630 <= pos_mouse[0] <= 660 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 44
                    elif 660 <= pos_mouse[0] <= 690 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 45
                    elif 690 <= pos_mouse[0] <= 720 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 46
                    elif 720 <= pos_mouse[0] <= 750 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 47
                    elif 750 <= pos_mouse[0] <= 780 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 48
                    elif 780 <= pos_mouse[0] <= 810 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 49
                    elif 810 <= pos_mouse[0] <= 840 and 420 <= pos_mouse[1] <= 450 and flag_game and flag_my_shot:
                        cell_number = 50
                    elif 540 <= pos_mouse[0] <= 570 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 51
                    elif 570 <= pos_mouse[0] <= 600 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 52
                    elif 600 <= pos_mouse[0] <= 630 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 53
                    elif 630 <= pos_mouse[0] <= 660 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 54
                    elif 660 <= pos_mouse[0] <= 690 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 55
                    elif 690 <= pos_mouse[0] <= 720 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 56
                    elif 720 <= pos_mouse[0] <= 750 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 57
                    elif 750 <= pos_mouse[0] <= 780 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 58
                    elif 780 <= pos_mouse[0] <= 810 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 59
                    elif 810 <= pos_mouse[0] <= 840 and 450 <= pos_mouse[1] <= 480 and flag_game and flag_my_shot:
                        cell_number = 60
                    elif 540 <= pos_mouse[0] <= 570 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 61
                    elif 570 <= pos_mouse[0] <= 600 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 62
                    elif 600 <= pos_mouse[0] <= 630 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 63
                    elif 630 <= pos_mouse[0] <= 660 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 64
                    elif 660 <= pos_mouse[0] <= 690 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 65
                    elif 690 <= pos_mouse[0] <= 720 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 66
                    elif 720 <= pos_mouse[0] <= 750 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 67
                    elif 750 <= pos_mouse[0] <= 780 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 68
                    elif 780 <= pos_mouse[0] <= 810 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 69
                    elif 810 <= pos_mouse[0] <= 840 and 480 <= pos_mouse[1] <= 510 and flag_game and flag_my_shot:
                        cell_number = 70
                    elif 540 <= pos_mouse[0] <= 570 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 71
                    elif 570 <= pos_mouse[0] <= 600 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 72
                    elif 600 <= pos_mouse[0] <= 630 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 73
                    elif 630 <= pos_mouse[0] <= 660 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 74
                    elif 660 <= pos_mouse[0] <= 690 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 75
                    elif 690 <= pos_mouse[0] <= 720 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 76
                    elif 720 <= pos_mouse[0] <= 750 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 77
                    elif 750 <= pos_mouse[0] <= 780 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 78
                    elif 780 <= pos_mouse[0] <= 810 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 79
                    elif 810 <= pos_mouse[0] <= 840 and 510 <= pos_mouse[1] <= 540 and flag_game and flag_my_shot:
                        cell_number = 80
                    elif 540 <= pos_mouse[0] <= 570 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 81
                    elif 570 <= pos_mouse[0] <= 600 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 82
                    elif 600 <= pos_mouse[0] <= 630 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 83
                    elif 630 <= pos_mouse[0] <= 660 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 84
                    elif 660 <= pos_mouse[0] <= 690 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 85
                    elif 690 <= pos_mouse[0] <= 720 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 86
                    elif 720 <= pos_mouse[0] <= 750 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 87
                    elif 750 <= pos_mouse[0] <= 780 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 88
                    elif 780 <= pos_mouse[0] <= 810 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 89
                    elif 810 <= pos_mouse[0] <= 840 and 540 <= pos_mouse[1] <= 570 and flag_game and flag_my_shot:
                        cell_number = 90
                    elif 540 <= pos_mouse[0] <= 570 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 91
                    elif 570 <= pos_mouse[0] <= 600 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 92
                    elif 600 <= pos_mouse[0] <= 630 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 93
                    elif 630 <= pos_mouse[0] <= 660 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 94
                    elif 660 <= pos_mouse[0] <= 690 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 95
                    elif 690 <= pos_mouse[0] <= 720 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 96
                    elif 720 <= pos_mouse[0] <= 750 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 97
                    elif 750 <= pos_mouse[0] <= 780 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 98
                    elif 780 <= pos_mouse[0] <= 810 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 99
                    elif 810 <= pos_mouse[0] <= 840 and 570 <= pos_mouse[1] <= 600 and flag_game and flag_my_shot:
                        cell_number = 100
                    if flag_main_menu and flag_choice_battleship and 0 < cell_number < 101 and not flag_battleship:
                        choice_battleship(screen, cell_number)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_cruiser_1 and 0 < cell_number < 101 and not flag_cruiser_1:
                        choice_cruiser(screen, cell_number, 1)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_cruiser_2 and 0 < cell_number < 101 and not flag_cruiser_2:
                        choice_cruiser(screen, cell_number, 2)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_destroyer_1 and 0 < cell_number < 101 and not flag_destroyer_1:
                        choice_destroyer(screen, cell_number, 1)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_destroyer_2 and 0 < cell_number < 101 and not flag_destroyer_2:
                        choice_destroyer(screen, cell_number, 2)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_destroyer_3 and 0 < cell_number < 101 and not flag_destroyer_3:
                        choice_destroyer(screen, cell_number, 3)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_boat_1 and 0 < cell_number < 101 and not flag_boat_1:
                        choice_boat(screen, cell_number, 1)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_boat_2 and 0 < cell_number < 101 and not flag_boat_2:
                        choice_boat(screen, cell_number, 2)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_boat_3 and 0 < cell_number < 101 and not flag_boat_3:
                        choice_boat(screen, cell_number, 3)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    elif flag_main_menu and flag_choice_boat_4 and 0 < cell_number < 101 and not flag_boat_4:
                        choice_boat(screen, cell_number, 4)
                        if flag_sound:
                            pygame.mixer.music.play()
                        cell_number = 0
                    if flag_game and flag_my_shot and cell_number != 0:
                        my_shot(screen, cell_number)
                        number_shots_remaining(screen)
                        cell_number = 0
            if event.type == pygame.KEYDOWN and flag_selection_menu and difficulty_level == 'beginner' \
                    and flag_advantage and flag_input:
                input_box = pygame.Rect(480, 435, 151, 60)
                if event.key == pygame.K_BACKSPACE:
                    text_data = text_data[:-1]
                    if flag_sound:
                        pygame.mixer.music.play()
                    pygame.Surface.fill(screen, (255, 250, 250), (480, 435, 151, 60))
                    notebook_sheet(screen)
                    pygame.draw.rect(screen, (255, 0, 0), input_box, 5)
                    text_data_1 = f1.render(text_data, True, (80, 123, 175))
                    screen.blit(text_data_1, (480 + 65, 435 + 13))
                    pygame.display.update((480, 435, 151, 60))
                elif event.key == pygame.K_RETURN:
                    if flag_sound:
                        pygame.mixer.music.play()
                    if 0 <= int(text_data) <= 10:
                        handicap_beginner = int(text_data)
                        pygame.Surface.fill(screen, (255, 250, 250), (480, 435, 151, 60))
                        notebook_sheet(screen)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 5)
                        if len(text_data) == 1:
                            text_data_1 = f1.render(text_data, True, (0, 255, 0))
                            screen.blit(text_data_1, (480 + 65, 435 + 13))
                        elif len(text_data) == 2:
                            text_data_1 = f1.render(text_data, True, (0, 255, 0))
                            screen.blit(text_data_1, (480 + 50, 435 + 13))
                        pygame.display.update((480, 435, 151, 60))
                else:
                    if flag_sound:
                        pygame.mixer.music.play()
                    text_data += event.unicode
                    pygame.Surface.fill(screen, (255, 250, 250), (480, 435, 151, 60))
                    notebook_sheet(screen)
                    pygame.draw.rect(screen, (255, 0, 0), input_box, 5)
                    try:
                        if int(text_data) in range(0, 11):
                            if len(text_data) == 1:
                                text_data_1 = f1.render(text_data, True, (80, 123, 175))
                                screen.blit(text_data_1, (480 + 65, 435 + 13))
                            elif len(text_data) == 2:
                                if int(text_data) == 0:
                                    text_data = '0'
                                    text_data_1 = f1.render(text_data, True, (80, 123, 175))
                                    screen.blit(text_data_1, (480 + 65, 435 + 13))
                                else:
                                    text_data_1 = f1.render(text_data, True, (80, 123, 175))
                                    screen.blit(text_data_1, (480 + 50, 435 + 13))
                        else:
                            text_data = text_data[:-1]
                            if len(text_data) == 1:
                                text_data_1 = f1.render(text_data, True, (80, 123, 175))
                                screen.blit(text_data_1, (480 + 65, 435 + 13))
                            elif len(text_data) == 2:
                                text_data_1 = f1.render(text_data, True, (80, 123, 175))
                                screen.blit(text_data_1, (480 + 50, 435 + 13))
                    except ValueError:
                        text_data = ''
                        if flag_sound:
                            pygame.mixer.music.play()
                        pygame.Surface.fill(screen, (255, 250, 250), (480, 435, 151, 60))
                        notebook_sheet(screen)
                        pygame.draw.rect(screen, (255, 0, 0), input_box, 5)
                    pygame.display.update((480, 435, 151, 60))
        if flag_game and flag_enemy_shot and difficulty_level == 'beginner':
            beginner_enemy_shot(screen)
            number_shots_remaining(screen)
            cell_number = 0
        elif flag_game and flag_enemy_shot and difficulty_level == 'master':
            master_enemy_shot(screen)
            number_shots_remaining(screen)
            cell_number = 0
        elif flag_game and flag_enemy_shot and difficulty_level == 'professional':
            professional_enemy_shot(screen)
            number_shots_remaining(screen)
            cell_number = 0
        if not flag_game and not flag_main_menu and not flag_selection_menu and not flag_statistics and not flag_quit:
            flag_quit = True
            screen_music.stop()
            if flag_enemy_victory:
                screen_music = pygame.mixer.Sound('music/поражение.mp3')
                if flag_sound:
                    screen_music.set_volume(1.0)
                elif not flag_sound:
                    screen_music.set_volume(0.0)
                screen_music.play(-1)
            if flag_my_victory:
                screen_music = pygame.mixer.Sound('music/verdi_marsh.mp3')
                if flag_sound:
                    screen_music.set_volume(1.0)
                elif not flag_sound:
                    screen_music.set_volume(0.0)
                screen_music.play(-1)
            if flag_enemy_victory:
                screen_music_1 = pygame.mixer.Sound('music/bomba.mp3')
                if flag_sound:
                    screen_music_1.set_volume(0.5)
                elif not flag_sound:
                    screen_music_1.set_volume(0.0)
                screen_music_1.play(-1)
            elif flag_my_victory:
                screen_music_1 = pygame.mixer.Sound('music/saljuta.mp3')
                if flag_sound:
                    screen_music_1.set_volume(0.5)
                elif not flag_sound:
                    screen_music_1.set_volume(0.0)
                screen_music_1.play(-1)
        if not flag_game and not flag_main_menu and not flag_selection_menu and not flag_statistics and flag_quit:
            victory(screen)
            if flag_my_victory:
                tmp = 'picture/салют/' + str(salute) + '.png'
                smail = pygame.image.load(tmp).convert_alpha()
                smail = pygame.transform.scale(smail, (240, 250))
                screen.blit(smail, (50, 200))
                tmp = 'picture/салют_2/' + str(salute_2) + '.png'
                smail = pygame.image.load(tmp).convert_alpha()
                smail = pygame.transform.scale(smail, (200, 250))
                screen.blit(smail, (540, 210))
                pygame.time.wait(150)
                salute += 1
                salute_2 += 1
                if salute == 35:
                    salute = 0
                if salute_2 == 25:
                    salute_2 = 0
            elif flag_enemy_victory:
                tmp = 'picture/взрыв/' + str(bomba) + '.png'
                smail = pygame.image.load(tmp).convert_alpha()
                smail = pygame.transform.scale(smail, (250, 250))
                screen.blit(smail, (30, 200))
                pygame.time.wait(105)
                bomba += 1
                if bomba == 24:
                    bomba = 0
            pygame.display.update((30, 190, 1055, 510))
            pygame.mixer.music.load('music/click.mp3')


if __name__ == '__main__':
    cell = {1: [120, 300], 2: [150, 300], 3: [180, 300], 4: [210, 300], 5: [240, 300], 6: [270, 300], 7: [300, 300],
            8: [330, 300], 9: [360, 300], 10: [390, 300], 11: [120, 330], 12: [150, 330], 13: [180, 330],
            14: [210, 330], 15: [240, 330], 16: [270, 330], 17: [300, 330], 18: [330, 330], 19: [360, 330],
            20: [390, 330], 21: [120, 360], 22: [150, 360], 23: [180, 360], 24: [210, 360], 25: [240, 360],
            26: [270, 360], 27: [300, 360], 28: [330, 360], 29: [360, 360], 30: [390, 360], 31: [120, 390],
            32: [150, 390], 33: [180, 390], 34: [210, 390], 35: [240, 390], 36: [270, 390], 37: [300, 390],
            38: [330, 390], 39: [360, 390], 40: [390, 390], 41: [120, 420], 42: [150, 420], 43: [180, 420],
            44: [210, 420], 45: [240, 420], 46: [270, 420], 47: [300, 420], 48: [330, 420], 49: [360, 420],
            50: [390, 420], 51: [120, 450], 52: [150, 450], 53: [180, 450], 54: [210, 450], 55: [240, 450],
            56: [270, 450], 57: [300, 450], 58: [330, 450], 59: [360, 450], 60: [390, 450], 61: [120, 480],
            62: [150, 480], 63: [180, 480], 64: [210, 480], 65: [240, 480], 66: [270, 480], 67: [300, 480],
            68: [330, 480], 69: [360, 480], 70: [390, 480], 71: [120, 510], 72: [150, 510], 73: [180, 510],
            74: [210, 510], 75: [240, 510], 76: [270, 510], 77: [300, 510], 78: [330, 510], 79: [360, 510],
            80: [390, 510], 81: [120, 540], 82: [150, 540], 83: [180, 540], 84: [210, 540], 85: [240, 540],
            86: [270, 540], 87: [300, 540], 88: [330, 540], 89: [360, 540], 90: [390, 540], 91: [120, 570],
            92: [150, 570], 93: [180, 570], 94: [210, 570], 95: [240, 570], 96: [270, 570], 97: [300, 570],
            98: [330, 570], 99: [360, 570], 100: [390, 570]}
    cell_2 = {1: [540, 300], 2: [570, 300], 3: [600, 300], 4: [630, 300], 5: [660, 300], 6: [690, 300], 7: [720, 300],
              8: [750, 300], 9: [780, 300], 10: [810, 300], 11: [540, 330], 12: [570, 330], 13: [600, 330],
              14: [630, 330], 15: [660, 330], 16: [690, 330], 17: [720, 330], 18: [750, 330], 19: [780, 330],
              20: [810, 330], 21: [540, 360], 22: [570, 360], 23: [600, 360], 24: [630, 360], 25: [660, 360],
              26: [690, 360], 27: [720, 360], 28: [750, 360], 29: [780, 360], 30: [810, 360], 31: [540, 390],
              32: [570, 390], 33: [600, 390], 34: [630, 390], 35: [660, 390], 36: [690, 390], 37: [720, 390],
              38: [750, 390], 39: [780, 390], 40: [810, 390], 41: [540, 420], 42: [570, 420], 43: [600, 420],
              44: [630, 420], 45: [660, 420], 46: [690, 420], 47: [720, 420], 48: [750, 420], 49: [780, 420],
              50: [810, 420], 51: [540, 450], 52: [570, 450], 53: [600, 450], 54: [630, 450], 55: [660, 450],
              56: [690, 450], 57: [720, 450], 58: [750, 450], 59: [780, 450], 60: [810, 450], 61: [540, 480],
              62: [570, 480], 63: [600, 480], 64: [630, 480], 65: [660, 480], 66: [690, 480], 67: [720, 480],
              68: [750, 480], 69: [780, 480], 70: [810, 480], 71: [540, 510], 72: [570, 510], 73: [600, 510],
              74: [630, 510], 75: [660, 510], 76: [690, 510], 77: [720, 510], 78: [750, 510], 79: [780, 510],
              80: [810, 510], 81: [540, 540], 82: [570, 540], 83: [600, 540], 84: [630, 540], 85: [660, 540],
              86: [690, 540], 87: [720, 540], 88: [750, 540], 89: [780, 540], 90: [810, 540], 91: [540, 570],
              92: [570, 570], 93: [600, 570], 94: [630, 570], 95: [660, 570], 96: [690, 570], 97: [720, 570],
              98: [750, 570], 99: [780, 570], 100: [810, 570]}
    flag_sound = True  # звук вкл/откл
    flag_selection_menu = True  # меню выбора сложности игры
    flag_statistics = False  # экран статистики
    difficulty_level = None  # уровень сложности игры
    list_ban_cell = []  # список запрещенных клеток для установки корабля
    list_battleship = []  # список координат установки корабля
    list_probability_ship = []  # список вариатов установки корабля
    list_enemy_ships = []  # список вражеских кораблей
    list_enemy_battleship = []  # координаты вражеского линкора
    list_enemy_cruiser_1 = []  # координаты вражеского крейсера_1
    list_enemy_cruiser_2 = []  # координаты вражеского крейсера_2
    list_enemy_destroyer_1 = []  # координаты вражеского эсминца_1
    list_enemy_destroyer_2 = []  # координаты вражеского эсминца_2
    list_enemy_destroyer_3 = []  # координаты вражеского эсминца_3
    list_enemy_boat_1 = []  # координаты вражеского катера_1
    list_enemy_boat_2 = []  # координаты вражеского катера_2
    list_enemy_boat_3 = []  # координаты вражеского катера_3
    list_enemy_boat_4 = []  # координаты вражеского катера_4
    list_killed_enemy_ships = []  # список вражеских убитых кораблей
    list_injured_enemy_ships = []  # список раненых вражеских кораблей
    list_my_shot = []  # список моих выстрелов
    list_my_ship = []  # список моих кораблей
    list_my_battleship = []  # координаты моего линкора
    list_my_cruiser_1 = []  # координаты моего крейсера_1
    list_my_cruiser_2 = []  # координаты моего крейсера_2
    list_my_destroyer_1 = []  # координаты моего эсминца_1
    list_my_destroyer_2 = []  # координаты моего эсминца_2
    list_my_destroyer_3 = []  # координаты моего эсминца_3
    list_my_boat_1 = []  # координаты моего катера_1
    list_my_boat_2 = []  # координаты моего катера_2
    list_my_boat_3 = []  # координаты моего катера_3
    list_my_boat_4 = []  # координаты моего катера_4
    list_killed_my_ships = []  # список моих убитых кораблей
    list_injured_my_ships = []  # список моих раненых кораблей
    list_enemy_shot = []  # список вражеских выстрелов
    flag_battleship = False  # установлен ли линкор : True - да , False - нет
    flag_cruiser_1 = False  # установлен ли крейсер_1 : True - да , False - нет
    flag_cruiser_2 = False  # установлен ли крейсер_2 : True - да , False - нет
    flag_destroyer_1 = False  # установлен ли эсминец_1 : True - да , False - нет
    flag_destroyer_2 = False  # установлен ли эсминец_2 : True - да , False - нет
    flag_destroyer_3 = False  # установлен ли эсминец_3 : True - да , False - нет
    flag_boat_1 = False  # установлен ли катер_1 : True - да , False - нет
    flag_boat_2 = False  # установлен ли катер_2 : True - да , False - нет
    flag_boat_3 = False  # установлен ли катер_3 : True - да , False - нет
    flag_boat_4 = False  # установлен ли катер_4 : True - да , False - нет
    flag_del_battleship = False  # флаг удаления линкора : True - да , False - нет
    flag_del_cruiser_1 = False  # флаг удаления крейсера_1 : True - да , False - нет
    flag_del_cruiser_2 = False  # флаг удаления крейсера_2 : True - да , False - нет
    flag_del_destroyer_1 = False  # флаг удаления эсминеца_1 : True - да , False - нет
    flag_del_destroyer_2 = False  # флаг удаления эсминеца_2 : True - да , False - нет
    flag_del_destroyer_3 = False  # флаг удаления эсминеца_3 : True - да , False - нет
    flag_del_boat_1 = False  # флаг удаления катера_1 : True - да , False - нет
    flag_del_boat_2 = False  # флаг удаления катера_2 : True - да , False - нет
    flag_del_boat_3 = False  # флаг удаления катера_3 : True - да , False - нет
    flag_del_boat_4 = False  # флаг удаления катера_4 : True - да , False - нет
    flag_my_shot = False  # мой выстрел
    flag_enemy_shot = False  # вражеский выстрел
    flag_my_shot_injured = False  # мой корабль ранен
    flag_game = False  # игра
    flag_my_victory = False  # я победил
    flag_enemy_victory = False  # победил противник
    flag_automatic = False  # автоматическая расстановка кораблей
    list_chek = []  # список галочек установленных кораблей
    flag_strategy_1 = False  # стратегия стрельбы 1
    flag_strategy_2 = False  # стратегия стрельбы 2
    flag_strategy_3 = False  # стратегия стрельбы 3
    flag_strategy_4 = False  # стратегия стрельбы 4
    flag_clear_field = False  # флаг очистки игрового поля
    flag_delete_ship = False  # флаг удаления корабля
    number_moves = 0  # количество ходов (для окна статистики)
    number_whole_ships = 10  # количество выживших кораблей
    flag_select_beginner = False  # выбор строки новичок
    flag_select_master = False  # выбор строки мастер
    flag_select_professional = False  # выбор строки профессионал
    handicap_beginner = 22  # фора для новичка
    flag_advantage = False  # выбор количества форы
    flag_local_battleship = True
    flag_local_cruiser_1 = True
    flag_local_cruiser_2 = True
    flag_local_destroyer_1 = True
    flag_local_destroyer_2 = True
    flag_local_destroyer_3 = True
    flag_local_boat_1 = True
    flag_local_boat_2 = True
    flag_local_boat_3 = True
    flag_local_boat_4 = True
    work()
