def quickSort(arr):
    equal = []
    right = []
    left = []
    for value in arr :
        if value < arr[0] : left.append(value)
        elif value > arr[0] : right.append(value)
        else : equal.append(value)
    left.extend(equal)
    left.extend(right)
    return left
#________________________CODE DESCRIPTION_____________________
#it iterate trouh the elements of the list and see if they are bigger, smaller or equal in respect of the first number in the array
#then if fuses all the lists and prints them
