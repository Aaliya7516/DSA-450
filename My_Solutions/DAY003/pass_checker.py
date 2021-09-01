def checker(p):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    symbol = ['@', '#','!','~','$','%','^','&','*','(',',','-','+','/',':','.',',','<','>','?','|']
    if " " in p:
        return False
    
    print("no space")
    flag = False
    for i in range (10):
        if str(i) in p:
            flag = True
            break
    if flag != True:
        return False
        
    print("num present")
    if (len(p)<8) or (len(p)>15):
        return False
        
    print("right len")
    flag = False
    for i in p:
        if i in alpha:
            flag = True
            break
    if flag != True:
        return False
        
    print("small alpha present")
    flag = False
    for i in alpha:
        if i.upper() in p:
            flag = True
            break
    if flag != True:
        return False
        
    print("capital alpha present")
    flag = False
    for i in p:
        if i in symbol:
            flag = True
            break
    if flag != True:
        return False
        
    print("symbol present")
    print("-=-=-=-=-=-=-=-=-=-=-=-=-=-")
    print("Valid Password")
    return ""
    
print(checker(input()))