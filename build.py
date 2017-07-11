def solution(list_of_tuples):
    list = sorted(list_of_tuples, key=lambda x: x[1])
    return list
