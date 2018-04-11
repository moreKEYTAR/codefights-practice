# Core problems for practicing python.


# PROBLEM 1
def addTwoDigits(n):
    """
    Add digits in the integer n, which will always be a length of 2.
    >>> addTwoDigits(61)
    7
    """
    nums = divmod(n, 10)
    return nums[0] + nums[1]


# PROBLEM 2
def largestNumber(n):
    """
    Return the largest number possible given the number of digits long for the
    number (n).
    >>> largestNumber(3)
    999
    """
    # num_string = ""
    # while n > 0:
    #     num_string += "9"
    #     n -= 1
    # return int(num_string)

    num = n * "9"
    return int(num)

# PROBLEM 3
def candies(n, m):
    """
    n children have got m pieces of candy. They want to eat as much candy as
    they can, but each child must eat exactly the same amount of candy as any
    other child. Determine how many pieces of candy will be eaten by all the
    children together. Individual pieces of candy cannot be split.
    >>> candies(11, 87)
    77
    """
    # This uses 2.7 Python division, which removes the remainder
    return (m / n) * n


# PROBLEM 4
def seatsInTheater(nCols, nRows, col, row):
    """
    Return number of people whose view may be blocked if you leave the theater.
    >>> seatsInTheater(6, 5, 4, 3)
    6
    >>> seatsInTheater(50, 12, 25, 12)
    0
    """
    # row 5, col 1-6 XXX///
    # row 4, col 1-6 XXX/// exit
    # row 3, col 1-6 XXX0XX
    # row 2, col 1-6 XXXXXX
    # row 1, col 1-6 XXXXXX
    #                 stage

    # if you are in row 3, col 4, it affects 6 people
    # total rows - row you are in (to get affected rows behind you, because yours is EXCLUDED)
        # 5 - 3 = 2 (for height)
    # total cols - the ones to your right (to get the affected columns, because yours is INCLUDED)
        # total cols - (your col - 1) = 6-3 = 3 (for width)

    rows_affected = nRows - row
    cols_affected = nCols - (col - 1)
    return rows_affected * cols_affected



if __name__ == "__main__":
    import doctest

    if not doctest.testmod(verbose=True).failed:
        print "\nALL TESTS PASSED"
