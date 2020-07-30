import converters
from shoppingCart import find_max


print(converters.kg_to_lb(100))
numbers = [10,15,50,52,20]
# max = find_max(numbers)  it a bad practice as changing the meaning of a built in function
maximum = find_max(numbers)
print(maximum)
