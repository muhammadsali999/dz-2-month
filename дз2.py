rounds = 0
while rounds < 12:
    day = input('введите день рождение:').lower ()
    month = input('введите месяц рождение:').lower ()
    if  day == 'stop' or month == 'stop':
        break
    day =int(day)

    month =int(month)

    if  day >=21 and  day <= 31 and    month == 3 or day<= 20 and month == 4:
         print('овен')
    elif day >= 21 and day <= 30 and  month == 4 or day <= 21 and month == 5:
         print('телец')
    elif day >= 22 and day <= 31 and  month == 5 or day <= 21 and month == 6:
         print('близнецы')
    elif day >= 22 and day <= 30 and  month == 6 or day <= 22 and month == 7:
         print('рак')
    elif day >= 23 and day <= 31 and  month == 7 or day <= 21 and month == 8:
         print('лев')
    elif day >= 22 and day <= 31 and  month == 8 or day <= 23 and month == 9:
         print('девы')
    elif day >= 24 and day <= 30 and  month == 9 or day <= 23 and month == 10:
         print('весы')
    elif day >= 24 and day <= 31 and  month == 10 or day <= 22 and month == 11:
         print('скорпион')
    elif day >= 23 and day <= 30 and  month == 11 or day <= 22 and month == 12:
         print('стрелец')
    elif day >= 23 and day <= 31 and  month == 12 or day <= 20 and month == 1:
         print('козерок')
    elif day >= 21 and day <= 31 and  month == 1 or day <= 19 and month == 2:
         print('водолей')
    elif day >= 20 and day <= 29 and  month == 2 or day <= 20 and month == 3:
         print('рыбы')
    else:
         print("Здраствуйте:(знак зодиака не найден)")

    rounds  -= 1