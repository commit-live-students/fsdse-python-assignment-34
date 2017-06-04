def solution(list_of_tuples):
    '''
    Enter your code here
    '''
    list_of_tuples.sort(key=lambda x:x[1])
    #list_of_tuples.sort(key=lambda x: x[len(list_of_tuples)-1])
    return list_of_tuples
#print(solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]))
