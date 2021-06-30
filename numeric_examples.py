
i1 = 12345
i2 = 1_234_815_996
i3 = 12_34_56_78
i4 = 823092736092736453495874985710934587130945801394851039457139045710934750193745019374509173409173405971309457

# int float complex bool

print(i1, i2, i3)

f1 = 123.456
f2 = 123_456.583_931

print(f1, f2)

import numpy as np
a = np.array([5.0, 10, 98]) # , dtype=np.float16)
print(a)
print(a.dtype, '\n')

# lambda

a = 19
b = 7

print(a + b)
print(a - b)
print(a * b)
print(a / b)   # "true" division  -> float
print(a // b)  # floored division -> whole number
print(b // a)
print(a // -b)
print(a ** b)  # exponentiation
print(a % b)   # modulo (remainder)

m = 10
m += 15   # m = m + 15
m *= 3    # m = m * 3
m /= 5    # m = m / 5
print(m, '\n')

i = "123"
j = 456
# print(i + j)
# print(j + i)
print(int(i) + j)
print(i + str(j))
print()

# print(i * j, '\n')
print("Here's the answer" * 3)
flags = [True] * 10
print(flags)

# sequence
#  list tuple str bytes

#  list(iterable)   tuple(iterable) str(anything) bytes(iterable of numbers)  bool(anything)

print("-" * 60)

print([1, 2, 3] * 8)

x = [[1, 2, 3,], [3, 4, 5]]

print(x * 3)

x = ['a', 'b']
print(x * 3)




























