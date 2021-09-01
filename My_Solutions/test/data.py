a  = input()

res = ''
def Sub(a):
    ans = ""
    for i in a:
        if (i not in ans):
            ans = ans+i
        else:
            break
    return ans

for i in range(len(a)):
    x = Sub (a[i:])
    if len(x) > len (res):
        res = x
print(res)
print(len(res))

