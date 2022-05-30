coins = [1, 2, 5, 10, 20, 50, 100, 200]
target = 200
ways = {}
ways[0] = 1

for coin in coins:
    for value in range(coin, target + 1):
        if value not in ways:
            ways[value] = 1
        elif (value - coin) in ways:
            ways[value] += ways[value - coin]
        

print(ways[target])
