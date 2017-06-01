def solution(list_of_tuples):
    d={}
    list=[]
    for k in list_of_tuples:
        d[k[-1]]=k
    sd = sorted(d.items())
    for k,v in sd:
        list.append(v)
    return list

output=solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
print output
