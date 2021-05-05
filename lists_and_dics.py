def run():
    my_list = [1, "hello", True, 4.5]
    my_dict = {
        "firstname": "santiago",
        "lastname": "Barrios"
    }

    super_list = [
        { "firstname": "santiago", "lastname": "Barrios" },
        { "firstname": "pedro", "lastname": "coral" },
        { "firstname": "paco", "lastname": "de lucía" },
        { "firstname": "sara", "lastname": "corrales" },
        { "firstname": "Thomas", "lastname": "uribe" },
        { "firstname": "facundo", "lastname": "cabral" },
    ]

    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_num": [ -1, -2, 0, 1, 2 ],
        "floating_nums": [1.1, 2.5, 4.3, 7.9]
    }

    # for key, value in super_dict.items():
    #     print(key, "-", value)

    # for values in super_list:
    #     for key, value in values.items():
    #         print(f'{key} - {value}')

    for item in super_list:
        print(item["firstname"] , "-" , item["lastname"])

if __name__ == '__main__':
    run()