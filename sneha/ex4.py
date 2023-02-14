str=input("Enter the text:")
dict={}
count=0
a=str.split()
print(a)
for i in a:
    if i in dict:
         dict[i]+=1
    else:
        dict[i]=1
for k,v in dict.items():
    print(k,v)

