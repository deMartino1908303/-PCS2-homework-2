def marsExploration(s):
    num_errors = 0
#---------------------------# it create a sub list of lenght 3 and checks if the first is s the second o and the third s
    for count in range(3,len(s)+3,3):
        sos = list(s[count - 3:count])
        if sos[0] != "S":
            num_errors += 1
        if sos[1] != "O":
            num_errors += 1
        if sos[2] != "S":
            num_errors += 1
    
    return num_errors
