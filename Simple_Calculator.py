# Task : Design a simple calculator with basic arithmetic operations.

def add(P, Q):
    return P + Q
def subtract(P, Q):
    return P - Q
def multiply(P, Q):
    return P * Q
def divide(P, Q):
    return P / Q

print("Please select the operation. ")
print("a. Add '+' ")
print("b. Subtract '-' ")
print("c. Multiply '*' ")
print("d. Divide '/' ") 

choice= input("Please enter choice(a/b/c/d):")

m1 = int(input(" Please enter first number: "))
m2 = int(input(" Please enter second number: "))

if choice =='a':
    print(m1,"+",m2,"=",add(m1,m2))

elif choice =='b':
    print(m1,"-",m2,"=",subtract(m1,m2))

elif choice =='c':
    print(m1,"*",m2,"=",multiply(m1,m2))

elif choice=='d':
    if m2 != 0:
        print(m1,"/",m2,"=",divide(m1,m2))
    else:
        print("invalid input.")

exit()