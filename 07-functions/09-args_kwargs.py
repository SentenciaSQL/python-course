def big_function(*args, **kwargs):
    print(args)
    print(kwargs)
    total = 0

    for item in kwargs.values():
        total += item
        print(item)

    return sum(args) + total

print(big_function(1, 2, 3, num1=77, num2=88))