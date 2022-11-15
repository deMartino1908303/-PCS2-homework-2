def plusMinus(arr):
    pos = 0
    neg = 0
    zero = 0
    for value in arr :
        if value > 0 :
            pos += 1
        elif value < 0 :
            neg += 1
        else:
            zero +=1
    
    pos_rate = pos / len(arr)
    neg_rate = neg / len(arr)
    zero_rate = zero / len(arr)
    print("%.6f" % pos_rate,"%.6f" % neg_rate,"%.6f" % zero_rate, sep = "\n")
    
   #_________________________CODE DESCRIPTION_______________________
    #it iterate trough all the values in the array and see if they are bigger, smaller or equal to zero then print the rate of precence with 6 decimals
