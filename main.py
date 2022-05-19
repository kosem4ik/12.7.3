money = input('Введите сумму: ')
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = [value * float(money) for value in per_cent.values()]
print('Максимальная сумма, которую вы можете заработать: ' + str(max(deposit)))
