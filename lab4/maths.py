import math 
degree = int(input("Input degree: "))
degree = math.radians(degree)

print("Output radian: ",degree)

height =int(input("Height: "))
first = int(input("Base, first value: "))
second = int(input("Base, second value: "))

print("Expected Output: ",(first+second)/2*height)

def areapolygon():
    sides = int(input("Input number of sides: "))
    length = int(input("Input the length of a side: "))

    p = sides * length
    a = length/(2*math.tan(math.pi/sides))
    return p*a/2

area = areapolygon()
print(area)

def paralellogram():
    length = int(input("Length of base: "))
    height = int(input("Height of parallelogram: "))
    result = "Expected Output: "+str(height*length)
    return result

area_parallelogram=paralellogram()
print(area_parallelogram)
