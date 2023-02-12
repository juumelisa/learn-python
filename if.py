a = 5
b = 3

# if a > b:
#   print(str(a) + ' greater than ' + str(b))
# elif a == b:
#   print(str(a) + ' same as ' + str(b))
# else:
#   print(str(b) + ' greater than ' + str(a))

if a > b or b > a:
  print('NOT EQUAL')
else:
  print('EQUAL')

if type(a) == str:
  print('STRING')
elif type(a) == int:
  print('INT')
else:
  print('I DONT KNOW')