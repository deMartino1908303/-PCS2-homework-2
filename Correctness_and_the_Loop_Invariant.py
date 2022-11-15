def insertion_sort(l):
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
#the mistake is that j needs to be equal to 0 to swap in case the number is in the first position
           l[j+1] = l[j]
           j -= 1
        l[j+1] = key
