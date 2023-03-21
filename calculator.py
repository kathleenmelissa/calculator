#calculator

p=int(input("Enter the first number"))
q=int(input("Enter the second number"))
operator=str(input("Enter operator(+,-,*,/)"))
if operator=="+":
    print(p+q)
elif operator=="-":
    print(p-q)
elif operator=="/":
    print(p/q)
elif operator=="*":
    print(p*q)
else:
    print("Invalid operator")
