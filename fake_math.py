def divide(first, second):
    if second == 0:
        return 'Ошибка'
    else:
        return first / second

result = divide(32,6)
result2 = divide(10, 0)
print(result, result2)