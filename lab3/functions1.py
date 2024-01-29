def ounces(gramm):
    result = gramm/28.3495231
    
    return result

print(ounces(28.3495231))

def temperature(F):
    C=(F-32)*(5/9)
    return C

#  F 68  = > C 20 I calculate this in Google
print(temperature(68))


def heads(head, legs):
    for i in range(1,head):
        if i*2 + (head-i)*4==legs:
            return f"chicken {i}, rabbits {head-i} "

print(heads(35, 94))


def prime(slot):

    slot=list(slot.split())
    slot=map(int, slot)

    result = []

    for i in slot:
        flag = True
        for j in range(2, i):
            if i%j==0:
                flag=False
        if flag:
            result.append(i)

    return result

print(prime("1 2 3 4 5 6 7 8 9 10 11 12 13 14 15")) 


def permutations(some_s):
    n = len(some_s)

    for i in range(n):
        for j in range(n):
            print(some_s[(j-i)], end=" ")
        print()

permutations("Tommy")

def _reverse(strings):
    strings=list(strings.split())
    strings.reverse()
    for i in strings:
        print(i, end=" ")

_reverse("Hello I am KBTU student")

def has33(arr):
    flag = False
    for i in range(len(arr)-1):
        if arr[i]==arr[i+1] and arr[i]==3:
            flag = True
    if flag:
        print("True")
    else:
        print("False")

print("\n")


has33([1,3,3])
has33([1, 3, 1, 3])
has33([3, 1, 3])


