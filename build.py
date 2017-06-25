from operator import itemgetter

def solution(dic):
    '''
    Enter your code here
    '''
    lst_asc = sorted(dic,key=itemgetter(1))
    return lst_asc
