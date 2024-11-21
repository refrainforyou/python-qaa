a = ['1,2,3,4', '1,2,3,4,50', 'qwerty1,2,3']


def sum_of_elements(massive):
    massive_int = []
    try:
        for number in massive:
            b = number.split(',')
            for value in b:
                massive_int.append(int(value))
            print(sum(massive_int))
            massive_int = []
    except Exception as e:
        print(f"{e}: 'Не можу це зробити'")


sum_of_elements(a)
