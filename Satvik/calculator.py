def calculator():
    print("1 for Addition")
    print("2 for Subtraction")
    print("3 for Division")
    print("4 for Multiplication")
    operation= int(input("please enter your choice:"))
    num1=float(input("Please enter a number :"))
    num2=float(input("Please enter any other number :"))
    
    if operation ==1:
        result= num1+num2
        print(result)
    elif operation==2:
        result= num1-num2
        print(result)
    elif operation==3:
        result= num1 /num2
        print(result) 
    elif operation== 4:
        result= num1*num2
        print(result)
    else: 
        print(" Operation is not defined ")   
   
calculator()
