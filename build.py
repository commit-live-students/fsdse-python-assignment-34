import operator

def solution(list_of_tuples):

    sorted_x = sorted(list_of_tuples, key=operator.itemgetter(1))

    return sorted_x
