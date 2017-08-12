def solution(list_of_tuples):
    list = sorted(list_of_tuples, key=lambda t: t[-1])
    return list
