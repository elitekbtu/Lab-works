
class Strings:
    def getstring(self, s):
        print(s)
    def printString(self,s):
        s=s.upper()
        print(s)

result = Strings()
result.getstring("hello world")
result.printString("hello world")



class Shape:
    def __init__(self):
        pass
        
    def area(self):
        return 0
    
    def rectangle(self):
        return self.length * self.width

class Square(Shape):
    def __init__(self, length, width):
        self.width = width
        self.length = length

    def area(self):
        return self.length * self.length

square = Square(5, 7)


print(square.area())

print(square.rectangle())




import math

class Point:
    def __init__(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2

    def show(self):
        return self.x1, self.y1, self.x2, self.y2


    def move(self):
        points=[]
        self.x1 = int(input("x1: "))
        self.y1 = int(input("y1: "))
        self.x2 = int(input("x2: "))
        self.y2 = int(input("y2: "))
        points.append(self.x1)
        points.append(self.y1)
        points.append(self.x2)
        points.append(self.y2)

        return points
    

    def dist(self):
        return math.sqrt((self.x1 - self.x2)**2 + (self.y1 - self.y2)**2)

point = Point(1,2,3,4)

print(point.show())

print(point.move())

print(point.dist())


class Bank():
    def __init__(self, account, money):
        self.money = money
        self.account = account

    def balance(self):
        return self.money
    
    def owner(self):
        return self.account
    
    def deposit(self, money):
        self.money+=money

        return f"You are deposit {money} money"
    
    def withdraw(self, money):
        if self.money - money < 0:
            return "insufficient funds"
        else:
            self.money-=money

            return f"you're balance: {self.money},  and you take {money}"
        
        
bank = Bank("Turarbek", 1000)

print(bank.balance())

print(bank.owner())

print(bank.deposit(1000))

print(bank.withdraw(3000))

print(bank.withdraw(2000))