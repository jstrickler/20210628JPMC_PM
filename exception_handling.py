import sys

file_path = "DATA/wombats.txt"
try:
    with open(file_path) as file_in:
        for line in file_in:
            print(line)
except FileNotFoundError as err:
    print(err)
except (PermissionError, IsADirectoryError) as err:
    print(err)
print()

values = [0, 5, 0, 18, 12, 6, 0]
try:
    print(values[19])
except IndexError as err:
    print(err)
print()

for value in values:
    try:
        result = 22 / value
    except ZeroDivisionError as err:
        print(err)
    else:
        print(result)
print()


import sqlite3
conn = None
try:
    conn = sqlite3.connect('mydata.db')
except sqlite3.DatabaseError as err:
    print(err)
    sys.exit()
else:
    cursor = conn.cursor()
#    cursor.execute("select foo from bar")
finally:
    if conn is not None:
        conn.close()

try:
    x = 1 / 0
except Exception as err:
    print(err)




print("All done.")

