#Tuplas
#Inmutables
my_tuple = tuple()
my_other_tuple=()

my_tuple = (20,1.59,'Brenda','Veramendi','Veramendi')
print(my_tuple)

print(my_tuple.count('Veramendi'))
print(my_tuple.index('Veramendi'))
#Es inmutable
my_tuple[1] = 1.64
print(my_tuple)