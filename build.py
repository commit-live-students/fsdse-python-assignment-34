import operator
def solution(list_of_tuples):

    list = sorted(list_of_tuples,key=operator.itemgetter(1))
    #list = sorted(list_of_tuples,key=lambda x: x[1])
    return list

d =  [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print solution(d)
