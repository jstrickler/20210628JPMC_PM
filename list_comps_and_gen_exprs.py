fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

f0 = []  # create new list
for f in fruits:
    f0.append(f.upper())    # result.append(EXPR)
print("f0:", f0, "\n")

# result = [EXPR for VAR in ITERABLE]
# result = [EXPR for VAR in ITERABLE if CONDITION]
f1 = [f.upper() for f in fruits]
print("f1:", f1, "\n")

def cleanup(s):
    return s.strip().upper()[:3]

f2 = [cleanup(f) for f in fruits]
print("f2:", f2, "\n")

f3 = [f.strip().upper()[:3] for f in fruits]
print("f3:", f3, "\n")

f4 = [f.upper() for f in fruits if f.startswith('p')]
print("f4:", f4, "\n")

f5 = [f for f in fruits if f.startswith('p')]
print("f5:", f5, "\n")

all_foods = ['spam', 'spam', 'ham', 'bacon', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'spam']
good_food = [food for food in all_foods if food != 'spam']
print("good_food:", good_food, "\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

last_names = [(p[0], p[1]) for p in people]
print("last_names:", last_names, "\n")

airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

canadian = [city for abbr, city in airports.items() if abbr.startswith('Y')]
print("canadian:", canadian)

fruit_gen = (f.upper() for f in fruits)
print(fruit_gen)
for fruit in fruit_gen:
    print(fruit)
print()

