def listfunc():
    print("in func1 of list functions module")
    myList = ['one', 'two']
    myList2 = list(('x, y', 'z'))
    myList2.append('w')

    print(myList2)
    print(myList)
    print("Printing list in loop")
    for i in myList:
        print("i=" + i)

    myList.append('three')
    print(myList)
    myList.pop(1)
    myList.remove('one')
    print("printing before clear" + myList.__str__())
    print(myList)
    myList.clear()

    print("printing after clear" + myList.__str__())


def tupleFunctions():
    myTuple = ('one', 'two', 'three')
    print(myTuple)

def setFunctions():
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
    myDic = {'name':'gal', 'lastname':'netanel'}
    print(myDic)
    myDic.pop('name');
    print(myDic)
    myDic['x'] = 'y'
    print(myDic)
