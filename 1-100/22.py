import string

with open("22_input.txt") as file:
    name_list = sorted(file.read().strip('"').split('","'))

    total_score = 0
    for i, name in enumerate(name_list):
        name_sum = sum([string.ascii_uppercase.index(c) + 1 for c in name])
        name_score = name_sum * (i + 1)
        print(name, name_score)
        total_score += name_score

        if name == "COLIN":
            a = 1

    print(total_score)
