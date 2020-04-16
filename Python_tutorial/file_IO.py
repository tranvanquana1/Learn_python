#ham input

name = input('my name is ')
print(name)

#opening and closing files

fo = open("foo.txt", 'w')   #mo file
print('name of the file: ', fo.name)

print('closed or not: ', fo.closed)
print('opening mode: ', fo.mode)

fo.close()  #dong file

#reading file
fr = open('foo.txt', 'a+')
fr.write('hello Tit')   #ghi file

print(fr.read(20))  #doc file

fr.close()

#rename and delete file
import os
os.rename('foo.txt', 'test.txt')    #doi ten file

os.remove('test.txt')   #xoa file

os.mkdir('data') #them folder

os.rmdir('data')    #xoa folder