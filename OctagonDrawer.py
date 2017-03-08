import turtle

nrSides = 0
lengthOfLine = 50

nrSides = int(input("How many sides should your shape have? "))

for sides in range(0, nrSides):
    turtle.forward(lengthOfLine)
    turtle.right(360/nrSides)
    
    for sides in range(0, nrSides):
        turtle.forward(lengthOfLine/2)
        turtle.right(360/nrSides)