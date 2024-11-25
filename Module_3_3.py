def print_params(a=1, b='строка', c=True):
    print(a, b, c)

values_list = [24, True, "Hello"]
values_dict = {'a' : 4, 'b' : 3, 'c' : 2}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = ["Say", 18]
print_params(*values_list_2, c = 42)