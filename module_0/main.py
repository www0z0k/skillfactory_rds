import numpy as np
import math

MAX_VAL = 100

def set_max():
	while True:
		try:
			val = int(input('\tВведите максимальное значение (целое число больше 1) '))
		except ValueError:
			print('\t\tНе целое или не число')
			continue
		else:
			if(val <= 1):
				print('\t\tНе больше 1')
			else:
				return val 

def game_core_v1(number):
	'''Просто угадываем на random, никак не используя информацию о больше или меньше.
	   Функция принимает загаданное число и возвращает число попыток'''
	count = 0
	while True:
		count += 1
		predict = np.random.randint(1, MAX_VAL + 1) # предполагаемое число
		if number == predict: 
			return count  # выход из цикла, если угадали
		
		
def score_game(game_core, name):
	'''Запускаем игру 1000 раз, чтобы узнать, как быстро игра угадывает число'''
	count_ls = []
	np.random.seed(1)  # фиксируем RANDOM SEED, чтобы ваш эксперимент был воспроизводим!
	random_array = np.random.randint(1, MAX_VAL + 1, size = (1000))
	for number in random_array:
		count_ls.append(game_core(number))
	score = int(np.mean(count_ls))
	print(f"Алгоритм {name} угадывает число от 1 до {MAX_VAL} в среднем за {score} попыток")
	return score

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
	return count # выход из цикла, если угадали

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
	return count # выход из цикла, если угадали


def test_all():
	if(MAX_VAL < 1000):
		score_game(game_core_v1, 'brute')
	else:
		print(f"{MAX_VAL} > 1000, алгоритм brute будет угадывать его слишком долго, пропускаем")
	
	if(MAX_VAL < 100000):
		score_game(game_core_v2, '+/- 1')
	else:
		print(f"{MAX_VAL} > 100000, алгоритм +/- 1 будет угадывать его слишком долго, пропускаем")
	score_game(game_core_v3, 'regression')


def once_more():
	reply = input('\tТеперь можно проверить на произвольных значениях, хотите? Нажмите Enter чтобы продолжить или введите любой символ и Enter если не надо ')
	if len(reply) == 0:
		global MAX_VAL
		MAX_VAL = set_max()
		test_all()
		once_more()
	else:
		print('Спасибо, всего доброго')
		return

test_all()

once_more()