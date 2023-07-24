print("Hello this is a program that does math for you, press enter after every answer") 

print("")

mathquestion = input("This calculater can do geomatry, quadratic formula, normal calculator,Pythagorean Theorem and more, enter what you want to calculate")
normalcalculator = input("For normal calculator type 'calculator' or press enter to continue")  
 # divition, subtraction, addition, multiplication 

if normalcalculator == "calculator":    
  calculater = input("Enter any expression (multiplication is *): ")  
  print(" ")
  print("= ",eval(calculater) ) 


def sum(diviona, additionb): 
    return (divitiona / additionb) 
if mathquestion == "Divition":
  divitiona = int(input('Enter 1st number: ')) 
  additionb = int(input('Enter 2nd number: '))
  print(f'{divitiona} divided by {additionb} = {sum(divitiona, additionb)}') 
  

def sum(subtractiona, subtractionb): 
    return (subtractiona - subtractionb) 
if mathquestion == "subtraction": 
  subtractiona = int(input('Enter 1st number: '))
  subtractionb = int(input('Enter 2nd number: '))
  print(f'{subtractiona} - {subtractionb} = {sum(subtractiona, subtractionb)}') 


def sum(additiona, additionb): 
    return (additiona + additionb) 
if mathquestion == "addition":
  additiona = int(input('Enter 1st number: '))
  additionb = int(input('Enter 2nd number: '))
  print(f'{additiona} + {additionb} = {sum(additiona, additionb)}')  
    
def sum(multiplicationa, multiplicationb): 
    return (multiplicationa * multiplicationb) 
if mathquestion == "multiplication": 
  multiplicationa = int(input('Enter 1st number: '))
  multiplicationb = int(input('Enter 2nd number: '))
  print(f'{multiplicationa} * {multiplicationb} is {sum(multiplicationa, multiplicationb)}') 

# volume of sphere, cube, rectanguler prism, pyramid, cone

import math
math.pi
pi = math.pi 
if mathquestion == "volume": 
 volumeshape = input("What shape? ") 
 if volumeshape == "sphere":
   raduispherevolume = int(input("What's the raduis? "))  
   print(4*math.pi*raduispherevolume**3/3) 


if mathquestion == "volume":
 if volumeshape == "cube": 
   sidecubevolume = int(input("What is the side length? "))  
   print(sidecubevolume**2) 

if mathquestion == "volume":
 if volumeshape == "rectangulrer prism": 
   rectangulerprismvolumel = int(input("what is the length? ")) 
   rectangulerprismvolumew = int(input("What is the width? ")) 
   rectangulerprismvolumeh = int(input("What is the height? " )) 
   print(rectangulerprismvolumel * rectangulerprismvolumew * rectangulerprismvolumeh) 


if mathquestion == "volume": 
 if volumeshape == "pyramid": 
  pyramidvolumel = int(input("What is the base length? ")) 
  pyramidvolumew = int(input("What is the base width?" )) 
  pyramidvolumeh = int(input("what is the pyramid height? ")) 
  print(pyramidvolumel*pyramidvolumew*pyramidvolumeh/3) 


if mathquestion == "volume": 
 if volumeshape == "cone": 
  conevolumer = int(input("what's the raduis of the cone? "))   
  conevolumeh = int(input("what's the hight of a cone? "))         
  print(math.pi*conevolumer**2*conevolumeh/3)       
 
# surface area of sphere, rectangular prism, cylinder, cone

if mathquestion == "surface area":
 shapesa = input("Which shape? ")   
 if shapesa == "sphere":   
  spheresaraduis = int(input("What's the raduis of the sphere ")) 
  print(4*math.pi*spheresaraduis**2)  

if mathquestion =="surface area":
 if shapesa =="rectanguler prism": 
  rpsal = int(input("Enter length: ")) 
  rpsaw = int(input("Enter width: "))
  rpsah = int(input("Enter height: ")) 
  rpsa = (rpsaw * rpsal + rpsah * rpsal + rpsah * rpsaw)  
  print(2*rpsa)  
 


if mathquestion == "surface area":
  if shapesa == "cylinder": 
    cysar = int(input("Enter raduis: "))  
    csah = int(input("Enter raduis: ")) 
    print(2 * math.pi * cysar * csah + 2 * math.pi * cysar**2)  
  

if mathquestion == "surface area": 
  if shapesa == "cone": 
    conesar = int(input("Enter raduis: "))
    conesah = int(input("Enter height: ")) 
    conesaanswer = (conesar + math.sqrt(conesah**2 + conesar**2))
    print(math.pi * conesar * conesaanswer) 

# Pythagorean theorem

if mathquestion == "Pythagorean theorem": 
  Pythagoreantheorema = int(input("Enter side a: "))
  Pythagoreantheoremb = int(input("Enter side b: ")) 
  Pythagoreantheoremanswer = (Pythagoreantheorema**2 + Pythagoreantheoremb**2) 
  Pythagoreantheoremanswera = (math.sqrt(Pythagoreantheoremanswer)) 
  print("Pythagorean theorem =" + str(Pythagoreantheoremanswera))  

# area of circle, rectangle, square, triangle 
#to do list, area of, pentagon, octagon 

if mathquestion == "area": 
 shapearea = input("What shape? ") 
 if shapearea == "circle": 
  circlearearaduis = int(input("Enter the circles raduis: ")) 
  print(math.pi*circlearearaduis**2)
 

if mathquestion == "area":
 if shapearea == "rectangle":
   print("rectangle area formula = length * height") 
   rectangleareabase = int(input("Enter rectangle base: "))
   rectangleareaheight = int(input("Enter rectangle height: ")) 
   rectangleareaanswer = (rectangleareabase * rectangleareaheight)
   print("the rectangle area = " + str( rectangleareabase ) + " * " + str( rectangleareaheight ) + ' ' + "=" + ' ' + str( rectangleareaanswer ))

if mathquestion == "area":
 if shapearea == "square": 
  print("Square area formula = side to the power of 2 ")  
  squareside = int(input("Enter the side length of square: "))
  squareareaanswer = (squareside**2)
  print("Square area = " + ' ' + str(squareside) + ' ' + "to the power of 2 = " + str(squareareaanswer)) 

if mathquestion == "area":
 if shapearea == "triangle": 
   print("triangle area formula = 1/2 * base * height ")
   triangleareabase = int(input("Enter triangle base: "))
   triangleareaheight = int(input(" Enter triangle height: "))
   triangleareaanswer = (0.5 * triangleareabase*triangleareaheight) 
   print("The triangle area = 1/2 *" + ' ' + str(triangleareabase) + " * " + str(triangleareaheight) + " = " + str(triangleareaanswer))  

if mathquestion == "area": 
  if shapearea == "trapazoid": 
    print("trapazoid area formula = base a + base b divided by 2 * height") 
    trapazoidareaa = int(input("Enter base a: "))
    trapazoidareab = int(input("Enter base b: ")) 
    trapazoidareah = int(input("Enter height of trapazoid: ")) 
    trap=(trapazoidareaa+trapazoidareab) 
    zoid=(trap/2) 
    trapazoidareaanswer=(zoid*trapazoidareah) 
    print(trapazoidareaanswer) 

if mathquestion == "area":
  if shapearea == "rhombus":
    print("Rhombus formula = diagonal 1 * diagonal 2 divided by 2")
    rdiaganal = int(input("Enter diagonal 1: ")) 
    rdiagnal2 = int(input("Enter diagonal 2: ")) 
    rhombusareaanswer = (rdiaganal*rdiagnal2/2)  
    print("rhombus =" + str(rdiaganal) + ' * ' + str(rdiagnal2) + " divided by 2 = " + str(rhombusareaanswer))  

if mathquestion == "area":
  if shapearea == "diamond":
    print("diomond formula = diagonal 1 * diagonal 2 divided by 2")
    diomonda = int(input("Enter diagonal 1: ")) 
    diomandb = int(input("Enter diagonal 2: ")) 
    diomandanswer = (diomonda*diomandb/2)  
    print("Diomond =" + str(diomonda) + ' * ' + str(diomandb) + " divided by 2 = " + str(diomandanswer))  
    
   # if mathquestion == "area":
  # if shapearea == "pentagon":
   # print("pentagon formula = 1/4 square root of 5*(5+2 square root of 5 ) x side squared")
    # pentagonarea = int(input("Enter side length of Pentagon:"))
    # pentagon1 = (5+2*math.sqrt(5)*pentagonarea**2)
    # pentagonareaanswer = (1/4*math.sqrt(5))
    # print(0.25*math.sqrt(5*(5+2*math.sqrt(5))*pentagonarea**2)) 

if mathquestion == "area":
  if shapearea == "hexagon":
    print("Hexagon formula = 3*square root of 3 divided by 2 * side of hexagon sqaured")
    hexagonside = int(input("Enter side length of hexagon: ")) 
    hexagonareaanswer = (3*math.sqrt(3)/2*hexagonside**2)  
    print("Hexagon area = " + "3 * the square root of 3 divided by 2 * " + str(hexagonside) + " = " + str(hexagonareaanswer) ) 

if mathquestion == "area":
  if shapearea == "octagon":
    print("Octagon formula = 2 * (1 + square root of 2)* side squared")
    octagonside = int(input("Enter side length of Octagon: ")) 
    octagonareaanswer  = (1 + math.sqrt(2)) 
    octagonareaanswer2 = (2*octagonareaanswer) 
    octagonareaanswer3 = (octagonareaanswer2 * octagonside**2)
    print("2 * (1 + sqaure root of 2) * " + str(octagonareaanswer3))  


# import complex math module
import cmath

if mathquestion == "quadratic formula":
 a = int(input("enter a: "))
 b = int(input("enber b: "))
 c = int(input("enter c: "))  

# calculate the discriminant
 d = (b**2) - (4*a*c)

# find two solutions
 sol1 = (-b-cmath.sqrt(d))/(2*a)
 sol2 = (-b+cmath.sqrt(d))/(2*a)

 print('The solution are {0} and {1}'.format(sol1,sol2)) 
