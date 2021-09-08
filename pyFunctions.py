def runme():
    print("In pyFunctions")

    # printme(1,2,3,name='x', lastname='y')
    # printMe1(1,2,3,name='x', lastname='y')
    my_dic = {'name': 'gal', 'lastname': 'netanel'}
    print_me_2('1', 2, 3, **my_dic)


def printMe1(*arg, **kwargs):
    print("arg is")
    print(arg)

    print("kwargs is")
    print(kwargs)

    print("print loop of arg")
    for i in arg:
        print(i)

    print("print loop of kwarg")
    for i in kwargs:
        print(i + ", " + kwargs[i])


def print_me_2(first_param, *arg, **kwargs):
    print("firstParam is " + first_param)

    print("arg is")
    print(arg)

    print("kwargs is")
    print(kwargs)

    print("print loop of arg")
    for i in arg:
        print(i)

    print("print loop of kwarg")
    for i in kwargs:
        print(i + ", " + kwargs[i])


runme()
