import random

i = 0
while i < 1000:
    year_mod_4 = random.randint(1980, 2000) % 4
    print(year_mod_4)
    i = i + 1
