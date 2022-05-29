for i in range(1, 101):
    sum_of_squares = sum(x ** 2 for x in range(1, i + 1))
    square_of_sums = sum(range(1, i + 1)) ** 2
    print(f"{i}. {square_of_sums} - {sum_of_squares} = {square_of_sums - sum_of_squares}")
