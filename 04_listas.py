#Lista son midificables
#Definicion
my_list = list()
my_other_liust = []

print(len(my_list))
my_list=[10,20,30,30,40,50,60,70]
print(my_list)
print(len(my_list))
print(my_list[0])
print(my_list[-1])
print(my_list.count(30))

#Desacoplar elementos
edad1,edad2,edad3,edad4,edad5,edad6,edad7,edad8 = my_list
print(edad1, edad2)
my_other_list = [1,2,3,4,5,4]
print(my_list + my_other_list)
my_list.append(15)

my_list.insert(1,'salmon')
print(my_list)

#Remover un elemento

my_list.remove('salmon')
print(my_list)

#Eliminar el ultimo elemento
my_list.pop()
print(my_list)
#Eliminar una posicion especifica
my_list.pop(2)
print(my_list)

#copiar lista
my_backup_list = my_list.copy()
print(my_backup_list)

#Eliminar lista

my_list.clear()
print(my_list)