#
# Complete the 'compareTriplets' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY a
#  2. INTEGER_ARRAY b
#

def compareTriplets(a, b):
    player_a = 0
    player_b = 0
    b_count = 0
    for value in a:
        if value > b[b_count]:
            player_a += 1
        elif value < b[b_count]:
            player_b += 1
        b_count += 1
    L = [player_a, player_b]
    return L
#_____________________________________CODE DESCRIPTION________________________
#the for iterate trough the a list and a counter iterate trough the b list
#the one who has the higher value get the point, in the case of a draw nobody gets the point
#then it puts the scores in an array and returns it
