def closestNumbers(arr):
#---------------------------------#sorting the array plus setting a high difference so that lower differences can be lower and creating a empty list for the numbers
#---------------------------------#the sorted list makes possible the fact that the closest number are next to each other and i only need 1 loop to find them
    arr.sort()
    difference = 9999
    lowst_diff_numb = []
    for count1 in range (len(arr)-1):
#---------------------------------# the for goes from 0 to the second-last
        n_c1 = arr[count1]
        c_c2 = arr[count1+1]
#--------# two number from (0:1) to (n-1:n)
        if abs(n_c1 - c_c2) < difference:
#---------------------------------# if the absolute difference between the numbers is lower that the one saved then it clear the list and append the new numbers
            lowst_diff_numb.clear()
            lowst_diff_numb.append(n_c1)
            lowst_diff_numb.append(c_c2)
            difference = abs(n_c1-c_c2)
        
        elif abs(n_c1 - c_c2) == difference:
#---------------------------------# if the absolute diffrence is equal it appends the numbers
            lowst_diff_numb.append(n_c1)
            lowst_diff_numb.append(c_c2)
            
    return lowst_diff_numb
