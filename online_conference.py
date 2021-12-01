# This is a sample Python script.
num = int(input('Введите количество билетов, которые хотите приобрести:'))
count = 0
for i in range(num):
    age = int(input('Введите возраст посетителя:'))
    if age < 18:
        count = count+0
    elif 18 <= age < 25:
        count = count + 990
    else:
        count = count+1390
    if num > 3:
        cost = cost * 0.9
print('Итого:' + ' ' + str(round(count)) + ' ' + 'рублей')
