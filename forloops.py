# for x in 'HELLO':
#   print(x)

# arr = ['Choi Seungcheol', 'Jeon Wonwoo', 'Kim Mingyu', 'Choi Hansol']
# for y in arr:
#   print(y)


my_dictionary = {
  'name': 'Choi Seungcheol',
  'nationality': 'South Korea',
  'birthdate': 'August, 8th 1995',
  'unit': ['HipHop', 'Leader']
}

for el in my_dictionary:
  print(el + ': ' + my_dictionary[el])
  if el == 'birthdate':
    break