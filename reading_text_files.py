mary_in = open('DATA/mary.txt')
# process file ...
mary_in.close()

with open('DATA/mary.txt') as mary_in:
    print("file opened...")
print()

with open('DATA/mary.txt') as mary_in:
    for raw_line in mary_in:  # file obj is generator of lines in the file (calls obj.readline() )
        line = raw_line.rstrip()   # remove \n from line
        print(line)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    contents = mary_in.read()  # read entire file into one string
    print("normal:")
    print(contents)
    print("raw:")
    print(repr(contents))
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_with_nl = mary_in.readlines()
    print(all_lines_with_nl)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    all_lines_without_nl = mary_in.read().splitlines()
    print(all_lines_without_nl)
print("-" * 60)

with open('DATA/mary.txt') as mary_in:
    first_chunk = mary_in.read(10)
    second_chunk = mary_in.read(20)
    # mary_in.tell()  get file pointer location
    # mary_in.seek(pos) set file pointer location
    print(first_chunk)
    print(second_chunk)
print("-" * 60)

import os
print(os.path.getsize('DATA/mary.txt'))


letter = 's'
with open('DATA/words.txt') as words_in:
    count = 0
    for line in words_in:
        if line.startswith(letter):
            count += 1
print(f"{count} words start with {letter}")

target = 'sam'
with open('DATA/words.txt') as words_in:
    with open('sam_words.txt', "w") as sam_out:
        for line in words_in:
            if target in line:
                sam_out.write(line)

print(os.path.exists('DATA/words.txt'))


fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date"]

with open('fruits.txt', 'w') as fruits_out:
    for fruit in sorted(fruits):
        fruits_out.write(fruit.capitalize() + '\n')

# with open(...) as file_obj:
#     for line_number, line_text in enumerate(file_obj):