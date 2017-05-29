def solution(list_of_tuples):

    def byKey(tup):
        return tup[-1]

    list_of_tuples.sort(key = byKey)
    return list_of_tuples
