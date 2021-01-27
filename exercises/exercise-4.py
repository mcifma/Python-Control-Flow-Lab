# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


sideA=int(input("Please enter the length of the first side of the triangle:   "))
sideB=int(input("Please enter the length of the second side of the triangle:  "))
sideC=int(input("Please enter the length of the third side of the triangle:  "))



if (sideA == sideB) and (sideA == sideC):
    
    print(f"A triangle with sides {sideA}, {sideB} & {sideC} is an equalateral triangle")

elif (sideA == sideB) and (sideA != sideC ) and (sideB != sideC):
    print(f"A triangle with sides {sideA}, {sideB} & {sideC} is an isosceles triangle")

elif (sideA != sideB) and (sideA != sideC) and (sideB != sideC):
    print(f"A triangle with sides {sideA}, {sideB} & {sideC} is a scalene triangle")
    


