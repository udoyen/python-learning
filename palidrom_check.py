import datetime
from functools import wraps

def validate_decorator(validator, if_invalid=None):
    def decorator(function):
        @wraps(function)
        def wrapper(*args):
            if validator(*args):
                return function(*args)
            else:
                return if_invalid
        return wrapper
    return decorator

def spent_time_logging_decorator(function):
    @wraps(function)
    def wrapper(*args):
        start = datetime.datetime.now()
        result = function(*args)
        end = datetime.datetime.now()
        spent_time = end - start
        print("spent {} microseconds in {} with arguments {}. Result was: {}".format(spent_time.microseconds, function.__name__, str(args), result))
        return result
    return wrapper


def cache_decorator(function):
    cache = {}
    
    @wraps(function)
    def wrapper(*args):
        hashed_arguments = hash(str(args))
        if hashed_arguments not in cache:
            print("result for args {} was not found in cache...".format(str(args)))
            cache[hashed_arguments] = function(*args)
        return cache[hashed_arguments]
    return wrapper

def is_palindrome(strin_value):
    char_array = list(strin_value)
    size = len(char_array)
    half_size = int(size / 2)
    for i in range(0, half_size):
        if char_array[i] != char_array[size - i - 1]:
            return False
    return True

def should_not_contain_spaces(*args):
    return False not in map(lambda x: " " not in str(x), args)


@spent_time_logging_decorator
@validate_decorator(should_not_contain_spaces, "input shouldn't contain spaces.")
@cache_decorator
def convert_to_palindrome(v):
    def action(string_value, chars):
        chars_to_append = list(string_value)[0:chars]
        chars_to_append.reverse()
        new_value = string_value + "".join(chars_to_append)
        if not is_palindrome(new_value):
            new_value = action(string_value, chars + 1)
        return new_value
    return action(v, 0)

user_input = input("string to convert to palindrome (exit to terminate program): ")

while user_input != "exit":
    print(str(convert_to_palindrome(user_input)))
    user_input = input("string to check (exit to terminate program): ")
