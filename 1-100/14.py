biggest_collatz = 0
biggest_chain = 0

for i in range(1, 1 * 10**6):
    collatz = i
    chain_len = 1
    
    while collatz != 1:
        if collatz % 2 == 0:
            collatz /= 2
        else:
            collatz = collatz * 3 + 1
        chain_len += 1

    if chain_len > biggest_chain:
        biggest_chain = chain_len
        biggest_collatz = i
        print(i, chain_len)
