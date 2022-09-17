print('Введите систему счисления, в которую нужно перевести десятичное число')
sys_base = int(input()) #основание систему счисления, в которую переводим
remainder = 0 #остаток
whole_quot = 0 #целое частное
print('Введите число, которое хотите перевести в другую систему счисления')
sys_16_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
num_enter = int(input())
new_num_list = []

remainder = num_enter % sys_base
new_num_list.append(remainder)
whole_quot = num_enter // sys_base
if whole_quot > sys_base:
    while whole_quot >= sys_base:
        remainder = whole_quot % sys_base
        new_num_list.append(whole_quot % sys_base)
        whole_quot //= sys_base
    new_num_list.append(whole_quot)
new_num_list.reverse()

for i in new_num_list:
    if 9 < i <= 16:
        i = sys_16_list[i]
    print(i, end='', sep='')