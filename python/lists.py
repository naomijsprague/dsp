# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


def match_ends(words):
    """
    Given a list of strings, return the count of the number of strings
    where the string length is 2 or more and the first and last chars
    of the string are the same.

    >>> match_ends(['aba', 'xyz', 'aa', 'x', 'bbb'])
    3
    >>> match_ends(['', 'x', 'xy', 'xyx', 'xx'])
    2
    >>> match_ends(['aaa', 'be', 'abc', 'hello'])
    1
    """
    count = 0
    for i in words:
        if len(i) >= 2 and i[len(i)-1:] == i[:1]:
            count = count + 1
    return count
    raise NotImplementedError


def front_x(words):
    """
    Given a list of strings, return a list with the strings in sorted
    order, except group all the strings that begin with 'x' first.
    e.g. ['mix', 'xyz', 'apple', 'xanadu', 'aardvark'] yields
         ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'].

    >>> front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa'])
    ['xaa', 'xzz', 'axx', 'bbb', 'ccc']
    >>> front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa'])
    ['xaa', 'xcc', 'aaa', 'bbb', 'ccc']
    >>> front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark'])
    ['xanadu', 'xyz', 'aardvark', 'apple', 'mix']
    """
    xwords = []
    others = []
    for i in words:        
        if i[:1] == 'x':
            xwords.append(i)
        else:
            others.append(i)
    xwords.sort()
    others.sort()
    for i in others:
        xwords.append(i)
    return xwords
    raise NotImplementedError


def sort_last(tuples):
    """
    Given a list of non-empty tuples, return a list sorted in
    increasing order by the last element in each tuple.
    e.g. [(1, 7), (1, 3), (3, 4, 5), (2, 2)] yields
         [(2, 2), (1, 3), (3, 4, 5), (1, 7)].

    >>> sort_last([(1, 3), (3, 2), (2, 1)])
    [(2, 1), (3, 2), (1, 3)]
    >>> sort_last([(2, 3), (1, 2), (3, 1)])
    [(3, 1), (1, 2), (2, 3)]
    >>> sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)])
    [(2, 2), (1, 3), (3, 4, 5), (1, 7)]
    """
    def sort_last(tuples):
        sorted_by_second = sorted(tuples, key=lambda tup: tup[-1])
    print sorted_by_second
   

def remove_adjacent(nums):
    i = 0
    while i < len(nums)-1:
        if nums[i] == nums[i+1]:
            del(nums[i])
        i = i+1
    print nums

remove_adjacent([1, 2, 2, 3])  


def linear_merge(list1, list2):
    def linear_merge(list1, list2):
    new_list = list1
    for i in range(len(list2)):
        new_list.append(list2[i])   
    new_list.sort()
    print new_list
    
    
    
linear_merge(['aa', 'xx', 'zz'], ['bb', 'cc'])
