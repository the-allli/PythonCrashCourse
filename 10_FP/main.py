# Lambda function to calculate the square of a number
square = lambda x: x * x
print(square(5))  # 25

# Map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x*x, nums))
print(squared)  # [1,4,9,16]

# Filter
nums = [1,2,3,4,5]
even = list(filter(lambda x: x % 2 == 0, nums))
print(even)  # [2,4]

# Reduce
from functools import reduce
nums = [1,2,3,4]
product = reduce(lambda x,y: x*y, nums)
print(product)  # 24

# Decorators
def my_decorator(func):
    def wrapper():
        print("Before")
        func()
        print("After")
    return wrapper
@my_decorator
def greet():
    print("Hello!")
greet()
# Before
# Hello!
# After

# Generators & yield

squares = (x*x for x in range(5))
for s in squares:
    print(s)
# Generator function to count up to n
def count_up_to(n):
    count = 1
    while count <= n:
        yield count
        count += 1
for num in count_up_to(5):
    print(num)

# itertools module
import itertools
# count(start, step)
for i in itertools.count(10, 2):
    if i > 20:
        break
    print(i)  # 10,12,14,16,18,20
# cycle()
count = 0
for item in itertools.cycle(['A', 'B', 'C']):
    print(item)
    count += 1
    if count == 6:
        break  # A,B,C,A,B,C
# accumulate()
from operator import mul
print(list(itertools.accumulate([1,2,3,4])))  # sums: [1,3,6,10]
print(list(itertools.accumulate([1,2,3,4], mul)))  # products: [1,2,6,24]
# chain()
for x in itertools.chain([1,2], ['a','b']):
    print(x)  # 1,2,a,b
# combinations
for combo in itertools.combinations([1,2,3], 2):
    print(combo)  # (1,2),(1,3),(2,3)
# permutations
for perm in itertools.permutations([1,2,3], 2):
    print(perm)  # (1,2),(1,3),(2,1),(2,3),(3,1),(3,2)  
