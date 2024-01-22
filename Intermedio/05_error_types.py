#Error Types

#SyntaxError
#El editor de codigo lo detecta
#printn(9)
print("python")

#NameError
#Se debe difinir name
#print(name)
first_name= "Brenda Veramendi"
print(first_name)

my_list = ['Python','Swift','Kotlin','Dart','Javascript']
print(my_list[0])
print(my_list[4])
print(my_list[-1])
#print(my_list[6])

#ModulesNotFoundError
#imports math
import math

#AtributeError
#print(math.PI)
print(math.pi)

#KeyError

my_dict = {"Nombre":"Brenda", "Apellido":"Veramendi",1:"Python"}
print(my_dict["Apellido"])
#print(my_dict["Apelsido"])

#TypeError
#print(my_dict["0"]) Error
print(my_dict[0])

#ImportError
#from math import PI Error
from math import pi
print(pi)

#ValueError
# Error my_int = int("10 Años")
my_int = int("10")

#ZeroDivisionError
#print(4/0)
print(4/2)











