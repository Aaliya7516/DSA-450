def countSetBits(n):
    sum = 0
    def ones(n):
        if n == 1 or n == 1:
            return n
        else:
            return (0 if n%2 == 0 else 1) + ones(n//2)
    for i in range(1,n+1):
        sum += ones(i)
    return sum

print(countSetBits(4))
print(countSetBits(17))
print(countSetBits(177312))