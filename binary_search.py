array_in_question = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] #can comment this out and use an array of your choice.



def searcharray(array, input):
    if input not in array:
        raise ValueError("value not in array")
    
    left, right = 0, len(array) - 1
    while left <= right:
        middle = (left + right) // 2 # uses both backslashes to get the lower rounded value of the division
        if array[middle] == input:
            return middle
        elif array[middle] < input:
            left = middle + 1
        elif array[middle] > input:
            right = middle - 1

user_input = input("put in a number to search for in the array: 1-10: ")

found_index = searcharray(array_in_question, int(user_input)) #Simply calls the fucntion and passes the array and input value we want to find.
print (f"Value found at index:{found_index}  contains = {array_in_question[found_index]}")

input("Press enter to exit the program")


