import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = (10.0, 10.0)
print("ACCOUNTS BAR GRAPH-BY JATHNIEL")
e=[]
c=[]
allowance=int(input("ENTER THE ALLOWANCE:"))
def expenses():
    r=int(input("ENTER THE NUMBER OF EXPENSES:"))
    for i in range(0,r):
        a=str(input("ENTER THE EXPENSE:"))
        b=int(input("ENTER THE COST:"))
        e.append(a)
        c.append(b)
def showing():
    y_position = range(len(e))
    plt.bar(y_position, c)
    plt.xticks(y_position, e)
    plt.ylabel('AMOUNT')
    plt.xlabel('EXPENSES')
    plt.title("ACCOUNTS")
    plt.show()
expenses()
showing()
d=0
for i in c:
    d=d+i
print(f"THE TOTAL COST IS Rs.{d} OUT OF Rs.{allowance} AND REMAINING IS Rs.{allowance-d}")





