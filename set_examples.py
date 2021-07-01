c1 = ['red', 'purple', 'pink', 'green', 'pink', 'brown', 'orange', 'yellow']
c2 = ['yellow', 'red', 'red', 'red', 'green', 'black', 'blue', 'pink']

set1 = set(c1)
set2 = set(c2)
set1.add('ecru')
set2.add('mauve')
set2.add('mauve')
set2.add('mauve')
print(set1)
print(set2)

print("Common to both:", set1 & set2)  # intersection
print("Only in one:", set1 ^ set2)     # xor
print("In either one:", set1 | set2)   # union
print("Only set1:", set1 - set2)
print("Only set2:", set2 - set1)

set1.discard('purple')
set2.discard('lavender')




