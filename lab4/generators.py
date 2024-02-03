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





