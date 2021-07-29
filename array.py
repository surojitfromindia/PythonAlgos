a1 = [12, 3, 44, 43]

print(a1[:2])  # this will cause array up to index less than 2
print(a1[2:])  # this will cause array from index 2 to end

a2 = [12, 3, 4, 32, 21]
n = len(a2)
nh = n//2
print(nh)

L = a2[:nh]
print(L)
R = a2[nh:]
print(R)


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
        print(L, " ", R)
        # divide the left array
        divde(L)
        divde(R)


divde([5, 6, 7, 9, 10])
