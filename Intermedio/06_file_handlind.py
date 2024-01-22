#Files Handling
import os
text_file=open("./file_text.txt","r+") #Leer y escribir
#print(text_file.read())

#print(text_file.readline(2))

print(text_file.readline())

for line in text_file.readlines():
  print(line)

text_file.close()
#text_file.write("\n Me gusta JavaScript")

#Json

import json

json_file = open("./my_file.json","w+")

json_test = {
  "name": "Brenda",
  "surname": "Veramendi",
  "lenguage": "Python",
  "website":"https://github.com/brendaveramendi?tab=overview&from=2024-01-01&to=2024-01-16"
}
#Lo que se va a gregar el fichero y la identacion
json.dump(json_test, json_file,indent=2)

json_file.close()

with open("./my_file.json") as my_other_file:
  for line in my_other_file.readlines():
    print(line)
    
json_dict = json.load(open("./my_file.json"))
print(json_dict)
print(type(json_dict))
print(json_dict["name"])

#Csv file

import csv