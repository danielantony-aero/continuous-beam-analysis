def bm():
    print("\nCalculation of bending moment ")
    l = int(input("Length of beam in m: "))
    load_type = int(input("For Point Load Type '1' And For UDL Load Type '2': "))
    if load_type == 1:
        # bending moment due to point load calculation
        p = int(input("Number of point loads: "))
        p_loads = []
        p_dist = []
        p_bm = []

        for i in range(p):
            ploads = int(input(f"Enter point load {i+1} in N: "))
            p_loads.append(ploads)
            pdist = int(input(f"Enter distance of load {i+1} from left support in m: "))
            p_dist.append(pdist)
            p_bm.append((p_loads[i] * p_dist[i]) - ((p_loads[i] * p_dist[i]**2) / l))

        M = max(p_bm)
        print(f"maximum bending moment:{M} Nm")
        return M

    elif load_type == 2:
        # bending moment due to udl load calculation
        udl = float(input("UDL load intensity in N/m: "))
        a = int(input("UDL starting point from left support in m: "))
        b = int(input("UDL ending point from left support in m: "))
        l=b-a
        # conditions for udl load 
        if a < l and a >= 0 and a < b:
            x_max = (a + b) / 2
            udl_to_pl = udl * l
        elif b > 0 and b <= l and b > a:
            print("invalid input ,starting point exceeds beam length")
            a = int(input("UDL starting point from left support in m: "))
            b = int(input("UDL ending point from left support in m: "))
        else:
            print("invalid input , end point is before starting point")
            a = int(input("UDL starting point from left support in m: "))
            b = int(input("UDL ending point from left support in m: "))
        Rb = (udl_to_pl * (l - x_max)) / l
        Ra =   udl_to_pl - Rb
        udl_bm = (Ra * x_max) - (udl / 2) * (x_max - a) ** 2
        M = udl_bm
        print(f"maximum bending moment:{M}Nm")
        return M
        
def inertia():
    
    def inertia_T():
        # T SECTION
        print("T SECTION")
        print("Dimensions Of The Top Flange")
        b1 = int(input("Enter The Width of Top Flange(mm):\n"))
        d1 = int(input("Enter The Depth of Top Flange(mm):\n"))
        print("Dimensions Of The Web")
        b2 = int(input("Enter The Width of The Web(mm):\n"))
        d2 = int(input("Enter The Depth of The Web(mm):\n"))
        A1 = b1 * d1
        A2 = b2 * d2
        y1 = (d1 / 2) + d2
        y2 = d2 / 2
        y = ((A1 * y1) + (A2 * y2)) / (A1 + A2)
        h1 = abs(y1 - y)
        h2 = abs(y2 - y)
        I1 = ((b1 * (d1 ** 3)) / 12) + (A1 * (h1 ** 2))
        I2 = ((b2 * (d2 ** 3)) / 12) + (A2 * (h2 ** 2))
        I = I1 + I2
        print(f"\nMoment of inertia of T section is:{I}mm⁴")
        return I,y

    def inertia_I_symmetrical():
        # I SECTION (symmetrical)
        print("I SECTION (symmetrical)")
        print("Dimensions Of The Top Flange")
        b1 = int(input("Enter The Width of Top Flange(mm):\n"))
        d1 = int(input("Enter The Depth of Top Flange(mm):\n"))
        print("Dimensions Of The Web")
        b2 = int(input("Enter The Width of The Web(mm):\n"))
        d2 = int(input("Enter The Depth of The Web(mm):\n"))
        b3 = b1
        d3 = d1
        A1 = b1 * d1
        A2 = b2 * d2
        A3 = b3 * d3
        y1 = (d1 / 2) + (d2 + d3)
        y2 = d2 / 2 + d3
        y3 = d3 / 2
        y = ((A1 * y1) + (A2 * y2) + (A3 * y3)) / (A1 + A2 + A3)
        h1 = abs(y1 - y)
        h2 = abs(y2 - y)
        h3 = abs(y3 - y)
        I1 = ((b1 * (d1 ** 3)) / 12) + (A1 * (h1 ** 2))
        I2 = ((b2 * (d2 ** 3)) / 12) + (A2 * (h2 ** 2))
        I3 = ((b3 * (d3 ** 3)) / 12) + (A3 * (h3 ** 2))
        I = I1 + I2 + I3
        print(f"\nMoment of inertia of I section is:\n{I}mm^4")
        return I,y

    def inertia_I_unsymmetrical():
        print("I SECTION (unsymmetrical)")
        print("Dimensions Of The Top Flange")
        b1 = int(input("Enter The Width of Top Flange(mm):\n"))
        d1 = int(input("Enter The Depth of Top Flange(mm):\n"))
        print("Dimensions Of The Web")
        b2 = int(input("Enter The Width of The Web(mm):\n"))
        d2 = int(input("Enter The Depth of The Web(mm):\n"))
        print("Dimensions Of The Bottom Flange")
        b3 = int(input("Enter The Width of Bottom Flange(mm):\n"))
        d3 = int(input("Enter The Depth of Bottom Flange(mm):\n"))
        A1 = b1 * d1
        A2 = b2 * d2
        A3 = b3 * d3
        y1 = (d1 / 2) + (d2 + d3)
        y2 = d2 / 2 + d3
        y3 = d3 / 2
        y = ((A1 * y1) + (A2 * y2) + (A3 * y3)) / (A1 + A2 + A3)
        h1 = abs(y1 - y)
        h2 = abs(y2 - y)
        h3 = abs(y3 - y)
        I1 = ((b1 * (d1 ** 3)) / 12) + (A1 * (h1 ** 2))
        I2 = ((b2 * (d2 ** 3)) / 12) + (A2 * (h2 ** 2))
        I3 = ((b3 * (d3 ** 3)) / 12) + (A3 * (h3 ** 2))
        I = I1 + I2 + I3
        print(f"\nMoment of inertia of I section is:\n{I}mm^4")
        return I,y

    def inertia_circular():
        D=int(input("Enter the outer diameter(mm):"))
        d=int(input("Enter the inner diameter(mm):"))
        I=(3.14*((D**4)-(d**4)))/64
        y=D/2
        print(f"\nMoment of inertia of circular section is:\n{I}mm^4")
        return I,y
        
    def inertia_rectangular():
        b= int(input("Enter The Width of the beam (mm):\n"))
        d=int(input("Enter The Depth of the beam (mm):\n"))
        y=d/2
        I=(b*(d**3))/12
        print(f"\nMoment of inertia of rectangular section is:\n{I}mm^4")
        return I,y
    #area of cross section selection   
    print('''
    Select Cross-Section Type
    1. T-Section
    2. I-Symmetrical Section
    3. I-Unsymmetrical Section
    4. Circular Section
    5. Rectangular Section''')
    
    choice = input("Enter choice or type cross-section name: ")

    if choice == "1" or choice.lower() == "t-section" or choice.lower() == "t":
        return inertia_T()
    elif choice == "2" or choice.lower() == "i-symmetrical section" or choice.lower() == "i-symmetrical":
        return inertia_I_symmetrical()
    elif choice == "3" or choice.lower() == "i-unsymmetrical section" or choice.lower() == "i-unsymmetrical":
        return inertia_I_unsymmetrical()
    elif choice == "4" or choice.lower() == "circular section" or choice.lower() == "circular":
        return inertia_circular()
    elif choice == "5" or choice.lower() == "rectangular section" or choice.lower() == "rectangular":
        return inertia_rectangular()
    else:
        print("Invalid choice. Please try again.")
        inertia()
        
        
#user interface 
print('''
====================================================
Welcome to Beam Deflection Calculator
====================================================
''')
print("What do you want to calculate?")
print('''1. Maximum Stress (σ)
2. Maximum Distance from Neutral Axis (y)
3. Maximum Bending Moment (M)
4. Moment of Inertia (I)
5. Young's Modulus (E)
6. Radius of Curvature (R) ''')
choice=int(input("Enter the unknown to be calculated (1-6):"))

y_max=0
if choice==1: 
    print("\nTo Calculate Maximum Stress")
    M=input("\nMaximum bending moment (M) in Nm: ")
    if M==" ":
        M=bm()
    elif M==0:
        M=0
    else:
        M=int(M)
        
    I=input("Moment of inertia (I) in mm⁴: ")
    if I==" ":
        I,y_max=inertia()
        print("y max",y_max)
    elif I==0:
        I=0
    else:
        I=int(I)
    E=int(input("Young's Modulus (E) in N/mm²: "))
    R=int(input("Radius of curvature (R) in m: "))
    if not y_max:
        y_max=int(input("Distance from neutral axis (y) in mm: "))
 #stress calculation       
    if E==0 and R==0:
        stress = ((M*1000)/I) * y_max
    else:
        stress = (E /( R*1000)) * y_max
    stress=round(stress,5)   
    print(f"Maximum Stress of the beam: {stress}N/mm²")
    print(f"Maximum Stress of the beam: {stress*1000000}N/m²")
    
elif choice==2: 
    print("\nTo Calculate  Distance from Neutral Axis")
    I,y_max=inertia()
    y_max=round(y_max,2)
    print(f"y maximum: {y_max}mm")
    
elif choice==3: 
    print("\nTo Calculate Maximum Bending Moment  ")
    E=int(input("Young's Modulus (E) in N/mm²:"))
    R=int(input("Radius of curvature (R) in m:"))
    stress=int(input("Maximum Stress of the beam(σ) in N/mm²:"))
    I=input("Moment of inertia (I) in mm⁴: ")
    if I==" ":
        I,y_max=inertia()
        print(f"y max: {y_max} mm")
    elif I==0:
        I=0
    else:
        I=int(I)
    if not y_max:
        y_max=int(input("Distance from neutral axis (y) in mm: "))
    #max bending moment calculation       
    if E==0 and R==0:
        M=(stress/y_max)*I
    else:
         M=(E/(R*1000))*I
    print(f"Maximum bending moment of the beam: {M}Nmm")
    print(f"Maximum bending moment of the beam: {M/1000}Nm")
     
elif choice==4: 
    print("\nTo Calculate Moment of Inertia")
    print('''To find Inertia using,
    1)Dimensions 
    2)Bending moment, Distance from neutral axis and stress 
    3) Bending moment,Radius of curvature and Young's modulus 
    ''')
    var=int(input("Enter the method of finding Moment of Inertia:"))
    if var==1:
        I,y_max=inertia()
        print(f"Inertia of the beam: {I}mm⁴")
        print(f"Inertia of the beam: {I/1000000000000}m⁴")
        
    if var==2:
         M=int(input("\nMaximum bending moment (M) in Nm: "))
         y_max=int(input("Distance from neutral axis (y) in mm: "))
         stress=int(input("Maximum Stress of the beam(σ) in N/mm²:"))
         I=(y_max/stress)*(M*1000)
         print(f"Inertia of the beam: {I}mm⁴")
         print(f"Inertia of the beam: {I/1000000000000}m⁴")
    if var==3:
         M=int(input("\nMaximum bending moment (M) in Nm: "))
         R=int(input("Radius of curvature (R) in m: "))
         E=int(input("Young's Modulus (E) in N/mm²:"))        
         I=(R/E)*(M*1000000)
         print(f"Inertia of the beam: {I}mm⁴")
         print(f"Inertia of the beam: {I/1000000000000}m⁴")
         
elif choice==5: 
    print("\nTo Calculate Young's Modulus ")
    print('''To find Young's modulus using,
    1)Bending moment, Inertia and Radius of curvature 
    2) Stress,Radius of curvature and Distance from neutral axis 
    ''')
    var=int(input("Enter the method of finding Young's modulus:"))
    
    if var==1:
        R=int(input("Radius of curvature (R) in m:"))
        M=int(input("\nMaximum bending moment (M) in Nm: "))
        I=input("Moment of inertia (I) in mm⁴: ")
        if I==" ":
            I,y_max=inertia()
            print(f"y max: {y_max} mm")
        else:
            I=int(I)
        E=((M*1000)/I)*(R*1000)
        print(f"Young's modulus of the beam is:{E}N/mm²")
    
    if var==2: 
        R=int(input("Radius of curvature (R) in m:"))
        stress=int(input("Maximum Stress of the beam(σ) in N/mm²:"))  
        y_max=int(input("Distance from neutral axis (y) in mm: "))
        E=(stress/y_max)*(R*1000)
        print(f"Young's modulus of the beam is:{E}N/mm²")
        
elif choice==6: 
    print("\nTo Calculate Radius of Curvature ")
    print('''To find Radius of Curvature using,
    1)Bending moment, Inertia and Young's modulus 
    2) Stress, Young's modulus and Distance from neutral axis 
    ''')
    var=int(input("Enter the method of finding Radius of Curvature:"))
    
    if var==1:
         E=int(input("Young's Modulus (E) in N/mm²:"))
         M=int(input("\nMaximum bending moment (M) in Nm: "))
         I=input("Moment of inertia (I) in mm⁴: ")
         if I==" ":
            I,y_max=inertia()
            print(f"y max: {y_max} mm")
         else:
            I=int(I)
         R=(I/M)*E
         print(f"Radius of curvature of the beam:{R*(10**-6)}m")
    if var==2: 
        E=int(input("Young's Modulus (E) in N/mm²:"))
        stress=int(input("Maximum Stress of the beam(σ) in N/mm²:"))  
        y_max=int(input("Distance from neutral axis (y) in mm: "))
        R=(y_max/stress)*E
        print(f"Radius of curvature of the beam:{R*(10**-3)}m")
    
else:
    print ("\ninvalid Selection try again!!!")