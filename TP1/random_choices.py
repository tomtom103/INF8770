import random
import string

dictionnary = list(string.octdigits)
weights = [0.5, 0.05, 0.05, 0.05, 0.05, 0.1, 0.1, 0.1]
print(len(dictionnary))
print(len(weights))
choices = random.choices(
    population=dictionnary,
    weights=weights,
    k=5000
)

print(''.join(choices[:100]))