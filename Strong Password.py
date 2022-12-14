def minimumNumber(n, password):
    
    numbers = "0123456789"
    num_precence = False
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    low_precence = False
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    up_precence = False
    special_characters = "!@#$%^&*()-+"
    spc_precence = False
    
#---------------------------# creation of data and verification variables
    for count in range(n) :
        if not num_precence and password[count] in numbers :
            num_precence = True
        elif not low_precence and password[count] in lower_case :
            low_precence = True
        elif not up_precence and password[count] in upper_case :
            up_precence = True
        elif not spc_precence and password[count] in special_characters :
            spc_precence = True
#---------------------------# it iterate trough the characters in the password and turn true the verification variables of the one that it finds

    result  = (num_precence, low_precence, up_precence, spc_precence)
    #---------------------------#it count the number of false, meaning the absence of a specific type of character
   # ---------------------------# if the lenght of the password plus the things to add are not enough to create a 6 caracter password return how many character to reach 6
    if result.count(False)< 6-n :
       return 6-n
    
    return result.count(False)
