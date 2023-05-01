import random

symbols = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
count = int(input('Введите длину пароля'))
result = ''
for i in range(count):
    result += random.choice(symbols)
print(result)