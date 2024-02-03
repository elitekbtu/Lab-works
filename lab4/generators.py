def squares(n):
    import math 
    result = []
    i=1
    while i<math.sqrt(n):
        result.append(i*i)
        i+=1
    return result

results = squares(100)
print(results)

n = int(input("please input n: "))

def evens(n):
    result  = ""
    n = n//2 * 2
    for i in range(0,n+1,2):
        result += str(i)+', '
    return result[:len(result)-2]

print(evens(n))


def div34(n):
    result =[0]
    for i in range(3, n+1):
        c = i
        while c>1:
            if c%3==0:
                c/=3 
            elif c%4==0:
                c/=4
            else:
                break

        if c==1:
            result.append(i)
    return result

n = int(input("please input n: "))
print(div34(n))

a, b = map(int, input("please input a and b: ").split())


def squares(n, m):
    for i in range(n, m+1):
        yield i**2
    
generator = squares(a, b)
for i in generator:
    print(i)

def all(n):
    for i in range(n, -1, -1):
        yield i

n = int(input("please input n: "))    
generator = all(n)

for i in generator:
    print(i)






