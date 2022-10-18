def add(x,y):
    return x+y

def sub(x,y):
    return x-y

def mul(x,y):
    return x*y
    
def div(x,y):
    return x/y
    
    
print("\t\t\t\tCALCULATOR")
x=int(input("Enter first num: "))
y=int(input("Enter Second  num: "))

z=input("Enter your choice: \n1. +\n2. -\n3. *\n4. /")

if z=='+':
    print("Sum is: ",add(x,y))
elif z=='-':
    print("Substraction is: ",sub(x,y))
elif z=='*':
    print("Multiplication is: ",mul(x,y))
elif z=='/':
    print("Division is: ",div(x,y))
else:
    print("Wrong Choice")
