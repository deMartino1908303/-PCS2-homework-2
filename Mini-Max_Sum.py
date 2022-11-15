def miniMaxSum(arr):
    tot_sum = []
    
    for counter in range(len(arr)):
        tmp_sum = 0
        for count in range(len(arr)):
            if count != counter:
                tmp_sum += arr[count]
        tot_sum.append(tmp_sum)
    
    print(min(tot_sum), max(tot_sum))
    
  
#_______________________________CODE DESCRIPTION___________________________  
#since it give a maxium of 5 integres to sum i decided to do all the possible sums of 4 integers out of the 5 and
#print the max and the min of the array with all the sums
