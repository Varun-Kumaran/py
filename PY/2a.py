def oddeven(a):
    if (a%2==0):
        return "Even"
    else:
        return "Odd"
num=int(input("enter a number:"))
print("The given number is ",oddeven(num))
