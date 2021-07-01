import pprint

knight_data = {}

with open('DATA/knights.txt') as knights_in:
    for raw_line in knights_in:
        knight_record = raw_line.rstrip()
        name, title, color, quest, comment = knight_record.split(':')
        knight_data[name] = {
            "title": title,
            "color": color,
            "quest": quest,
            "comment": comment,
        }

pprint.pprint(knight_data, sort_dicts=False)
print()

for name, data in knight_data.items():
    print(data['title'], name)
print()

print(knight_data['Gawain']['title'], '\n')
print(knight_data['Bedevere'])

# dict_list = list(knight_data.items())
# print(dict_list)
# print(dict_list[2])

