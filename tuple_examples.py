"""
struct person {
    char *fname;
    char *lname;
    int age;
}
"""

person = "Bill", "Gates", "Microsoft", "1955-10-24"

print(person[0], person[1])

# UNPACK!!

first_name, last_name, product, dob = person  # first_name = person[0], last_name = person[1]
last_name, product = person[1:3]

# var1, var2, ...  = ITERABLE

print(first_name, last_name)


people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
]

# for person in people:
#     first_name, last_name, product, dob = person
#     print(first_name, dob)
# print()

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product)
print()



