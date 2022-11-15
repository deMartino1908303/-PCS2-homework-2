def insertionSort1(n, arr):
    n -= 1
    tmp = arr[n]
#---------------------------#n start from 1 so -1 to fix it for list index and saving the first 
    while n > 0:
        if arr[n-1] > tmp:
#---------------------------# if the number before is bigger than the one being examined i move the number up 1 index
            arr[n] = arr[n-1]
            print(" ".join(map(str, arr)))
        elif arr[n-1] < tmp:
#---------------------------#if the number before is smaller i place the number to sort after it and break the cycle, 
            arr[n] = tmp
            print(" ".join(map(str, arr)))
            break
        n -= 1
    if arr[0] == arr[1]:
#---------------------------# looking back this could have been a while >= 1 but instead i did this if
        arr[0] = tmp
        print(" ".join(map(str, arr)))
