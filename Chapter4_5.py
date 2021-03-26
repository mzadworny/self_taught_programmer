def converter(x):
  '''
  Put in a number and get a float.
  In case o wrong input, ex. text give a error text.
  '''
  try:
    x = float(x)
    return x 
  except ValueError:
    print("Enter a number, not a string")

y = input("Give me a number. ")
x = converter(y)
print(x)
