d1 = dict()
d2 = {'TX': 'Austin', 'NC': 'Raleigh', 'NY': 'Albany', 'IL': 'Springfield'}
d3 = {}  # empty dict

d4 = {2:500, 1883: 9, 483: 5, 12333: 6}


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

print(airports['OAK'])
print(airports['RDU'])
print(airports.get('YCC'))
print(airports.get('JFK'))
print(airports.get('JFK', 'NOT FOUND'))
# print(airports['JFK'])  # raises exception
airports['DFW'] = "Dallas/Ft. Worth"
print(airports, '\n')

# airports_by_name = {name:abbr for abbr, name in airports.items()}
# print(airports_by_name, '\n')
for abbr in 'RDU', 'LAX', 'ELM', 'DFW', 'YCC':
    print(abbr, abbr in airports)
print()

print(airports.keys()) # generator!
print(airports.values())  # generator!
print()

for abbr, name in sorted(airports.items()):
    print(abbr, name)
print()

print(airports.items(), '\n')

def by_value(e):
    return e[1], e[0]

for abbr, name in sorted(airports.items(), key=by_value):
    print(abbr, name)
print()

del airports['OAK']
print(airports, '\n')










