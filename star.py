print("Right Angle Triangle of Stars(*)")
n=int(input("Please Enter the Number of Rows"))
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()