def Mergesort(A):
    if (len(A) > 1):
        # calcualte middle point
        middle = len(A) // 2
        # create two new arrays ,
        LA = A[:middle]
        RA = A[middle:]
        # call Mergesort on both halves
        Mergesort(LA)
        Mergesort(RA)

        # let take 3 index
        i = 0
        j = 0
        k = 0

        # start merging, using two pointer algo
        while i < len(LA) and j < len(RA):
            if LA[i] < RA[j]:
                A[k] = LA[i]
                i = i + 1
            else:
                A[k] = RA[j]
                j = j + 1
            # increase value of k
            k = k + 1

        # copy rest of the elements
        while i < len(LA):
            A[k] = LA[i]
            i = i + 1
            k = k + 1
        while j < len(RA):
            A[k] = RA[j]
            j = j + 1
            k = k + 1


A = [12, 4, 6, 7, 12, 2, 4, 5]
Mergesort(A)
print(A)
