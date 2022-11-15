def timeConversion(s):
    L = s.split(":")
    part_day = str(L[2])
    if part_day[2:] == "PM" and L[0] != "12":
        time  = str(int(L[0])+12)+":"+L[1]+":"+part_day[0:2]
    elif L[0] == "12" and part_day[2:] == "AM":
        time  = "00"+":"+L[1]+":"+part_day[0:2]
    elif L[0] == "12" and part_day[2:] == "PM":
        time  = L[0]+":"+L[1]+":"+part_day[0:2]
    else :
        time  = L[0]+":"+L[1]+":"+part_day[0:2]
        
    return time
#______________________CODE DESCRIPTION_____________________
#i hate strings so the first thing i did is splitting the string in an array, then i check for am and fm being cautious about 12 am witch is used to say midnight
#and 12 fm witch is not 24 in the 24h clock but is still 12, for the am i just place it back how it is for fm i add 12 to the hours
