def pangrams(s):
    lower_string = s.lower()
    alph = "qwertyuioplkjhgfdsazxcvbnm"
    for letter in alph:
        if letter not in lower_string :
            return "not pangram"
    return "pangram"

#_____________________CODE DESCRIPTION_______________
#it iterate trough all the letter of the alphabet and see if they are present in the string if
#a letter is not in the string then it is not a panagram, it is all set to lowercase for compatibility 
