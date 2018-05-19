from random import randint

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

new_list = [item for item in set(a) if item in b]
print(new_list)

# Extra 1 & 2
a = [randint(0, 50) for _ in range(0, 20)]
b = [randint(0, 50) for _ in range(0, 40)]
new_list = [item for item in set(a) if item in b]
print(new_list)
