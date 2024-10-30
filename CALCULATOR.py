def calculator ():
    n1=int(input("Enter a number: "))
    sign=input("Enter a sign: ")
    n2=int(input("Enter a number: "))
    if(sign=="+"):
        print(n1+n2)
    elif (sign == "-"):
           print(n1-n2)
    elif(sign=="*"):
           print(n1*n2)
    elif(sign=="/"):
           print(n1/n2)
    elif(sign=="%"):
           print(n1%n2)
    else:
        print("invalid sign")
calculator()