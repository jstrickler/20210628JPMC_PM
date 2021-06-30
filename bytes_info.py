a = "40\u00B0 C\n"
print(a, len(a))

b = b"abc"
print(b)
print(a[0], b[0])

x = "48\u00B0 C"
print(x, len(x))
y = x.encode()
print(y, len(y))

z = y.decode()
print(z)
