list1 = ['chemistry', 'physical', 16, 15]
list2 = [1, 2, 3, 4, 5]
list3 = ['a', 'b', 'c', 'd', 'e']

print(list1[0])
print(list2[1:4])

#thay doi gia tri cua phan tu
list1[2] = 13
print(list1)

#xoa phan tu
del list1[2]
print(list1)

#cac phep toan
len(list2) #so phan tu cua list2
list4 = list2 + list3   #cong list2 voi list 3
print(list4)
print(['hi']*4) #nhan danh sach
print(3 in list2)   #kiem tra co phan tu trong danh sach ko
print(max(list3))   #tim phan tu lon nhat trong danh sach
min(list2)  #tim phan tu nho nhat

#cac ham khac
list1.append('acb') #them object vao danh sach


list1.count(15) #tim so lan xuat hien cua 1 phan tu

list1.extend('Tit') #them cac ky tu trong 1 chuoi
print(list1)

list1.index('T')    #tra ve vi tri cua phan tu trong danh sach

list1.insert(2, 'Vu')   #them phan tu vao 1 vi tri

list1.pop(15)   #xoa phan tu va tra lai phan tu do

list1.remove('Vu') #xoa phan tu

list1.reverse() #dao nguoc danh sach

list1.sort([function])  #sap xep theo 1 ham 