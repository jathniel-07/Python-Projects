from cmath import sqrt,cos

def total_thrust():
    m=float(input("Enter the mass of the rocket(kg):"))
    dv=float(input("Enter the change in velocity of the rocket(m/s):"))
    dt=float(input("Enter the rate of change of time for the change in velocity dv(t):"))
    F_t=m*dv/dt
    print("Tangential thrust of the rocket:",F_t)
    r=float(input("Enter the radius of the rocket's path:"))
    v=float(input("Enter the velocity of the rocket:"))
    F_n=m*(v**2/r)
    print(f"Centripetal thrust of the rocket:{F_n}N")
    F_norm=F_t**2+F_n**2
    F=sqrt(F_norm)
    print(f"THE TOTAL THRUST OF THE ROCKET IS {F}N")

def acceleration():
    m=float(input("Enter the mass of the rocket(kg):"))
    F=float(input("Total thrust of the rocket(N):"))
    a=F/m
    print(f"The acceleration of the rocket:{a}m/s²")

def engine_thrust():
    m=float(input("Enter the mass flow rate of the Exhaust(kg/s):"))
    v=float(input("Enter the Exhaust velocity of the rocket(m/s):"))
    Pe=float(input("Enter the Exhaust Pressure:"))
    Pa=float(input("Enter the atmospheric pressure:"))
    A=float(input("Enter the Area of nozzle exit:"))
    F=m*v+(Pe-Pa)*A
    print(f"THE TOTAL THRUST OF THE ROCKET IS {F}N")
    O=float(input("Enter the angle of projection of the rocket(∅):"))
    angle=cos(O)
    print(f"THE TOTAL THRUST OF THE ROCKET AT AN ANGLE IS {F*angle}")
def display():
    print("SIMPLE ROCKET CALCULATOR")
    asking=input("WHAT WOULD YOU LIKE TO CALCULATE ?(total_thrust=Ttotal,acceleration=a,engine_thrust=et,Exit=X):")
    if asking=="Ttotal":
        total_thrust()
        display()
    if asking=="et":
        engine_thrust()
        display()
    if asking=="a":
        acceleration()
        display()
    if asking=="X":
        exit()
display()



