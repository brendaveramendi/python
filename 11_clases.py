#Clases

#El nombre de las clases
#es con camelCase
class MyPerson:
  #pass para q ejecute nada
  #no tire error
  pass

class Person:
  #Creacion de constructor
  #Sienpre llama a constructor
  #self siempre se debe llamar 
  #hace referencia asi mismo
  def __init__(self,name,surname, alias):
    self.fullname = f'{name} {surname} {alias}' #Prop Publica
    self._name = name #Propiedad privada
  
  def get_name(self):
    return self._name
  
  def walk(self):
    print (f'{self.fullname } esta caminando')
  
my_person = Person('Brenda','Veramendi', 'brendaveramendi')
print(my_person.fullname)
my_person.walk()
my_person.fullname = 'other other loco'
print(my_person.fullname)