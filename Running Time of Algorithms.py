def runningTime(arr):
    n = len(arr)
    swaps = 0
    for count1 in range (1,n):
        position = 0
        change = False
        #print ("-1-this is the cicle number : ", count1)
        for count2 in range (count1-1,-1,-1):
            #print ("##this is the count for cecking : ", count2)
            if arr[count1] < arr[count2]:
                position = count2
                change = True
        if change :
            tmp_inset = arr.pop(count1)
            arr.insert(position,tmp_inset)
            swaps += count1-position
    return swaps
#_________________________________CODE DESCRIPTION________________________
#this is my code of insertion sort 2 but insted of returning the sorted list it returns the number of position swapped in total
