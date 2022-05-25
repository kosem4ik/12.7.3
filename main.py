price_all = 0
while True:
    try:
        ticket_number = int(input('Сколько билетов вы хотите приобрести на мероприятие? '))
        if type(ticket_number) == int:
            break
    except ValueError:
        print('Введите целое число')
for i in range(ticket_number):
    i += 1
    while True:
        try:
            age_for_ticket = int(input(f'Для какого возраста билет №{i}? '))
            if age_for_ticket < 18:
                print('Билет бесплатный')
            elif 25 > age_for_ticket >= 18:
                price_all += 990
                print('Стоимость билета: 990 руб.')
            else:
                price_all += 1390
                print('Стоимость билета: 1390 руб.')
            if type(age_for_ticket) == int:
                break
        except ValueError:
            print('Введите целое число')
if ticket_number > 3:
    price_all = price_all - ((price_all / 100) * 10)
    print(f'Сумма к оплате {price_all} руб. с учетом 10%-ой '
          f'скидки на полную стоимость заказа '
          f'за регистрацию больше 5-и человек')
else:
    print(f'Сумма к оплате {price_all} руб.')
