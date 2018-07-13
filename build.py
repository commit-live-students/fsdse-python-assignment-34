def solution(list_of_tuples):
    list = sorted(list_of_tuples, key=lambda tup: tup[-1] )
    return list
