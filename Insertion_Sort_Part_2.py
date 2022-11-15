def insertionSort2(n, arr):
    for count1 in range (1,n):
#---------------------------#count of the number to examine from 1 to n-1 
        change = False

        for count2 in range (count1-1,-1,-1):
#---------------------------# decreasing fro cicle to see if the number before are smaller. if it finds any, it saves the position whereit is
#---------------------------#bigger of the one before and smaller than the one after
            if arr[count1] < arr[count2]:
                position = count2
                change = True
                
        if change :
#---------------------------# if it has any change to do it does them here
            tmp_inset = arr.pop(count1)
            arr.insert(position,tmp_inset)
        print(" ".join(map(str, arr)))
