num1=int(input("enter first number"))
num2=int(input("enter second number"))


gcd = 1

for i in range(1, max(num1, num2)):
    if num1 % i == 0 and num2 % i == 0:
        gcd = i
print( gcd)