import os

x = int(input("Digite um número inteiro:"))

for y in range(1, x+1):
    if y % 2 != 0:
        print(y)


os.system("pause")