age = int(input("enter your age "))

if(age <= 13):
    print(f'you are child {age} you are not eligible')
elif (age <= 19):
    print(f"ypu are teanage {age}")
elif(age <= 60):
    print(f'you are adult {age}')
else:
    print(f'you are senior {age}')
    
