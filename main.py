from random import choice

# all_symbols = "_+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

# lenght = int(input("Введите длину пароля: "))
# password = ""

# for i in range(lenght):
#     password += choice(all_symbols)
# print(password)

sogl = "qwrtpsdfghjklzxcvbnmQWRTPSDFGHJKLZXCVBNM"
glas = "eyuioa"
numbers = "1234567890"
symbols = "!@#$+=-_"
password = ""

for i in range(5):
    password += choice(sogl) + choice(glas)
for i in range(3):
    password += choice(numbers)
for i in range(2):
    password += choice(symbols)
print(password)
