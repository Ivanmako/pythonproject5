number = input('Введите число: ')[::-1].upper()
    base = int(input('Введите основание: '))
def translate(number, base):
    digits = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    number = input('Введите число: ')[::-1].upper()
    base = int(input('Введите основание: '))
    dec_number = 0
    for i in range(len(number)):
        dec_number += digits.index(number[i]) * base ** i
    return dec_number