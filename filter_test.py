__author__ = 'yingminzhou'

people = [{'name': 'Mary', 'height': 160},
          {'name': 'Isla', 'height': 80},
          {'name': 'Sam'}]
#unfunctional one
height_total = 0
height_count = 0

for person in people:
    if 'height' in person:
        height_total += person['height']
        height_count += 1

if height_count > 0:
    average_height = height_total / height_count
    print(average_height)


heights = list(map(lambda x: x['height'],filter(lambda x: 'height' in x,people)))

if len(heights)>0:
    from operator import add
    from functools import reduce
    average_height = reduce(add,heights)/len(heights)
    print(average_height)
