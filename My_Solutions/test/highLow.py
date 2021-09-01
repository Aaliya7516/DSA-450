a = [2, 4, 5, 6, 3,5,6 ,2] 

ans = []
def highLow(a):

    x = max(a)
    ans.append(x)
    a.remove(x)

    if(len(a) != 0):
        x = min(a)
        ans.append(x)
        a.remove(x)

    if len(a) != 0:
        highLow(a)

    if len(a) == 0:
        return ans

print(highLow(a))
