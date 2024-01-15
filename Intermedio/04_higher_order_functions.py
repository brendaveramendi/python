#Funciones de orden superior

def sum_one(value):
  return value +1

def sum_two_values_and_add_one(first_value, second_value):
  return sum_one(first_value + second_value)


print(sum_two_values_and_add_one(2,3))


def sum_two_values(first_value, second_value,f):
  return f(first_value+second_value)

print(sum_two_values(3,1,sum_one))

#Closure 
#retorna una funcion

def sum_ten(original_value):
  def add (value ):
    return value + 10 + original_value
  return add


add_closure = sum_ten(1)
print(add_closure(5))
print((sum_ten(5))(1))
print((sum_ten(5))(1))

# Map

numbers = [1,2,3,4,5,25]

def multiply_two(number):
  return number * 2

print(list(map(multiply_two,numbers)))
 
# Filter


def filter_greater_than_ten(number):
    if number > 10:
        return True
    return False


print(list(filter(filter_greater_than_ten, numbers)))
print(list(filter(lambda number: number > 10, numbers)))


# Reduce
#Se tiene que importar reduce
from functools import reduce
def sum_two_values(first_value, second_value):
    return first_value + second_value

reduce()
print(reduce(sum_two_values, numbers))


