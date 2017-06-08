'''
def solution(list_of_tuples):

    newList = []
    for i in range(len(list_of_tuples)):
        for j in range(1,len(list_of_tuples)):
            if list_of_tuples[i][1] < list_of_tuples[j][1]:
                newList.append(list_of_tuples[i])
    return newList

list_of_tuples = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(solution(list_of_tuples))
'''

def solution(list_of_tuples):
    return sorted(list_of_tuples, key=lambda x: x[1])

lst_tups = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(solution(lst_tups))
