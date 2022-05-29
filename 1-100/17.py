from re import L
import inflect

eng = inflect.engine()

sum_letters = 0
for i in range(1, 1001):
    number = eng.number_to_words(i)
    letters = len(number.replace(' ', '').replace('-', ''))
    sum_letters += letters
    print(i, letters, number.replace(' ', '').replace('-', ''))
    
print(sum_letters)
