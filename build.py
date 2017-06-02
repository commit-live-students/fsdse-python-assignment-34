def solution(list_of_tuples):
    '''
    Enter your code here
    '''
    import operator
    sort_list = [None] * len(list_of_tuples)
    for item in list_of_tuples:
        total = 0
        for comp_item in list_of_tuples:
            total += operator.gt(item[-1],comp_item[-1])
        sort_list[total] = (item)
    return sort_list
