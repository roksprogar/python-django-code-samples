# https://docs.python.org/3/tutorial/datastructures.html

# 5. Data Structures

# 5.3. Tuples and Sequences

# Using named tuples instead of classes
from collections import namedtuple
Car = namedtuple('Car', 'color mileage')

# Works like a class
my_car = Car('red', 3812.4)
print(my_car.color)
print(my_car.mileage)

# String representation
print(my_car)

# But (named)tuples are immutable
try:
    my_car.color = 'black'
except AttributeError:
    print('Can\' change a named tuple!')

# 5.5. Dictionaries

# Sort a dictionary by value
import operator
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

# Using sorted
print(sorted(xs.items(), key=lambda x: x[1]))

# Using operator
print(sorted(xs.items(), key=operator.itemgetter(1)))
