

def Merge(A, a1, a2):
    i = 0
    j = 0
    # fill this array
    k= 0
    # check if either of the index reached max length
    while i < len(a1) and j < len(a2):
        if(a1[i] < a2[j]):
            A[k]= a1[i]
            i = i + 1
        else:
            A[k]=a2[j]
            j = j + 1
        k = k +1
    
    # copy the rest of cause i may not reach the last index yet
    while(i < len(a1)):
        A[k] = a1[i]
        i = i + 1
        k = k + 1

    while(j < len(a2)):
        A[k]= a2[j]
        j = j + 1
        k = k + 1


def divde(A):
    # do this if and only if the start and end index are different
    # that is there is only one element in array
    # or can use length function
    if(len(A) > 1):
        # calculate the half
        nh = (len(A)) // 2
        # create a left array and a right array
        L = A[:nh]
        R = A[nh:]

        # divide the left array
        divde(L)
        divde(R)
        Merge(A, L, R)


A = [5, 7, 6, 10, 1]
divde(A)
print(A)

