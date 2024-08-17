import random 
n = random.randint(1 , 100)
a = -1
gussess = 0

while(a != n):
    a = int(input("Guss the number: "))
    if(a > n):
        print("Lower number Please")
    elif (a == n):
        print("great")
    else: 
        print("Higher number Please")
    gussess += 1

print(f'You have gussed the number {n} currectly in {gussess} attempts')