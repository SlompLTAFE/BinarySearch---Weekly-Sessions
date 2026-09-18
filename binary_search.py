array_in_question = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


def find(array, input):
    if input not in array:
        raise ValueError("value not in array")

    left, right = 0, len(array) - 1

    while left <= right:
        middle = (left + right) // 2

        if array[middle] == input:
            return middle
        elif array[middle] < input:
            left = middle + 1
        elif array[middle] > input:
            right = middle - 1

