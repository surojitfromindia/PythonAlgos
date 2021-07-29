# find if a sum exist in an sorted array


sum = 12
A = [3, 4, 5, 6, 6, 7, 11]


i = 0
j = len(A)-1

while(i < j):
    if(A[i] + A[j] == sum):
        print('found at position', i, " ,", j, end="\n")

    if (A[i] + A[j] < sum):
        # increase i
        i = i + 1
    else:
        # decrese j
        j = j - 1
