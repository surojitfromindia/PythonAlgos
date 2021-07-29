a1 = [5, 6, 12]
a2 = [1, 9, 10]

i = 0
j = 0
k = 0
# fill this array
a3 = []
# check if either of the index reach max length
while i < 3 and j < 3:
    if(a1[i] < a2[j]):
        a3.append(a1[i])
        i = i + 1
    else:
        a3.append(a2[j])
        j = j + 1
# copy the rest of cause i may not reach the last index yet

while(i < 3):
    a3.append(a1[i])
    i = i + 1

while(j < 3):
    a3.append(a2[j])
    i = i + 1


print(a3)
