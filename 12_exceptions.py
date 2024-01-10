#Exception

numberOne= 5
numberTwo = 1
snumberTwo = '2'

try:
  print(numberOne + numberTwo)
except ValueError as error: 
  print(error)
except Exception as my_random_error_name:
  print(my_random_error_name)

try:
  print(numberOne + numberTwo)
except: 
  print('Se ha producido un error')
else:
  #Se ejecuta si no se produce un error
  print('Continua')
finally:
  #Se ejecuta siempre
  print('Ejec Continua')