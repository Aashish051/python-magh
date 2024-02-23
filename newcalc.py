a=  float(input("Enter First Number:"))
b=  float(input("Enter second Number:"))

print("1. Addition\n2. Subtraction\n3. Multiplication")

choice=input("Enter Choice (1/2/3):")

if choice=='1':
    result=a + b
    print("Result=",result)
elif choice=='2':
    result=a - b
    print("Result=",result)
elif choice=='3':
    result=a * b
    print("Result=",result)
else:
    print ("Invalid Number")
    