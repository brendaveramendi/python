#Lambdas

#Sin nombre, en una variable
sum_two_values = lambda first_value, second_value: first_value + second_value

print(sum_two_values(2,3))

def sum_values(value):
  return  lambda first_value, second_value: first_value + second_value * value

print (sum_values(2)(2,3))

