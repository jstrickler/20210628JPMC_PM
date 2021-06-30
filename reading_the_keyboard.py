state = input("In what state do you live? ")
print(f"{state} is a nice state")

raw_shrimp = input("How many shrimp can you eat? ")
try:
    shrimp = int(raw_shrimp)
except Exception as err:
    print(err)
else:
    print("shrimp " * shrimp)
