import operator
def solution(list_of_tuples):
    '''
    Enter your code here
    '''
    asc_list = sorted(list_of_tuples,key=operator.itemgetter(1))
    return asc_list

solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
