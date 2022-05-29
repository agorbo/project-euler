n = 1000

multiples = set()

for i in range(5, n, 5):
    multiples.add(i)

for i in range(3, n, 3):
    multiples.add(i)

print(sum(multiples))