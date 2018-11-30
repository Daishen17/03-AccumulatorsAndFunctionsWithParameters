"""
This module lets you practice the ACCUMULATOR pattern
in its simplest classic forms:
   SUMMING:       total = total + number

Authors: David Mutchler, Vibha Alangar, Matt Boutell, Dave Fisher, Mark Hays,
         Aaron Wilkin, their colleagues, and Yifan Dai.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.
import math
def sum_of_digits(number):
    if number < 0:
        number = -number
 
    digit_sum = 0
    while True:
        if number == 0:
            break
        digit_sum = digit_sum + (number % 10)
        number = number // 10

    return digit_sum


def main():
    """ Calls the   TEST   functions in this module. """
    run_test_sum_cosines()
    run_test_sum_square_roots()



def run_test_sum_cosines():
    """ Tests the   sum_cosines   function. """
    # -------------------------------------------------------------------------
    # DONE: 2. Implement this function.
    #   It TESTS the  sum_cosines  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_cosines   function:')
    print('--------------------------------------------------')

    expected = 0.5403023058681398
    answer = sum_cosines(1)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 0.4161468365471424
    answer = sum_cosines(2)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    expected = 0.9899924966004454
    answer = sum_cosines(3)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def sum_cosines(n):
        C = math.cos(n)

        return sum_of_digits(C)



    # -------------------------------------------------------------------------
    # DONE: 3. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_cosines  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


def run_test_sum_square_roots():
    """ Tests the   sum_square_roots   function. """
    # -------------------------------------------------------------------------
    # DONE: 4. Implement this function.
    #   It TESTS the  sum_square_roots  function defined below.
    #   Include at least **   3   ** tests.
    #
    # Use the same 4-step process as in implementing previous
    # TEST functions, including the same way to print expected/actual.
    # -------------------------------------------------------------------------
    print()
    print('--------------------------------------------------')
    print('Testing the   sum_square_roots   function:')
    print('--------------------------------------------------')

    expected = 1
    answer = sum_square_roots(1)
    print('Test 1 expected:', expected)
    print('       actual:  ', answer)

    expected = 1.4142135623730951
    answer = sum_square_roots(2)
    print('Test 2 expected:', expected)
    print('       actual:  ', answer)

    expected = 1.7320508075688772
    answer = sum_square_roots(3)
    print('Test 3 expected:', expected)
    print('       actual:  ', answer)

def sum_square_roots(n):
    HDD = math.sqrt(n)
    return sum_of_digits(HDD)




    # -------------------------------------------------------------------------
    #DONE: 5. Implement and test this function.
    #   Note that you should write its TEST function first (above).
    #   That is called TEST-DRIVEN DEVELOPMENT (TDD).
    #
    #   No fair running the code of  sum_square_roots  to GENERATE
    #   test cases; that would defeat the purpose of TESTING!
    # -------------------------------------------------------------------------


# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
