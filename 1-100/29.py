
limit = 100
seen = set()
for a in range(2, limit + 1):
    for b in range(2, limit + 1):
        seen.add(a ** b)

print(len(seen))
