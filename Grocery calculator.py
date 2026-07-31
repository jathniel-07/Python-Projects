class Grocery:
    def calc_grocery(self):
        import time
        print("|GROCERY CALCULATOR|")
        number_of_items=int(input("ENTER THE NUMBER OF THE ITEMS:"))
        total_price=0
        f=open("grocery.txt",'w')
        p=1
        for i in range(0,number_of_items):
            price=float(input(f"ENTER THE PRICE OF {p}st ITEM:₨."))
            list=str(input("ENTER THE NAME OF THE LIST:"))
            f.write(f"{p}.{list} - {price}\n")
            p=p+1
            total_price=total_price+price
        print(f"THE TOTAL COST OF {number_of_items} ITEMS IS:₨.{total_price}")
        f.write(f"THE TOTAL COST OF {number_of_items} ITEMS IS:₨.{total_price}")
        print("\nYOUR GROCERY LIST IS SAVED AS grocery.txt THE SAME DIRECTORY")
        f.close()
        complete_msg="\nLIST COMPLETED !"
        for i in complete_msg:
            print(i,end="",flush=True)
            time.sleep(0.01)
g=Grocery()
g.calc_grocery()
