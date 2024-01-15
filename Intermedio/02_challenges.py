"""
El famosos Fizz buzz
Escribe un programa que muestre por consola
con un print los numeros del 1 al 100 (con salto de linea cada numero)
Multiplos de 3 por la pañabra fizz
Multiplos de 5 por la pañabra "buzz"
Multiplos de 3 y 5 a la vez por la
palabra "fizzbuzz"  
"""
def fizzbuzz():
  lista_buf = []
  for index in range(1,101):
   if index % 3 == 0 and index % 5 ==0:
    print (index)
   elif index % 3:
    print (index)
   elif index % 5:
    print (index)
   else:
    print(lista_buf)
  
     
fizzbuzz() 


"""
¿ES UN ANAGRAMA?
Escribe una función que reciba dos palabras (String) y retorne
verdadero o falso (Bool) según sean o no anagramas.
- Un Anagrama consiste en formar una palabra reordenando TODAS
  las letras de otra palabra inicial.
- NO hace falta comprobar que ambas palabras existan.
- Dos palabras exactamente iguales no son anagrama.
"""
def is_anagram(word_one, word_two):
  
  return sorted(word_one.lower()) == sorted(word_two.lower())


print(is_anagram("amor", "roma"))

"""
LA SUCESIÓN DE FIBONACCI
Escribe un programa que imprima los 50 primeros números de la sucesión
de Fibonacci empezando en 0.
- La serie Fibonacci se compone por una sucesión de números en
  la que el siguiente siempre es la suma de los dos anteriores.
  0, 1, 1, 2, 3, 5, 8, 13...
"""

def sucesión_fibonacci():
  number_one = 0
  number_two = 1
 
  for index in range(1,51):
    print(number_one)
    fibo = number_one + number_two
    number_one = number_two
    number_two = fibo  
    
sucesión_fibonacci()

"""
¿ES UN NÚMERO PRIMO?
Escribe un programa que se encargue de comprobar si un número es o no primo.
Hecho esto, imprime los números primos entre 1 y 100.
"""
print("----------------------")

def primo():
  for index in range(2,101):
    flag = True
    for i in range(2,index//2+1):
      if(index%i==0):
        flag = False
        break
    if flag:
     print(index)
       
    

print("*********************")        
primo()
   
"""
INVIRTIENDO CADENAS
Crea un programa que invierta el orden de una cadena de texto
sin usar funciones propias del lenguaje que lo hagan de forma automática.
- Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

def reverse_string(word_reverse):
  reverse =""
  tex_len = len(word_reverse)
  for i in range (0,tex_len):
    reverse+=word_reverse[tex_len-i-1]
  print(reverse)
    
reverse_string("Hola mundo")