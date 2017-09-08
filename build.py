def solution(list_of_tuples):
    '''
    Enter your code here
    '''
    for i in range (0, len(list_of_tuples)-1):
        for j in range (0, len(list_of_tuples)-1):
            if list_of_tuples[j][1] > list_of_tuples[j+1][1]:
                list_of_tuples[j],list_of_tuples[j+1] = list_of_tuples[j+1],list_of_tuples[j]


    return list_of_tuples

'''
a = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print solution(a)
'''
