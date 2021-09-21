def selectionSorting(a):
    l = 0
    r = len(a)
    while(l<r):
        mina = l
        for i in range(l, r):
            if a[i] < a[mina]:
                mina = i
        a[mina], a[l] = a[l], a[mina]
        l +=1
    return a

print(selectionSorting([64, 25, 12, 22, 11]))
print(selectionSorting([56,56,87,234,789,45,6,89,34,56]))
print(selectionSorting([932,67,7823,782, 56,89,23,3,1,342]))