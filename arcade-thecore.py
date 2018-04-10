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
    num_string = ""
    while n > 0:
        num_string += "9"
        n -= 1
    return int(num_string)


if __name__ == "__main__":
    import doctest

    if not doctest.testmod(verbose=True).failed:
        print "ALL TESTS PASSED"
