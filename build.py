def solution(list_of_tuples):
    return sorted(list_of_tuples, key=last)

def last(n): return n[-1]

solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
