def show_stars():
    num = 2
    def inside_function():
        print('stars'*num)

    return inside_function

returned_function_name = show_stars()

returned_function_name()