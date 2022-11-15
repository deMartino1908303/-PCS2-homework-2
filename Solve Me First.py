def solveMeFirst(a,b):
	# Hint: Type return a+b below
    # i made it more fun
    arr_a = [0]*a
    arr_b = [0]*b
    arr_a.extend(arr_b)
    return len(arr_a)
#__________code description___________
#in order to use as mutch memory possible on the hackerranck server as possible i create array with 0 in them long as mutch as the value to sum
#i extend one with the other and the lenght of the resulting array is the sum of the two starting number
