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


# PROBLEM 5
def maxMultiple(divisor, bound):

    """
    Return the largest int (less or equal to the bound)
    that is...
    1) evenly divisible by the divisor
    2) is greater than zero.
    Guaranteed that an answer exists (a multiple of the divisor)
    >>> maxMultiple(3, 10)
    9
    >>> maxMultiple(7, 101)
    98
    """

    return (bound / divisor) * divisor


# PROBLEM 6
def circleOfNumbers(n, firstNumber):
    """
    Given n and firstNumber, find the number which is
    written in the radially opposite position to firstNumber.
    (In a circle of integers, starting with 0 and ending at n-1)
    >>> circleOfNumbers(6, 3)
    0
    >>> circleOfNumbers(10, 2)
    7
    """
    ans = (n / 2) + firstNumber
    if ans >= n:
        ans -= n
    return ans


# PROBLEM 7
def lateRide(n):

    """
    Calculate the time given
    - start time is 00:00
    - n number of minutes have elapsed since start time
    ** Time should be returned as a sum of the digits of the time,
    with a 24-hr clock
    >>> lateRide(808)
    14
    """

    hours, mins = divmod(n, 60)
    h1, h2 = divmod(hours, 10)
    m1, m2 = divmod(mins, 10)
    return h1 + h2 + m1 + m2


# PROBLEM 8
def phoneCall(min1, min2_10, min11, s):

    # min1 is 1 minute in length
    # min2_10 is 9 minutes in length

    min_count = 0

    if s >= min1:
        min_count += 1
        s -= min1

        if s >= min2_10:
            num_min2_10 = s/min2_10
            if num_min2_10 < 9:
                min_count += num_min2_10
            else:
                min_count += 9
                s -= (min2_10 * 9)

                if s >= min11:
                    num_min11 = s/min11
                    min_count += num_min11
    return min_count


if __name__ == "__main__":
    import doctest

    if not doctest.testmod().failed:
        print "\nALL TESTS PASSED"
