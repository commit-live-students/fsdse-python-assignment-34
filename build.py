"""
# Write a Python program to get a list, sorted in increasing order by the last element in each tuple from a given list of non-empty tuples.


**Notes:**
* Define a function to accept list of tuples as parameter.
* For each tuple get last element and sort list according to ascending order of last element in tuples.
* Return sorted list.


**Instructions:**
* Program should be written in file build.py
* Function name should be solution.
* Input

       Type:  List
       Value: [(2, 5), (1, 2), (4, 4), (2, 3), (2, 1)]

* Expected Output

        Type:  List
        Value: [(2, 1), (1, 2), (2, 3), (4, 4), (2, 5)]

"""
def solution(list_of_tuples):
    '''
    Enter your code here
    '''
    return sorted(list_of_tuples,key=lambda x:x[1])
