expression = input("Expression: ")
x , y, z = expression.split()

x = float(x)
z = float(z)

if y == "+":
    print(x + z)
elif y == "-":
    print(x - z)
elif y == "*":
    print(x * z)
elif y == "/":
    if z == 0:
        print("Undefined")
    else:
        print(x / z)
else: 
    print("Invalid Input")

