import math

fact100 = math.factorial(100)
fact100_str = str(fact100)

print(sum([int(i) for i in list(fact100_str)]))
