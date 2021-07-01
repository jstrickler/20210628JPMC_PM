import os
from financials.credit import johnlib, johnlib as jl

# import johnlib
# import johnlib as jl


def show_animals():
    print("not the original...")

johnlib.show_animals = show_animals

johnlib.spam()
johnlib.ham()

print(johnlib.MAX_TRIES)
print(johnlib.ANIMALS[1])

jl.spam()

johnlib.ANIMALS.append('kangaroo')

johnlib.show_animals()

print(os.getenv('PYTHONPATH'))

# 1. current folder
# 2. folders in PYTHONPATH env variable
# 3. folders under installation folder for Python (standard library plus installed mods from PyPi)

johnlib._toast()  # NAUGHTY!!

