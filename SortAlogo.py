

# write a InsertSort on python

# let start with a array

v = [6, 5, 4, 3, 2, 1]

# start with second element as a key

for i in range(1, len(v)):
    key = v[i]
    # compare with the previous value
    # so take a less index
    j = i - 1
    while j >= 0 and key < v[j]:
        # shift / swap place
        v[j+1] = v[j]
        j = j - 1
    v[j+1] = key

print(v)
