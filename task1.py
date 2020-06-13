x = float(input("Первая цифра "))
y = float(input("Втораця цифра "))
oper = input("Операция ")

if oper == '+':
    c = x + y
    print(str (c))
elif oper == '-':
    c = x - y
    print(str(c))

elif oper == '*':
    c = x * y
    print(str (c) )
elif oper == '/':
    c = x / y
    print(str(c))

else:
    print('Ошибка')
