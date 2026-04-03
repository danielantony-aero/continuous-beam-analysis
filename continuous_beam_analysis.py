print("Continuous Beam Analysis\n")
n = int(input("Enter the number of spans: "))

# Creating storage for inputs
l = []
mpl = []
epl = []
x_mpl = []
x_epl = []
w = []
area = []
cg_x = []

# Getting values
for i in range(1, n + 1):
    length = int(input(f"\nEnter the length of Span {i}: "))
    l.append(length)

    print(f'''\nType of Load Applied in Span {i}:
    1) Point Load at Middle
    2) Point Load at Eccentric Point
    3) Uniformly Distributed Load (UDL)''')

    load_type = int(input(f"\nEnter the type of load applied in Span {i}: "))

    if load_type == 1:
        print("\nApplied Load: Point Load at Middle\n")
        middle_pl = int(input("Enter the point load: "))
        mpl.append(middle_pl)
        x_mpl.append(length / 2)

        epl.append(0)
        x_epl.append(0)
        w.append(0)

    elif load_type == 2:
        print("\nApplied Load: Eccentric Point Load\n")
        eccentric_pl = int(input("Enter the eccentric point load: "))
        distance_epl = int(input("Enter the distance from the left support: "))
        epl.append(eccentric_pl)
        x_epl.append(distance_epl)

        mpl.append(0)
        x_mpl.append(0)
        w.append(0)

    elif load_type == 3:
        print("\nApplied Load: Uniformly Distributed Load (UDL)\n")
        udl = int(input("Enter the UDL: "))
        w.append(udl)

        mpl.append(0)
        x_mpl.append(0)
        epl.append(0)
        x_epl.append(0)

# Unpacking and processing values
for j in range(n):
    length = l[j]
    point_load = mpl[j]
    pl_dist = x_mpl[j]
    eccentric_pl = epl[j]
    epl_dist = x_epl[j]
    udl = w[j]

    if point_load != 0:
        BM_max = (point_load * length) / 4
        A = 0.5 * length * BM_max
        x = length / 2

    elif eccentric_pl != 0:
        a = epl_dist
        b = length - a
        BM_max = (eccentric_pl * a * b) / length
        A = 0.5 * length * BM_max
        x = (length + a) / 3

    else:  # UDL
        BM_max = (udl * (length ** 2)) / 8
        A = (2 / 3) * length * BM_max
        x = length / 2

    area.append(A)
    cg_x.append(x)

# Getting values for formula substitution
A1, A2 = area[0], area[1]
x1, x2 = cg_x[0], cg_x[1]
l1, l2 = l[0], l[1]

print(f"\nValues for formula substitution:")
print(f"A1 = {A1}, x1 = {x1}, l1 = {l1}")
print(f"A2 = {A2}, x2 = {x2}, l2 = {l2}")
#rxn moment calculation 
M_rxn=(-3*(((A1*x1)/l1)+((A2*x2)/l2)))/(l1+l2)
print(f"reaction moment:{M_rxn}")		