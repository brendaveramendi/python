#Loops
#While

my_condition = 0

while my_condition < 0:
  print(my_condition)
  my_condition +=2
else: 
  print('Es mayor que 10')
  
while my_condition < 20:
  my_condition+=1
  if my_condition == 15:
    print('Mi condicion es 15')
    #rompe la iteracion
    break
  print(my_condition)
  
my_list = [1,2,3,4,5,6,7,8,9,10]
my_set = {0,1,2,3}
my_other_dict = {'Nombre':'Brenda', 'Apellido':'Veramendi','DNI':34426962}
#For

for element in my_list:
  print(element)


for element in my_set:
  print(element)
  
for element in list (my_other_dict.values()):
  print(element)
