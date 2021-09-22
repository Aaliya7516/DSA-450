def repeatedStringMatch( A, B):
    A1 = A
    count = 1
    while len(A)< len(B):
        A += A1
        count +=1
    if B in A:
        return count
    elif B in A+A1:
        return count+1
    else:
        return -1

print(repeatedStringMatch("a", "cdabcdab"))
print(repeatedStringMatch("abcd", "cdabcdab"))
print(repeatedStringMatch("aa", "a"))