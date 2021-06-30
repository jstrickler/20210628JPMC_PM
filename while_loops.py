i = 0
while i < 5:
    print(i)
    i += 1
print("-" * 60)

while True:
    state = input("Enter your state (q to quit): ")
    if state == 'q':
        break
    if state == '':
        print("Please enter 2-letter state abbreviation")
    elif len(state) != 2:
        print("Entry must be 2 letters")
    elif not state.isalpha():
        print("Only letters are allowed")
    elif not state.isupper():
        print("Abbreviation must be upper case")
    else:
        print(f"{state} is a nice state")
