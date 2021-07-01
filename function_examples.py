
def get_message():
    return "Hello, JPMC world"

message = get_message()
print(message)

def hello():
    m = get_message()
    print(m)


result = hello()
print(result)

import typing as T

def dosomething(values: T.Iterable, colors: T.List[str]) -> float:
    pass



# type hints for the win!
def count_lines(file_name: str) -> int:
    line_count = 0
    with open(file_name) as file_in:
        for line in file_in:
            line_count += 1
    return line_count

for file_path in 'DATA/alice.txt', 'DATA/mary.txt', 'DATA/parrot.txt':
    print(file_path, count_lines(file_path))
print()

# x = count_lines(1234)


def spam(a, b, *p):
    print(p, '\n')

spam(1, 2)
spam(1, 2, 3)
spam('this', 'is', 'only', 'a', 'test', 'wombat', 'zebra cobra')


def greet(greeting="Hello"):
    print(f"{greeting}, world")

greet()
greet("Howdy")
greet("'sup?")

def doit(wombat):
    result = wombat()
    return result

def a():
    return 5

def b():
    return 42

print(doit(a))
print(doit(b))

print(type(doit), type(a), type(b))


x = 5

x = doit

m = x



def make_card_deck(back_image, *args, use_jokers=False):
    print(back_image, use_jokers)

make_card_deck('foo.jpg')
make_card_deck('bar.png', use_jokers=True)
# make_card_deck('blah.tiff', True)





















