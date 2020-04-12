def printme(str):
    print(str)
    return
printme('hello world')

#doi so la 1 list
def changeme(mylist):
    mylist[1] = 15
    print('changed: ', mylist)
    return

changeme([10, 16, 13])

#ham voi doi so mac dinh
def printinfo(name, age = 1):
    print('name:', name)
    print('age:', age)
    return

printinfo(age = 2, name = 'Tit')
printinfo('tit')

#ham co so bien thay doi
def printnum(arg1, *vartuple):
    print(arg1)
    for var in vartuple:
        print(var)
    return

printnum(10)
printnum(10, 15, 20)

#ham an danh lambda arg1, arg2 ...: expression
sum = lambda arg1, arg2: arg1+arg2
print(sum(1, 2))

#ham tra lai trang thai
def sum(num1, num2):
    total = num1 + num2
    return total

total = sum(10, 20)
print(total)

#bien global va bien local

result = 0  #day la bien global

def multip(num1, num2):
    result = num1*num2  #day la bien local
    print('inside function:', result)
    return result

multip(2, 3)

print('outside function:', result)  #result = 0