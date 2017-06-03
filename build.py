def solution(list_of_tuples):
    lis=[]
    lis=sorted(list_of_tuples,key= lambda x:x[1])
    return lis
val = [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]
print(solution(val))
