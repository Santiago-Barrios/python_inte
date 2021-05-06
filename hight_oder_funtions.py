from functools import reduce


def run():
    my_list = [1, 4, 6, 9, 13, 19, 21]
    odd = list(filter(lambda x: x%2 !=0, my_list ))
    print(odd)

    my_list2 = [1, 2, 3, 4, 5]
    squares = [ i**2 for i in my_list2 ]
    squares2 = list(map(lambda x: x**2, my_list2 ))
    print(squares2)

    my_list3 = [2, 2, 2, 2, 2]
    # all_multiplied = 1
    # for i in my_list3:
    #     all_multiplied = all_multiplied * i
    # print(all_multiplied)
    all_multiplied = reduce(lambda a, b : a * b, my_list3)
    print(all_multiplied)

if __name__ == '__main__':
    run()