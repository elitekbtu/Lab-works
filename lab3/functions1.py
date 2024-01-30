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

print('\n')

def order007(arr):
    result = []
    for i in arr:
        if i==0 or i==7:
            result.append(i)
    
    flag =  False
    for i in range(len(result)-2):
        if result[i]==result[i+1] and result[i]==0 and result[i+2]==7:
            flag = True
        
    if flag:
        print("True")
    else:
        print("False")

order007([1,2,4,0,0,7,5])
order007([1,0,2,4,0,5,7])
order007([1,7,2,0,4,5,0])

def volume(r):
    pi = 3.1415
    r=4/3*r**3*pi
    print(r)

volume(3)


def _unique(arr):
    result = []
    for i in arr:
        if arr.count(i)==1:
            result.append(i)
    print(result)


_unique([1,2,4,0,0,7,5])
_unique([1,2,5,7,4,5,4,2,9])


def palindrom(strings):
    if strings==strings[::-1]:
        print("YES")
    else:
        print("NO")

palindrom("madam")
palindrom("qazaq")
palindrom("result")



def histogram(arr):
    for i in arr:
        print("*"*i)
histogram([1,2,3,4,5,6])



from random import randint

def guessanumber():
    print("Hello! What is your name?")
    name = input()
    print(f"Well, {name}, I am thinking of a number between 1 and 20.")
    number = randint(1,20)
    sum = 0
    run = True
    while run:
        guess = int(input("Take a guess: "))
        sum+=1
        if guess == number:
            run = False
            print(f"Good job, {name}! You guessed my number in {sum} guesses!")
            break
        if guess>number:
            print("Your guess is too high.")
        else:
            print("Your guess is too low")


guessanumber()

def randomator(start, end, length):
    arr=[randint(start, end)for i in range(length)]
    print(arr)
randomator(1,10,10)