import re


my_string = "Esta es la leccion numero 7 : Expresiones Regulares leccion"
my_other_string = "Esta es la leccion numero 6 : Manejo de Ficheros"

#re.I para ignorar mayusculas
expression = re.match("esta es la leccion",my_string,re.I)

print(expression)
print(expression.span())

#Acceder al valor

start, end = expression.span()
print(start)
print(end)
print(my_string[start:end])

#search

search = re.search("leccion", my_string,re.I)
print(search)

#findall
#Encuentra todas las considencias

findall = re.findall("leccion", my_string, re.I)
print(findall)

#split
#Separa el contenido por el a}caracter que elijas
print(re.split(":",my_string))

#Sub
#sustituye ocurrencias

print(re.sub("leccion|Leccion","LECCIÓN",my_string))
print(re.sub("[L|l]eccion","LECCIÓN",my_string))
print(my_string)

#Patterns
#r inidca q es una expresion regular

pattern = r"[lL]eccion"
print("---->",re.findall(pattern, my_string))


pattern = r"[0-9]"
print(re.search(pattern, my_string))

#Solo numeros
pattern = r"\d"
print(re.findall(pattern, my_string))

#Solo letras
pattern = r"\D"
print(re.findall(pattern, my_string))

pattern = r"[l].*"
print(re.findall(pattern, my_string))

email = "brenda@gmail.com"
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z-.]+$"
print(re.match(pattern, email))
print(re.search(pattern, email))
print(re.findall(pattern, email))

email = "brenda@gmail.com.mx"
print(re.findall(pattern, email))






