def list_func():
    print("in func1 of list functions module")
    my_list = ['one', 'two']
    my_list2 = list(('x, y', 'z'))
    my_list2.append('w')

    print(my_list2)
    print(my_list)
    print("Printing list in loop")
    for i in my_list:
        print("i=" + i)

    my_list.append('three')
    print(my_list)
    my_list.pop(1)
    my_list.remove('one')
    print("printing before clear" + my_list.__str__())
    print(my_list)
    my_list.clear()

    print("printing after clear" + my_list.__str__())


def tuple_functions():
    myTuple = ('one', 'two', 'three')
    print(myTuple)


def set_functions():
    mySet1 = set(('setone', 'settwo', 'setthree'))
    print(mySet1)

    mySet2 = {'set1_one', 'set1_two', 'set1_three'}
    print(mySet2)
    mySet2.add('zzzz')
    print(mySet2)
    mySet2.add('zzzz')
    mySet2.add('zzzz')
    print(mySet2)
    mySet2.remove('zzzz')
    print(mySet2)


def dictFunctions():
    myDic = {'name': 'gal', 'lastname': 'netanel'}
    print(myDic)
    myDic.pop('name');
    print(myDic)
    myDic['x'] = 'y'
    print(myDic)
