
# -*- coding: utf-8 -*-

import operator

def solution(list_of_tuples):
    '''
    Enter your code here
    '''
    return sorted(list_of_tuples, key=operator.itemgetter(1))
    #itemgetter
    #Return a callable object that fetches item from its operand using the operand’s __getitem__() method.
    #If multiple items are specified, returns a tuple of lookup values.

print(solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
