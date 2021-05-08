def divisors(num):
    divisors = []
    for i in range (1, num +1):
        if num % i == 0:
            divisors.append(i)
    return divisors


def run():
    try:
        num = int(input('ingresa un numero: '))
        if num <=0:
            raise ValueError( 'El valor debe ser positivo' )
        elif type(num) == str:
            raise ValueError( 'El valor debe ser un número' )
        print(divisors(num))
        print('termino mi programa')
    except ValueError as ve:
            print(ve)


if __name__ == '__main__':
    run()