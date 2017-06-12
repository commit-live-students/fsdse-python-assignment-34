import operator

def solution(list_of_tuples):
#    print list_of_tuples
    ascDic = sorted(list_of_tuples,key = operator.itemgetter(1))
    return ascDic
#    print ascDic

print solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
