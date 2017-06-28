def solution(list_of_tuples):
    '''
    Enter your code here
    '''

    list = sorted(list_of_tuples, key= lambda x: x[1])
    return list
