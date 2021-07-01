counts = {}

with open('DATA/breakfast.txt') as breakfast_in:
    for raw_line in breakfast_in:
        food = raw_line.rstrip()

        if food not in counts:
            counts[food] = 0

        counts[food] += 1   # counts[food] = counts[food] + 1

def by_value(e):
    return -e[1], e[0]

sorted_counts = sorted(counts.items(), key=by_value)

for food_item, count in sorted_counts:
    print(food_item, count)


