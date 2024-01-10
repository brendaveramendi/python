#Funciones

def my_function ():
  print('Esto es una funcion')
  
my_function()

def sum_two_numbers (firs_number, second_number):
  print(firs_number + second_number)

sum_two_numbers(8,8)

def sum_two_numbers_return (firs_number, second_number):
  return firs_number + second_number

def print_name_default (name='Hola',surname='Prueba'):
  print(f'Nombre: {name} Apellido: {surname}')
  
print_name_default()
print_name_default('Brenda','Veramendi')