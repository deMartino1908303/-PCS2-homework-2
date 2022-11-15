def caesarCipher(s, k):
#---------------------------------------#creation of reference alphabets (upper and lower case) + empty string to fill
    new_str = ""
    alph = "abcdefghijklmnopqrstuvwxyz"
    cap_alph = alph.upper()
#---------------------------------------# loop of every letter in the string    
    for character in s :
    
        if character in alph :
#---------------------------------------# to do if the letter is lowecase
            place = alph.index(character)
#-------------#find were is it on the alphabet and find the transposed letter if the place + the offset is bigger than 26
            while place+k >= 26 :
                place -=  26
#-------------# resetting the sting so it contains itself plus the new letter
            new_str = new_str + alph[place+k]
        elif character in cap_alph :
#---------------------------------------# to do if the letter is uppercase        
            place = cap_alph.index(character)
            while place+k >= 26 :
                place -=  26
            new_str = new_str + cap_alph[place+k]
#---------------------------------------# to do if the character is not a letter
        else :
            new_str = new_str + character
    
    return new_str
