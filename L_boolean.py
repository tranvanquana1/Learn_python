#boolean value
print(3>9)
print(3>1)

a,b = 20,100
if a>b:
    print("a is greater than b")
else:
    print("b is greater than a")

"""evaluate boolean and variable
    most values are true: any string is true, except empty string is false
    number is true, except number 0
    any list, tuple, set, dictionary are true, exept empty ones
"""
print(bool("hello"))

#some values are false
#the following will return false
bool(False)
bool(None)
bool(())
bool([])
bool({})
bool(0)
bool("")

#function can return a boolean
#function isinstance() can be used determine if an object is of a certain data type 
x = 200
print(isinstance(x, int))