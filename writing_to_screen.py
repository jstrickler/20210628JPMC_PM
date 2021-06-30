a = "apple"
b = 123
c = 48.382

result = "a" * 3
print(result)
print(repr(result))
print(["a"] * 3, '\n')

print(a, b, c)
print()
separator = ' '
end = '\n'
print(str(a) + separator + str(b) + separator + str(c) + end)
print("aaa")
print("bbb")
print("ccc")
print(a, b, c, 42, "wombat", sep="/")
print(a, b, c, sep="#")
print(a, b, c, sep=", ")
print(a, b, c, sep="")
print(a, b, c, sep=separator)

print("aaa", end='#')
print("bbb", end="%")
print("ccc")

print(a, b, c, sep="<=>", end="END")
print("More to come")

print("Value is", c)

print("Fruit is", a, "value is", c)
print("Fruit is {}, value is {}".format(a, c))
print("Fruit is {}, value is {}".format(c, a))

print("Value is {:.1f}".format(c))

v = "Value is {:.1f}".format(c)
print(v)

fmt = "Value is {:.2f}"
print(fmt.format(c))

print(f"Fruit is {a}, value is {c}")   # 3.6+
print("Fruit is {}, value is {}".format(a, c))
print("2 + 2 is {}".format(2 + 2))
print(f"2 + 2 is {2 + 2}")

v = f"Value is {c:.2f}"










