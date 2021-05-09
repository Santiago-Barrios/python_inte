from random import randint
from os import system

def read():
    with open('./archivos/data.txt', "r", encoding='utf-8') as f:
        words = [i.replace('\n', '') for i in f]
    return words


def comparison(word, lineas):
    w = list(word)
    l = list (lineas)
    clue = ''
    while w != l:
        clue = input('Ingrese una letra: ')

        assert len(clue) == 1, '¡¡presionanste mas de una letra!!'
        system('clear')
        for i in range(0, len(w)):
            if w[i] == clue:
                l[i] = w[i]
        print(' '.join(l).upper())
        print('\n')
    print('Ganaste la palabra era ' + word.upper())


def run():
    words = read()
    index = randint(0, len(words))
    word = words[index]
    lineas = '-'*len(word)

    print('Adivina la palabra')
    print(' '.join(lineas))
    print('\n')

    comparison(word, lineas)


if __name__ == '__main__':
    run()