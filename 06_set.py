#Set

my_set = set()
#Es un diccionario si esta vacio
my_other_set = {}

print(type(my_set))
print(type(my_other_set))

my_other_set = {1,2,3,4,5,6,6}
print(my_other_set)
print(type(my_other_set))
#Los set no es unaestructura ordenada
my_other_set.add(7)
my_other_set.add('brenda')
my_other_set.add('a')
print(my_other_set)

#Sin orden

set_sin_orden = {'Mauro', 'Brains', 35,1.77}
print(set_sin_orden)

set_sin_orden.add('maurodev')
print(set_sin_orden)
#Agrega un elemento sin orden con un hash elelemento
my_other_set.add(0)
print(my_other_set)

print(0 in my_other_set)
print(10 in my_other_set)

#Remover un elemento del set
my_other_set.remove('a')
my_other_set.remove('brenda')
print(my_other_set)
#Concatenacion de set

my_set_lenguage = {'Python', 'Kotlin','Swift'}
my_adition = my_set_lenguage.union(my_other_set)
print(my_adition)

#Diferencia de set
my_set = {0,1,2,3}

print(my_adition.difference(my_set))

print(my_adition)