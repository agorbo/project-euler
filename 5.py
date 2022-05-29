from sympy.ntheory import factorint

biggest_factorization = dict()
for i in range(1, 21):
    i_factorization = factorint(i)
    for k, v in i_factorization.items():
        if k not in biggest_factorization or v > biggest_factorization[k]:
            biggest_factorization[k] = v
    
    biggest = 1
    for k, v in biggest_factorization.items():
        biggest *= k ** v

    print(i, biggest)
