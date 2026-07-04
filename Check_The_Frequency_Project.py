dict= {"My": 6, "name": 6, "is": 6, "Khalfan": 7, "and": 6, "I am": 6 , "from": 6, "Pakistan": 1}
print("The original dictionary is : " + str(dict))
K = 6
res = 0
for key in dict:
    if dict[key] == K:
        res += 1
print("The frequency of K is : " + str(res))