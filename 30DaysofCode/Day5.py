def multiplication_table():
    for x in range(1, 11):
        result = x * n
        print(f'{x} x {n} = {result}')


if __name__ == '__main__':
    n = int(input(f'Choose one number: '))     
    multiplication_table()   