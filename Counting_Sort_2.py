def countingSort_list(arr):
    lis = [0] * 100
    for value in arr:
        lis[value] += 1
    return lis

#----------------------------#i used my code from counting sort 1 to create the counter array
    
def countingSort(arr):
    
    counted_arr = countingSort_list(arr)
    sorted_lis = []
    index_counter = 0
    
    for counter in counted_arr:
#----------------------------#the for iterate trough the values in the counter array
#----------------------------#for each it appends the index that start from 0 and +1 every for cycle
        
        for times in range(counter):
#---------------#repeat the append for how big is the counter from my counting sort 1
            sorted_lis.append(index_counter)
        
        index_counter += 1
    
    return sorted_lis
