# countries = ['Indonesia', 'Malaysia', 'Singapore', 'Australia', 'South Korea']
# print(countries[1:4])
# print(type(countries))
# print(countries[-1])
# print(len(countries))

list1 = ['apple', 'banana', 'mango', 'avocado']
list2 = [1, 2, 3, 4]
list1.extend(list2)
print(list1)
list1.append('orange')
print(list1)

list1.insert(1, 'cherry')
print(list1)

list2.clear()
print(list2)

print(list1.index('avocado'))