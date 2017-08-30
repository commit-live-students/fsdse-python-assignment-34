def solution(list_of_tuples):
    '''
    Enter your code here
    '''
    def last(n):
        return n[-1]

    return sorted(list_of_tuples, key = last)
