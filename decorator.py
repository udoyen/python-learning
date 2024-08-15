

# def decorator(function_to_decorate):
#     def wrapper(value):
#         print("you are calling {} with "{}" as parameter".format(function_to_decorate. ←-
#         __name__, value))
#         return function_to_decorate(value)
#     return wrapper

# def replace_commas_with_spaces(value):
#     return value.replace(",", " ")

# function_to_use = decorator(replace_commas_with_spaces)
# print(function_to_use("my,commas,will,be,replaces,with,spaces"))



from functools import wraps


def decorator(function_to_decorate):
    @wraps(function_to_decorate)
    def wrapper(value):
        print("you are calling {} with '{}' as parameter".format(function_to_decorate.__name__, value))
        return function_to_decorate(value)
    return wrapper


@decorator
def replace_commas_with_spaces(value):
    return value.replace(",", " ")


print(replace_commas_with_spaces.__name__)
print(replace_commas_with_spaces.__module__)
print(replace_commas_with_spaces.__doc__)
print(replace_commas_with_spaces("my,commas,will,be,replaces,with,spaces"))


