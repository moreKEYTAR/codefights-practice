"""

Write a solution that only iterates over the string once and uses O(1) 
additional memory, since this is what you would be asked to do during a 
real interview.

Given a string s, find and return the first instance of a non-repeating 
character in it. If there is no such character, return '_'.

Examples...

    >>> s = "abacabad"
    >>> firstNotRepeatingCharacter(s)
    c

There are 2 non-repeating characters in the string: 'c' and 'd'. 
Return c since it appears in the string first.

    >>> s = "abacabaabacaba"
    >>> firstNotRepeatingCharacter(s)
    '_'

There are no characters in this string that do not repeat.

Input/Output...

    [execution time limit] 4 seconds (py)

    [input] string s

    A string that contains only lowercase English letters.

    Guaranteed constraints:
    1 <= s.length <= 105

    [output] char

The first non-repeating character in s, or '_' if there are no characters 
that do not repeat.

"""


def firstNotRepeatingCharacter(s):

    import string
    alphabet = string.ascii_lowercase
    alpha_dict = {}

    for letter in alphabet:
        alpha_dict[letter] = (len(s), 0)
        # tuple with (index, count)
        # index is length of s because this index will never be used

    for i, char in enumerate(s):
        count = alpha_dict[char][1] + 1
        alpha_dict[char] = (i, count)

    uniques = []
    for key, value in alpha_dict.iteritems():
        if value[1] == 1:
            uniques.append((value[0], key))
            # adds tuple with the index first, then the key for easier sorting
    uniques.sort()

    result = "_"
    if uniques:
        result = uniques[0][1]
    return result

##### V1 ###############################################

#     s_dict = {s[-1]:1}  # for loop will go backwards; part of plan to go backwards through list

#     for i in range(-2, -(len(s) + 1), -1):
#         current = s[i]
#         count = s_dict.get(current, 0)
#         s_dict[current] = count + 1
    
#     for char in s:
#         count = s_dict.get(char)
#         if count == 1:
#             return char
#     return '_'


if __name__ == "__main__":
    import doctest

    result = doctest.testmod(verbose=True)
    if not result.failed:

        print "\nTESTS PASSED."
