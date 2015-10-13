__author__ = 'yingminzhou'

names = ['Mary', 'Isla', 'Sam']

#unfunctional one
for i in range(len(names)):
    names[i] = hash(names[i])

print(names)

#functional one
secret_name = map(hash,names)
print(names)

