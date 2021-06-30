list1 = list()   # new, empty, list
list2 = ['red', 'purple', 'orange', 'blue']
list3 = []

print(list1, list2, list3)

cities = ['Plano', 'Durham', 'Seattle', 'New York', 'Chicago', 'London']
print(cities)
print(cities[0], cities[3], cities[-1])
cities.append("Portland")
cities.append("Virginia Beach")
print(cities)
cities.insert(0, "Pittsburgh")
cities.insert(4, "Albany")
print(cities)

more_cities = ["Annapolis", "Hartford", "Burlington"]
cities.extend(more_cities)
print(cities)

#  add elements:
#  LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)

del cities[3]
print(cities)

city = cities.pop()
print(city)
print(cities)

city = cities.pop()
print(city)
print(cities)

city = cities.pop(3)
print(city)
print(cities)

cities.remove('Chicago')
cities.remove("London")
print(cities)









