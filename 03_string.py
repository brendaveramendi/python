my_string = 'Este es un string'
my_other_string = 'Este es mi otro string'

# \n es un salto de linea
print('Hola soy un string \n este es otro string')
name, last_name = 'Brenda Noelia', 'Veramendi'
print('Hola mi nombre es {} y apellido {}'.format(name,last_name))
print(f'Mi nombre es {name} y  apellido {last_name}')

#Desempaquetandi de caracteres

lenguage = 'python'

a,b,c,d,e,f = lenguage
print(a)
print(b)
print(c)
print(d)
print(e)

#Division 
print('Division')
lenguage_slice = lenguage[0:3
                          ]
print(lenguage_slice)

#Funciones con string

print(lenguage.capitalize())
print(lenguage.upper())
print(lenguage.count('t'))
print(lenguage.isnumeric())
print(lenguage.lower())
print('1'.isnumeric())