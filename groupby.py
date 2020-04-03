from itertools import groupby

numbers = [1,2,2,2,3,1,1]

numbers = list(dict.fromkeys(numbers))
print(numbers)