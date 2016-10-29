def insertionsort(seq):
    i = 1
    while i < len(seq):
        key = seq[i]
        j = i - 1
        while j >= 0 and seq[j] > key:
            seq[j+1] = seq[j]
            j = j-1
        seq[j+1] = key
        i = i + 1

L = [5,2,4,6,1,3]
L2 = [10, 4, 7, 19, 2, 11]
print(L)
insertionsort(L)
print(L)
print(L2)
insertionsort(L2)
print(L2)
print(L)
insertionsort(L)
print(L)
