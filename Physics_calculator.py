class Physics:
    def calc_Physics(self):
        import math
        print("""
00000000000   00       00   00        00   00000000000  000000000000   000000000000   000000000000
00       00   00       00    00      00    00                00        00             00
00       00   00       00     00    00     00                00        00             00
00000000000   00000000000      00  00      00000000000       00        00             000000000000
00            00       00       0000                00       00        00                       00
00            00       00       00                  00       00        00                       00
00            00       00      00                   00       00        00                       00
00            00       00     00           00000000000   00000000000   000000000000   000000000000    
""")                                       
        def display():
            ans=str(input("WHAT WOULD YOU LIKE TO FIND ?:"))
            print(f"FINDING {ans}.....")
            def displacement():
                v=float(input("ENTER THE VELOCITY OF THE OBJECT:"))
                t=float(input("ENTER THE TIME TAKEN:"))
                d=v*t
                print(f"THE OBJECT WITH VELOCITY {v} AT TIME {t} GIVES A DISPLACEMENT OF {d}m")
            def velocity():
                d=float(input("ENTER THE DISPLACEMENT OF THE OBJECT:"))
                t=float(input("ENTER THE TIME TAKEN:"))
                v=d/t
                print(f"THE OBJECT DISPLACED AT {d}m FROM THE ORIGIN AT A TIME INTERVAL OF {t}s MOVES WITH THE VELOCITY OF {v}m/s")
            def time():
                v=float(input("ENTER THE VELOCITY OF THE OBJECT:"))
                d=float(input("ENTER THE DISPLACEMENT OF THE OBJECT:"))
                t=d/v
                print("THE TIME TAKEN TO REACH {d}m AT {v}m/s IS {t}s")
            def angle():
                o=float(input("ENTER THE LENGTH OF THE OPPOSITE SIDE:"))
                a=float(input("ENTER THE LENGTH OF THE ADJACENT SIDE:"))
                h=float(input("ENTER THE LENGTH OF THE HYPOTENUSE SIDE:"))
                sin=o/h
                cos=a/h
                tan=o/a
                cot=a/o
                cosec=1/sin
                sec=1/cos
                print(f"""sin(ø)  ={sin}
cos(ø)  ={cos}
tan(ø)  ={tan}
cot(ø)  ={cot}
cosec(ø)={cosec}
sec(ø)  ={sec}""")
            def angle_of_projection():
                print("""
|
|
|
|
|
|
|
|
|
|
|             .---------->maximum height  
|           . | .
|          .  |  .
|         .   |   . 
|        .    |    .
|       .     |     .
|      .      |<----------------------------->Distance between the ground and the max height    
|     .       |       .
|    .        |        .
|   .         |         . 
|  .          |          .  
| . [---------------------]<----------------> Total distance travelled from the origin                     
|.  <----------------------.--------------->angle of elevation           
|_______________________________________________________________________________________________

                        Distance between the ground and the max height=opposite


""")
                H=float(input("ENTER THE DISTANCE BETWEEN THE GROUND AND THE MAX HEIGHT REACHED:"))
                R=float(input("ENTER THE DISTANCE TRAVELLED BY THE OBJECT FROM THE ORIGIN:"))
                tan=math.degree(math.atan(4*H/R))
                print(f"THE ANGLE OF PROJECTION IS:{tan} degree")
            def angular_velocity():
                do=float(input("ENTER THE CHANGE IN ANGLE:"))
                dt=float(input("ENTER THE TIME OF THAT INSTANT:"))
                v=do/dt
                print(f"THE ANGULAR VELOCITY IS {v}rad/s")
            def average_speed():
                total_d=0
                total_t=0
                r=int(input("ENTER THE NUMBER OF READINGS OF THE DISTANCE:"))
                c=1
                for i in range(0,r+1):
                    d=float(input(f"ENTER THE {c} DISTANCE:"))
                    t=float(input("ENTER THE TIME IT REACHED THE DISTANCE:"))
                    total_d=total_d+d
                    total_t=total_t+t
                    c=c+1
                avg_velocity=total_d/total_t
                print(f"THE AVERAGE SPEED IS {avg_velocity}m/s")
            def acceleration():
                v=float(input("ENTER THE VELOCITY OF THE OBJECT:"))
                t=float(input("ENTER THE TIME INSTANT OF THAT VELOCITY"))
                a=v/t
                print(f"THE ACCELERATION IS {a}m/s²")
            def speed():
                d=float(input("ENTER THE DISTANCE:"))
                t=float(input("ENTER THE TIME TAKEN TO REACH THE DISTANCE:"))
                s=d/t
                print(f"THE SPEED IS {s}m/s")
        
            dis=["DISPLACEMENT","displacement","Displacement"]
            velocity=["VELOCITY","Velocity","velocity"]
            time=["TIME","Time","time"]
            angle=["ANGLE","angle","Angle"]
            angle_of_projection=["Angle of Projection","angle of projection","ANGLE OF PROJECTION","angleofprojection","ANGLEOFPROJECTION"]
            max_height=["MAXIMUM HEIGHT","maximum height","Maximum Height","maximumheight","MAXIMUMHEIGHT"]
            angular_velocity=["Angular Velocity","angular velocity","ANGULAR VELOCITY","angularvelocity","ANGULARVELOCITY"]
            e=["EXIT","X","Close","close","terminate","TERMINATE","exit"]
            avg_speed=["AVERAGE SPEED","average speed","Average Speed","AVERAGESPEED","averagespeed"]
            acc=["acceleration","ACCELERATION","Acceleration"]
            speed=["SPEED","speed"]
    
            if(ans in dis):
                displacement()
                display()
            elif(ans in velocity):
                velocity()
                display()
            elif(ans in time):
                time()
                display()
            elif(ans in angle):
                angle()
                display()
            elif(ans in angle_of_projection):
                angle_of_projection()
                display()
            elif(ans in angular_velocity):
                angular_velocity()
                display()
            elif(ans in avg_speed):
                average_speed()
                display()
            elif(ans in acc):
                acceleration()
                display()
            elif(ans in speed):
                speed()
                display()
            elif(ans in e):
                print("Leaving..................")
                searching()
            else:
                print("INVALID ARGUEMENT")
                display()
        display()
