a=float(input("Enter First Number:"))
b=float(input("Enter Second Number:"))

print("1.add\n2.subtract\n3.multiply\n4.divide")

choice=input("Enter choice(1/2/3/4):")

if choice=='1':
    result=a+b
    print("Outcome:",result)
elif choice=='2':
    result=a-b
    print("Outcome:",result)
elif choice=='3':
    result=a*b
    print("Outcome:",result)
elif choice=='4':
    if b == 0:
        print("Error!")
    else:
        result = a / b
        print("Result:", result)
else:
    print("invalid number:")
        

        
