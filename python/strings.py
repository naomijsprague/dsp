# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def donuts(count):
    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.

    >>> donuts(4)
    'Number of donuts: 4'
    >>> donuts(9)
    'Number of donuts: 9'
    >>> donuts(10)
    'Number of donuts: many'
    >>> donuts(99)
    'Number of donuts: many'
    """
    if count < 10:
        return "Number of donuts: %s" % count
    else:
        return "Number of donuts: many"
        


def both_ends(s):
    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.

    >>> both_ends('spring')
    'spng'
    >>> both_ends('Hello')
    'Helo'
    >>> both_ends('a')
    ''
    >>> both_ends('xyz')
    'xyyz'
    """
    if len(s) < 2:
        return ''
    else:
        front = s[:2]
        back = s[(len(s)-2):]
        return front + back
        
    raise NotImplementedError


def fix_start(s):
    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.

    >>> fix_start('babble')
    'ba**le'
    >>> fix_start('aardvark')
    'a*rdv*rk'
    >>> fix_start('google')
    'goo*le'
    >>> fix_start('donut')
    'donut'
    """
    new_word = s[:1]
    for i in s[1:]:
        if i == s[:1]:
            new_word =  new_word + '*'
        else:
            new_word = new_word + i
    return new_word
    
    raise NotImplementedError


def mix_up(a, b):
    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.

    >>> mix_up('mix', 'pod')
    'pox mid'
    >>> mix_up('dog', 'dinner')
    'dig donner'
    >>> mix_up('gnash', 'sport')
    'spash gnort'
    >>> mix_up('pezzy', 'firm')
    'fizzy perm'
    """
    afront = a[:2]
    aback = a[2:]
    bfront = b[0:2]
    bback = b[2:]
    new_first = bfront + aback
    new_second = afront +bback
    return new_first + ' '+ new_second
    
    raise NotImplementedError


def verbing(s):
    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    >>> verbing('hail')
    'hailing'
    >>> verbing('swimming')
    'swimmingly'
    >>> verbing('do')
    'do'
    """
    if len(s) >= 3:
        if s[len(s)-3:] == 'ing':        
            return s + 'ly'
        else:
            return s + 'ing'
    else:
        return s
    raise NotImplementedError


def not_bad(s):
    word_not = 'not'
    word_bad = 'bad'
    index_not = s.find(word_not)
    index_bad = s.find(word_bad)
    if index_not < index_bad:
        new_string = s[:index_not] + 'good' + s[index_bad+3:]
    print new_string    


def front_back(a, b):
    len_a = len(a)/2
    len_b = len(b)/2
    if len(a)%2 == 0:
        a_front = a[:len_a]
        a_back = a[len_a:]
    elif len(a)%2 != 0:
        a_front = a[:len_a+1]
        a_back = a[len_a+1:]
    if len(b)%2 == 0:
        b_front = b[:len_b]
        b_back = b[len_b:]
    elif len(b)%2 != 0:
        b_front = b[:len_b+1]
        b_back = b[len_b+1:]
    new_string = a_front + b_front + a_back + b_back
    print new_string
