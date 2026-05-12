def print_numbers(*args):
    for num in args:
        print(num)

print_numbers(1, 2, 3, 4)


def print_info(*args, **kwargs):
    for value in args:
        print(value)

    for key, value in kwargs.items():
        print(f"{key}: {value}")


print_info("Amit", "Alic", ages=(60, 70))
