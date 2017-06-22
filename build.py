from operator import itemgetter
list1=[(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
def solution(list_of_tuples):
    list1.sort(key=itemgetter(1))
    return list1
solution(list1)    
