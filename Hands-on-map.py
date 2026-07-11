list_1 = [1, 2, 3, 4, 5]
list_2 = [6, 7, 8, 9, 10]
result= map(lambda x,y: x+y, list_1, list_2)
print("Addition of two lists using map and lambda function:")
print(list(result))

nums = [1, 2, 3, 4, 5]
def sqaure (n):
    return n*n
sq =list(map(sqaure, nums))
print("Square of numbers and list", sq)
