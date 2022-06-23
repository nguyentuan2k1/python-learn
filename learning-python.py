# Học python qua giải bài tập
# Giải bài tập python ở trang :
# https://quantrimang.com/hon-100-bai-tap-python-co-loi-giai-code-mau-142456



#Bài 1 : 

# ar = []
# for i in range(2000,3200+1):
#     if(i % 7 == 0 and i % 5 != 0 ):
#         ar.append(str(i))

# print(','.join(ar))

#End bài 1

#Bài 2 :
# value = input("Nhập số cần tính vào :")
# tong = 1
# for i in range(1,int(value)+1):
#     tong*= i

# print(str(tong))

# End bài 2

#  bài 3
# dic = {}
# input = input("Nhập số nguyên N vào: ")
# for i in range(1,int(input)+1):
#     dic[i] = i*i

# print(dic)

# End bài 3
#  bài 4

# ar  = [ x for x in input("Nhập chuỗi số vào , cách nhau bằng dấu , :").split(',')]
# tuple = tuple(ar)
# print(ar)
# print(tuple)



# End bài 4



#  bài 5



# class InputString(object) :
#     def __init__(self) :
#         self.s = ''

#     def getString(self):
#         self.s = input('Nhập chuỗi vào :')
    
#     def printString(self):
#         print(self.s.upper())


# Strobj = InputString()
# Strobj.getString()
# Strobj.printString()
# End bài 5


#  bài 6

# x = int(input('Nhập số cần tính vào :'))

# def square(numb) :
#     numb = numb ** 2
#     return numb

# print(str(square(x)))
# End bài 6


#  bài 7

# print(abs.__doc__)

# print(int.__doc__)

# print(input.__doc__)

# End bài 7


#  bài 8


# class Person : 
   
#     def __init__(self,name):
#         self.name = name
    
#     def printName(self):
#         print("Tên của bạn là :"+self.name)


# person = Person('Tèo')
# person.name = 'Tí'
# person.printName()


# person1 = Person()

# person1.printName()
# End bài 8


# Bài 9

# import math


# def caculate_value(numb):
#     value = math.sqrt((2*50*numb)/30)
#     return round(value)

# input = [x for x in input('Nhập giá trị cần tính vào cách nhau bởi dấu , :').split(',')]
# ar = []
# for i in range(0,len(input)):
#     ar.append(str(caculate_value(int(input[i]))))

# print(','.join(ar))

# End bài 9


#  bài 10

# input = input('Nhập giá trị X và Y vào , cách nhau bởi dấu "," :').split(',')
# # x =  input[0]
# # y = input[1]

# ar_2_chieu = []
# for i in range(0,int(input[0])):
#     ar_2_chieu.append([])
#     # print(ar_2_chieu)
#     for y in range(0,int(input[1])):   
#         ar_2_chieu[i].append(int(0))

# for i in range(0,int(input[0])):
   
#     for y in range(0,int(input[1])):   
#         ar_2_chieu[i][y] = i*y



# print(ar_2_chieu)



# End bài 10

#  bài 11

# item = [x for x in input('Nhập dữ liệu vào , cách nhau bởi dấu , :').split(',') ]
# item.sort()
# print(','.join(item))

# End bài 11

#  bài 12


# item = [x for x in input('Nhập dữ liệu vào , cách nhau bởi dấu , :').split(',') ]



# #Foreach python
# for i in range(len(item)):
#     item[i] = item[i].upper()
    
   
# print(item)





# End bài 12


#  bài 13


# s = input('Nhập chuỗi vào tách nhau bởi khoảng trắng').split(' ')
# sortlist = sorted(list(set(s)))
# print(' '.join(sortlist))

# End bài 13


#  bài 14

# check = True
# def checknumber(arr):
#     returnvalue = False
#     for i in range(0,len(arr)) :
#         if(len(arr[i]) != 4):
#             returnvalue = True
#             break
    
#     return returnvalue

# while(check):
#     so = input('Nhập các số nhị phân có 4 chữ số , nếu sai nhập lại :').split(',')
#     check = checknumber(so)

# arr_temp = []
# for j in range(0,len(so)):
#     if(int(so[j])%5 == 0):
#         arr_temp.append(so[j])

# print(",".join(arr_temp))


# End bài 14


#  bài 15
# def allnumberischan(numb):
#     numb = str(numb)
#     for j in range(0,len(numb)):
#         if(int(numb[j]) % 2 != 0):
#             return False
#     return True

# arr_temp = []
# for i in range(1000,3000+1):
#     if(allnumberischan(i)):
#         arr_temp.append(str(i))

# print(",".join(arr_temp))
# End bài 15


#  bài 16

# st = input('Nhập dữ liệu đầu vào')
# numb = 0
# string = 0
# for i in range(0,len(st)):
#     if(st[i].isdigit()):
#         numb+=1
#     elif(st[i].isalpha()):
#         string+=1

# print("Số là {0}".format(numb)+" Chữ là {0}".format(string))
# End bài 16

#  bài 17
# st = input('Nhập dữ liệu đầu vào')

# d = {"Upper Case":0,"LOWER CASE":0}

# for i in st:
#     if(i.islower()):
#         d["LOWER CASE"] +=1
#     elif(i.isupper()):
#         d["Upper Case"] +=1

# print ("Chữ hoa:", d["Upper Case"])
# print ("Chữ thường:", d["LOWER CASE"])
# End bài 17


#  bài 18
# a = input('Nhập số a')
# n1 = int("%s"%a)
# n2 = int("%s%s"%(a,a))
# n3 = int("%s%s%s"%(a,a,a))
# n4 = int("%s%s%s%s"%(a,a,a,a))
# print("Tổng cần tính",n1+n2+n3+n4)

# End bài 18


#  bài 19

# values = input("Nhập dữ liệu vào")
# temp_arr = []
# for i in values:
#     if(int(i)%2 != 0):
#         temp_arr.append(i)

# print(temp_arr)
# End bài 19


#  bài 20
# money = 0
# while True:
#     s = input("Nhap nhat ky giao dich : ")
#     if not s:
#         break
#     values = s.split(' ')
#     opeators = values[0]
#     amount = values[1]
#     if opeators == 'D':
#         money += int(amount)
#         print("So tien ban dang co la :"+str(money))
#     elif(opeators == 'W'):
#         if(money - int(amount) >=0):
#             money -= int(amount)
#             print("So tien ban dang co la :"+str(money))
#         else:
#               print("Ban khong the rut tien vi ban khong du :"+str(money))
#     else:
#         pass


# End bài 20

#  bài 21
import re


value = input("Nhập dữ liệu đầu vào: ").split(',')
password_valid = []
for i in range(0,len(value)):
    if(len(value[i])<6 or len(value[i])>12):
        continue
    if not(re.search(['a-z'],value[i])):
        continue
    if not (re.search(['0-9'],value[i])):
        continue
    if not (re.search(['A-Z'],value[i])):
        continue
    if not (re.search(['$#@'],value[i])):
        continue
    password_valid.append(value[i])

print(password_valid)





# End bài 21