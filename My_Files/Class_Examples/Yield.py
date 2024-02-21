def fun_generator():
    yield "Hello 1 World!"
    yield "Hello 2 World!"
    yield "Hello 3 World!"


obj = fun_generator()

print(next(obj))
print(next(obj))
print(next(obj))

# for each in fun_generator():
#     print(each)

test_list = [1, 4, 5, 6, 7]


def print_even(some_list):
    for num in some_list:
        if num % 2 == 0:
            yield num


print("Even numbers:")
for num in print_even(test_list):
    print(num, end=' ')
