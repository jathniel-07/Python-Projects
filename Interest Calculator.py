class Interest:
    def calc_Interest(self):
        def interest(principal_amount,no_of_years,interest_rate):
            interest_amt=principal_amount*no_of_years*interest_rate/100
            print(f"YOUR INTEREST IS:₨. {interest_amt}")
        def years(principal_amount,interest_amt,interest_rate):
            yot=interest_amt*100/principal_amount*interest_rate
            print(f"THE NUMBER OF YEARS IS: {yot}")
        def principal(interest_amt,no_of_years,interest_rate):
            p_amt=interest_amt*100/no_of_years*interest_rate
            print(f"THE VALUE OF P.A IS:₨. {p_amt}")
        def rates(principal_amount,no_of_years,interest_amt):
            roi=interest_amt*100/principal_amount*no_of_years
            print(f"THE RATE OF INTEREST IS: {roi}%")
        def display():
            print("WELCOME TO THE INTEREST Calculator")
            asking = input("WHAT WOULD YOU LIKE TO CALCULATE(INTEREST=I,PRINCIPAL_AMT=P,NO.OF.YEARS=n,RATE_OF_INTEREST=r,Exit=X)?:")
            if asking == "I":
                x = float(input("ENTER YOUR P.A:₨."))
                y = float(input("ENTER YOUR NUMBER OF YEARS:"))
                z = float(input("ENTER YOUR INTEREST RATE(%):"))
                interest(x, y, z, )
                display()
            if asking == "P":
                a = float(input("ENTER YOUR P.A:₨."))
                b = float(input("ENTER YOUR INTEREST RATE(%):"))
                c = float(input("ENTER NUMBER OF YEARS:"))
                principal(a, b, c)
                display()
            if asking == "n":
                p = float(input("ENTER YOUR P.A:₨."))
                q = float(input("ENTER YOUR INTEREST:₨."))
                r = float(input("ENTER YOUR INTEREST RATE(%):"))
                years(p, q, r)
                display()
            if asking == "r":
                d = float(input("ENTER YOUR P.A:₨."))
                e = float(input("ENTER NUMBER OF YEARS:"))
                f = float(input("ENTER YOUR INTEREST:₨."))
                rates(d, e, f)
                display()
            if asking=="X":
                exit()
                searching()
        display()