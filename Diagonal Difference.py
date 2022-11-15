def diagonalDifference(arr):
    # Write your code here
    pri_diag = 0
    sec_diag = 0
    for count in range(len(arr)):
        pri_diag += int(arr[count][count])
        sec_diag += int(arr[count][len(arr)-count-1])
    return abs(pri_diag-sec_diag)

#________________CODE DESCRIPTION________________________    
#since the arrays are cubes 1 counter for everything , 
#i sum the principla diagonal by getting the value [count] [count]
#the secondary starts from top so the fist list in the list but takes the last in the inner list so [count][reverse count]
#the -1 in the reverse count is there because the len function start from 1 but index start from 0
