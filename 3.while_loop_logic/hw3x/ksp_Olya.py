import random
while True:
	print('Гра камінь ножниці папір. k- камінь,  s- ножниці, p-папір. Щоб завершити введіть: вихід')
	player=input('ви вибрали:')
	if player not in['k', 's', 'p', 'вихід']:
		print('Не правильне введення!!!')
		if player == 'вихід':
			break
		generation = {1: 'k', 2: 's', 3: 'p'}
		choice = generation[random.randit(1,3)]
		print('Комп вибрав:{coice}')
		combination=[('k','s'),('k','p'),('s','p')]
		if player == choice:
			print('Нічия')
		elif(player, choice)in combination:
			print('Ти переміг')
		else:
			print('Комп переміг')