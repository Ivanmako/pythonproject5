n = int(input())
s = ''
while n > 0: #Вычисление двоичного числа в реверсивном виде
    x = n % 2
    s += str(x)
    n //= 2
for i in range(-1, -len(s) - 1, -1): #Разворот двоичного числа
    print(s[i], end='')
