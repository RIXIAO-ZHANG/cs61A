"""square root"""


def improved_square_guess(n,guess):
    return (guess+(n/guess)) / 2

def improved_cube_guess(n,guess):
    return (2*guess + (n/pow(guess,2)))/3




def square_root(n):
    guess = 1
    while pow(guess,2) != n:
        print(guess)
        guess = improved_square_guess(n,guess)      
    return guess

def cube_root(n):
    guess = 1
    while pow(guess,3) != n:
        print(guess)
        guess = improved_cube_guess(n,guess)
    return guess


"""These are common programming patterns that recur in code,
    but are used with a number of different functions.
    This patterns can be abstracted, by giving them names.
    To expres certain general patterns as named concepts, we will need to construct
    functions that can accept other functions as arguments or return functions as values.
 """
