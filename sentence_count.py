__author__ = 'yingminzhou'

from functools import  reduce
sentences = ['Mary read a story to Sam and Isla.',
             'Isla cuddled Sam.'
             'Sam chortled.']

# unfunctional one
sam_count = 0

for sentence in sentences:
    sam_count += sentence.count('Sam')

print(sam_count)

# functional one
sam_count = reduce(lambda a, x: a + x.count('Sam'),sentences,0)

print(sam_count)
