x,y,z = input("Expression: ").split()

if y == "+":
    result = float(x) + float(z)
    print(result)
elif y == "-":
    result = float(x) - float(z)
    print(result)
elif y == "*":
    result = float(x) * float(z)
    print(result)
elif y == "/":
    result = float(x) / float(z)
    print(result)
else:
    print("Error")