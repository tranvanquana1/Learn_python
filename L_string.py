a = 'hello world'
x = """
Tit
15/02/2019
Tran Anh Vu
"""

print(a)

print(x)

print(a[0])
#sub string
print(a[:5])
#operator string
f = a+x
print(f)

#string length
print(len(a))
#check string
c = 'he' not in a
print(c)
#string method
d = a.upper()
print(d)
print(d.lower())
b = a.split(" ")

#format stirng
h = 'hello {}'
print(h.format(x))