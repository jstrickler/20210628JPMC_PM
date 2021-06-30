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
cities.insert(3, 'Chicago')
cities.insert(0, 'London')
print(cities)

print(cities[0])
print(cities[8])
print(cities[-1])
print(cities[-3])

#    cities[START:STOP/SENTINEL]
print("all cities:", cities)
print(cities[0:4])
print(cities[4:7])
print(cities[:4])
print(cities[4:])
print(cities[:])
print(cities[-3:])
print(cities[:-1]) # all but the last
print(cities[1:-1]) # skip first and last
print(cities[-1:1])
print(cities[2:22])
print(cities[93902:39023230])

s = "Spaghetti Monster"
print(s[1:4])
print(s[-7:])
print(s[5:9])
print(s[:9])

from copy import deepcopy
spam = [[1, 2, 3], [4, 5, 6]]
a = spam            # alias
b = list(spam)      # shallow copy
c = deepcopy(spam)  # deep copy
a.append("wombat")
print(spam, a, b, c)
b[0].append('JPMC')
print(spam, a, b, c)

# for VAR in ITERABLE:
#    ...

for city in cities:
    # city = cities[0]
    # then city = cities[1]
    # then city = cities[2]
    #  etc etc
    print(city)

s = "spam"
for c in s:
    print(c)

s_letters = list(s)
print(s_letters, '\n')

# iterables
# sequence: str bytes list tuple
# mapping: dict set
# virtual: generator  MAGIC!!

#   x[start:stop:step]
for city in cities[-1::-1]:  # reverse iteration
    print(city)
print()

for city in reversed(cities):
    print(city.upper())
print()

# for (i = 0; i < 10; i++) {
#
# }





















