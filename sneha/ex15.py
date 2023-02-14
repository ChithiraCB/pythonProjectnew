a=[1,2,3,4]
b=[4,9,8]
if(len(a)==len(b)):
    print("length is same")
else:
    print("length is not same")
if(sum(a)==sum(b)):
    print("sums to same value")
else:
    print("not same value")
print("values occuring in both: ")
for i in a:
    if i in b:
        print(i)
if i not in b:
        print("no values")


