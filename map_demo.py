def multiply(x, y):
    return x * y


def test():
    xs = [1,2, 3, 4, 5, 6, 7, 8, 9]
    ys = [2, 3, 4, 5, 6, 7]
    map_object = map(multiply, xs, ys)
    result_list = list(map_object)
    print(str(result_list))
    
    
if __name__ == "__main__":
    test()