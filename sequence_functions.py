fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]


nums = [800,80,1000,32,255,400,5,5000]

print(len(fruits), min(fruits), max(fruits))
print(sorted(fruits))
print()

print(len(nums), min(nums), max(nums), sorted(nums), sum(nums))
print()

s = ['dog', 'bites', 'man']
for word in reversed(s):
    print(word)
print()

rev = reversed(s)
print(rev)
print("A:")
for word in rev:
    print(word)
print("B:")
for word in rev:
    print(word)
print()

states = ['TX', 'TX', 'NC', 'IL']
cities = ['Plano', 'Dallas', 'Raleigh', 'Chicago']

places = zip(cities, states)
# print(list(places))
for city, state in places:
    print(f"{city}, {state}")

places = zip(cities, states)
print(places, type(places))
print(list(places))
print()

print(cities)
for i, city in enumerate(cities):
    if i != 2:
        print(i, city)

print(list(enumerate(cities)))
print()

print("abc" + "def")
print(['a', 'b', 'c'] + ['d', 'e', 'f'])
print()

print('-' * 60)
print([True] * 10)
print((None,) * 8)
print("Badger! " * 25)

for fruit in fruits[::2]:
    print(fruit, end=' ')
print("\n")

for i in range(10):
    print("Badger! ")

print(list(range(10)))
# range(STOP)   range(START, STOP)  range(START, STOP, STEP)

for i in range(5, 101, 5):
    print(i, end=' ')
print("\n")







