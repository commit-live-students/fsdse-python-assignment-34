#def solution(list_of_tuples):
#    '''
#    Enter your code here
#    '''
#    return list

def last(n): return n[-1]

def solution(list_of_tuples):
  return sorted(list_of_tuples, key=last)

print solution([(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)])
