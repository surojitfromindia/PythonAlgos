
def InsertSort(A):
    # first get a key
    for i in range(1, len(A)):
        # get first key
        key = A[i]
        # get the prior element to compare
        j = i - 1
        # start the loop
        while A[j] > key and j >= 0 :
            # swap/ shift 1 room right
            A[j + 1] = A[j]
            # decrease j for next comparison
            j = j - 1
        # after exiting the loop
        # replace the last value with key
        A[j + 1] = key
    return A

sortedA = InsertSort([6, 7, 34, 2, 1, 5])            
print(sortedA)
