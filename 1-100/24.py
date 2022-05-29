from itertools import permutations

for i, permutation in enumerate(permutations('0123456789')):
    if i == 999999:
        print(permutation)
        break
