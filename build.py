def solution(list_of_tuples):

    return sorted(list_of_tuples,key=lambda x:x[1])

# solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 0), (3,5,1)])
# output: [(2, 0), (3, 5, 1), (1, 2), (2, 3), (4, 4), (2, 5)]
