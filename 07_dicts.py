#Diccionarios
#Son mutables
#Sin orden
my_dict = dict()

print(type(my_dict))

my_other_dict = {'Nombre':'Brenda', 'Apellido':'Veramendi','DNI':34426962}
print(my_other_dict)
#Acceder a los diccionarios
#Solo por la cable
print(my_other_dict['Apellido'])

#Busca por clave no por el valor
print('Apellido' in my_other_dict)

print(my_other_dict.items())
print(my_other_dict.keys())
print(my_other_dict.values())
