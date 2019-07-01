"""square root"""


def improved_square_guess(n,guess):
    return (guess+(n/guess)) / 2

def improved_cube_guess(n,guess):
    return (2*guess + (n/pow(guess,2)))/3






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

"Generalization process"
def improve(update, close, guess=1):
    while not close(guess):
        print(guess)
        guess = update(guess)
    return guess


def approx_eq(x,y,tolerance = 1e-15):
    return abs(x-y) < tolerance

"Specification process. To specify what it really means for the update and close function"
def square_root(a):
    def update(guess):
        return improved_square_guess(a,guess)
    def close(guess):
        return approx_eq(a,guess)
    return improve(update,close)
    "Call expression: To tell the improve funtion"
    "update and close are statements, therefore they are not evaluated."
