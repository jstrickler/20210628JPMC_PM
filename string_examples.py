s1 = "spam\n"
print(len(s1))
s2 = 'spam\n'
print(len(s2))
s3 = """spam\n"""
s4 = '''spam\n'''
s5 = r"spam\n"   # raw string -- backslash is not significant
print(s5, len(s5))


print("It's a Python thing")
print('It is a "Python" thing')

print("""It's a "Python" thing""")

insert_sql = """
insert into customers
(first_name, last_name)
values ("Bob", "Smith")
"""

