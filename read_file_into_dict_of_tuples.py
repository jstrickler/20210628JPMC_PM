import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        knight_record = raw_line.rstrip()
        name, title, color, quest, comment = knight_record.split(':')
        knight_data[name] = title, color, quest, comment

pprint.pprint(knight_data, sort_dicts=False)
print()

for name, data in knight_data.items():
    print(data[0], name)
print()

print(knight_data['Gawain'][1], '\n')
print(knight_data['Bedevere'])


