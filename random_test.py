__author__ = 'yingminzhou'

import random

names = ["Mary","Isla","Sam"]

# unfunctional one
code_names = ['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']

for i in range(len(names)):
    names[i] = random.choice(code_names)

print(names)


#functional one
secret_names = map(lambda x: random.choice(['Mr. Pink', 'Mr. Orange', 'Mr. Blonde']),names)

print(names)