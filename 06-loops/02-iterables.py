numbers = [1,2,3,4,5]

# Iterables: Iterables, listas, diciconarions, set, tuplas
# for number in numbers:
#     print(number)

iterator = iter(numbers)
# print(iterator)
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))
# print(next(iterator))

user = {
    'name':'John',
    'age':25,
    'can_swim': False
}

for key, value in user.items():
    print(key, value)

# for item in user.items():
#     key, value = item
#     print(key, value)