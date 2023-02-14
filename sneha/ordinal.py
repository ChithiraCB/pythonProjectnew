list1=["python","java"]
list2=[]
for item in list1:
    for ele in item:
        result=ord(ele)
        list2.append(result)
print(list2)