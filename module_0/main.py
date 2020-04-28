import numpy as np
import math

MAX_VAL = 100

def game_core_v1(number):
    '''Просто угадываем на random, никак не используя информацию о больше или меньше.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 0
    while True:
        count += 1
        predict = np.random.randint(1, MAX_VAL + 1) # предполагаемое число
        if number == predict: 
            return(count) # выход из цикла, если угадали
        
        
def score_game(game_core, name):
    '''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
    count_ls = []
    np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
    random_array = np.random.randint(1, MAX_VAL + 1, size = (1000))
    for number in random_array:
        count_ls.append(game_core(number))
    score = int(np.mean(count_ls))
    print(f"Алгоритм {name} угадывает число в среднем за {score} попыток при угадывании числа от 1 до {MAX_VAL}")
    return(score)

def game_core_v2(number):
    '''Сначала устанавливаем любое random число, а потом уменьшаем или увеличиваем его в зависимости от того, больше оно или меньше нужного.
       Функция принимает загаданное число и возвращает число попыток'''
    count = 1
    predict = np.random.randint(1, MAX_VAL + 1)
    while number != predict:
        count += 1
        if number > predict: 
            predict += 1
        elif number < predict: 
            predict -= 1
    return(count) # выход из цикла, если угадали

def game_core_v3(number):
    # try to play with prediction step value
    count = 1
    step = MAX_VAL
    predict = np.random.randint(1, MAX_VAL + 1)
    while number != predict:
        count += 1
        step = math.ceil(step / 2)
        if number > predict: 
            predict += step
        elif number < predict: 
            predict -= step
    return(count) # выход из цикла, если угадали


def test_all():
	score_game(game_core_v1, 'brute')
	score_game(game_core_v2, '+/- 1')
	score_game(game_core_v3, 'regression')


test_all()