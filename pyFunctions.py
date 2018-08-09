def runme():
    print("In pyFunctions")

    #printme(1,2,3,name='x', lastname='y')
    #printMe1(1,2,3,name='x', lastname='y')
    myDic = {'name':'gal', 'lastname': 'netanel'}
    printMe2('1', 2, 3, **myDic)




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

def printMe2(firstParam , *arg, **kwargs):
    print("firstParam is " + firstParam)

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
