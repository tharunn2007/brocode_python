import random

my_dict = {'a': 1, 'b': 2, 'c': 3}

# Random key
random_key = random.choice(list(my_dict.keys()))
print(f"Random key: {random_key}")

# Random value
random_value = random.choice(list(my_dict.values()))
print(f"Random value: {random_value}")

# Random key-value pair (as a tuple)
random_pair = random.choice(list(my_dict.items()))
print(f"Random key-value pair: {random_pair}")





