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


item = [x for x in input('Nhập dữ liệu vào , cách nhau bởi dấu , :').split(',') ]


# End bài 12