__author__ = 'yingminzjou'

from functools import reduce

sum = reduce(lambda a, x:a + x,[0,1,2,3,4])

print(sum)
