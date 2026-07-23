array_in_question = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def find(array, input):
    if input not in array:
        raise ValueError("value not in array")
    
    index = len(array) / 2
    pass