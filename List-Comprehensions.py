#This function use lambda & map
'''
num = [1,2,3,4,5]
result = list(map(lambda x : x*x ,num))
print(result)
'''
num = [1,2,3,4,5]
result = [x*x for x in num]  ## variable = [expressition for item in list]>>>This is Comprehensions list
print(result)