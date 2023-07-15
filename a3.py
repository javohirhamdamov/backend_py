numbers = [3,-4,8,2,0,-5,7,11,-9]
a = numbers[0]+numbers[4]
b = numbers[5]-numbers[3]
c = numbers[7]*numbers[6]
d = numbers[2]/numbers[1]
print(a,b,c,d)
del numbers[7]
numbers.insert(7,1)
numbers.insert(0,numbers.pop(1))
print(numbers)

#listning elementlari ustida amallar bajarildi, 0- va 1- index almashtirildi, 7-index 1ga ozgardi 