def countingSort(arr):
    lis = [0] * 100
    
    for value in arr:
        lis[value] += 1
    return lis

#__________________________________CODE DESCRIPTION__________________________
#it create a list of 0 then the for iterate trough the given list giving a +1 in the corrispondingn position
