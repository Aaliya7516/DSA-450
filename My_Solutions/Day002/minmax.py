arr = [3,3,43,45,65,654,8,2,123,31,5435,5,54,23,123,12]

max = arr[0]
min = arr[0]

for i in arr:
    if (i < min):
        min = i
    elif (i > max):
        max = i
        
print (min, max)