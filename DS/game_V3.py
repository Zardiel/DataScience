"""Игра угадай число
компьютер сам угадывает и сам отгадывает число
менее чем за 20 попыток
"""

import numpy as np


def game_core_v3(number: int = 1) -> int:
    """
    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    # Ваш код начинается здесь
    count = 0
    score = 0
    predict = np.random.randint(1, 101)
    while number != predict and score < 3:
        score += 1
        if number > predict:
            predict += int((100 - predict) / 2)
        else:
            predict -= int((100 - predict) / 2)

    while number != predict:
        count += 1
        if number > predict:
            predict += 1
        elif number < predict:
            predict -= 1
    # Ваш код заканчивается здесь

    return count


def score_game(game_core_v3) -> int:
    """За какое количество попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        game_core_v3 ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    # фиксируем сид для воспроизводимости
    np.random.seed(1)
    # загадали список чисел
    random_array = np.random.randint(1, 101, size=(1000))

    for number in random_array:
        count_ls.append(game_core_v3(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попытки")


if __name__ == '__main__':
    # RUN
    score_game(game_core_v3)
