def camelcase(s):
    # Write your code here
    cap_alp = "QWERTYUIOPLKJHGFDSAZXCVBNM"
    cap_lett = 0
    for count in s:
        if count in cap_alp:
            cap_lett += 1
    
    return cap_lett + 1


#_________________CODE DESCRIPTION___________
#if the letter in the string is in the capitalize alphaet the counter goes up by 1 because is a separate word
#+1 for the initial word that doesn`t have a capital letter
