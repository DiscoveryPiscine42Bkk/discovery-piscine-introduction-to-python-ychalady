array = [2, 8, 9, 48, 8, 22, -12, 2]
print(array)
transformed = {x + 2 for x in set(array)}
filtered = {x for x in transformed if x > 9}
print(filtered)