# Given 2 strings, a and b, return a string of the form short+long+short, 
# with the shorter string on the outside and the longer string on the inside. 
# The strings will not be the same length, but they may be empty ( zero length ).

# Hint for R users:

# The length of string is not always the same as the number of characters
# For example: (Input1, Input2) --> output


# ("1", "22") --> "1221"
# ("22", "1") --> "1221"


def short_long_short(a, b):
    if len(a) < len(b):
        short = a
        long = b
    else:
        short = b
        long = a
    
    return short + long + short



def short_long_short1(a, b):
    if len(a) < len(b):
        return a + b + a
    else:
        return b + a + b


print(short_long_short1("1", "22")) 