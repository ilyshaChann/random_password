import random

password = ''

x = input("Каким вы хотите видеть свой пароль, (из чисел), (из букв)" + " или " "(из чисел и букв)?: \n")

if x == "из чисел":
    for x in range(9):
        password = password + random.choice("0123456789")

elif x == "из букв":
    for x in range(9):
        password = password + random.choice("abcdefghigklmnopqrstuvyxwzABCDEFGHIGKLMNOPQRSTUVYXWZ")

elif x == "из чисел и букв":

    for x in range(9):
        password = password + random.choice("0123456789abcdefghigklmnopqrstuvyxwz")



print("Tвой пароль: " + password)

