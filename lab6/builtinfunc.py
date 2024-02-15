def multi(array):
    s = 1
    for i in range(len(array)//2):
        s*=array[i]
        s*=array[len(array)-1-i]
        if len(array)%2==1 and i==len(array)//2-1:
            s*=array[i+1]
    return s


def sumofletters(some_s):
    uppercase = 0
    lowercase = 0
    for i in some_s:
        if i>='A' and i<='Z':
            uppercase+=1
        elif i>='a' and i<='z':
            lowercase+=1
    result = [lowercase, uppercase]
    return result




def palindrom(some_s):
    if some_s==some_s[::-1]:
        return f"the word {some_s} is palindrom"
    else:
        return f"the word {some_s} isn't palindrom"
    

def squareroot():
    import math
    x = int(input("Input the value: "))
    y = int(input("Input the miliseconds: "))

    return f"Square root of {x} after {y} miliseconds is {math.sqrt(x)}"
    

def all_true_elements(tuple_data):
    boolean =  True
    for i in tuple_data:
        if i != True:
            boolean = False

    if boolean:
        return True
    else:
        return f"elements of tuple is different"


