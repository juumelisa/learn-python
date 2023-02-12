try:
  x = int(input('Input an integer: '))
  print(x)
except ValueError:
  print(str(ValueError))
else:
  print("Nothing wrong")