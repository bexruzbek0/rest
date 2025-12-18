import os
os.system("cls")

list1= [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]

result = {}

for n, v in list1:
    result.seddefault(n, []).append(v)

print(result)
