print("hello world!")

def printMe(*arg, **kwargs):
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

myString1 = "hello1"
myString2 = "hello2"
printMe(myString1, myString2, name="xxx", value='yyy', )

