class Calculator:
    def calc_Simple(self):
        def multiply():
            r=int(input("Enter the range of numbers to be multiplied:"))
            ans=1
            for i in range(1,r+1):
                a=int(input("Enter the number to be multiplied:"))
                b=a
            ans=ans*b
            print(f"The multiplied number is: {ans}")
        def divide():
            a=int(input("Enter the Numerator:"))
            b=int(input("Enter the Denominator:"))
            ans=a/b
            print(f"The divided number is: {ans}")
        def add():
            r=int(input("Enter the range of numbers to be added:"))
            ans=0
            for i in range(1,r+1):
                a=int(input("Enter the number to be added:"))
                b=a
                ans=ans+b
            print(f"The added number is: {ans}")
        def subtract():
            r=int(input("Enter the range of numbers to be subtracted:"))
            a=int(input("Enter the number to be subtracted:"))
            for i in range(1,r):
                b=int(input("Enter the number to be subtracted:"))
                a=a-b
            print(f"The subtracted number is: {a}")
        def modulus():
            a=int(input("Enter the Divident:"))
            b=int(input("Enter the Divisor:"))
            ans=a%b
            print(f"the Remainder is: {ans}")
        def display():
            print("Welcome to the Python Calculator")
            asking = input("What would you like to do?(Add=A,Subtract=S,Divide=D,Multiply=M,Modulus=Mod,Exit=E):")
            if asking == "A":
                add()
                display()
            if asking == "S":
                subtract()
                display()
            if asking == "D":
                divide()
                display()
            if asking == "M":
                multiply()
                display()
            if asking == "Mod":
                modulus()
                display()
            if asking == "E":
                print("\nEXITING...")
                exit
        display()

