def fibonacci(n):
    if n < 3:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = int(input('Введите количество членов последовательности Фибоначчи n: '))
if n < 1:
    print('Число меньшее единицы, не может быть n-ым членом последовательности')
else:
    print(n,'-ый член последовательности Фибоначчи равен ', fibonacci(n))