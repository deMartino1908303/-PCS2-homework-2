
def findMedian(arr):
    n = len(arr)
    median = int(((len(arr)+1)/2)-1)
    arr.sort()
    return arr[median]
   
#__________CODE DESCRIPTION__________
#by the time i write this i found a median function from statistics module
#i this case the lenght of the array is garanteed to be odd
#so i give +1 to make it even divide by 2 and subcract 1 because of the len function offset 
