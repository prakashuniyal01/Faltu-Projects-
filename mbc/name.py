# a = 3

# age = float(input('Enter your age : '))

# if(age>=18):
#     print("you are above the age of consent")
#     print("good to go")
# elif(age < 0):
#     print('you are entering invalid number')
# elif(age == 0):
#     print("You are entering 0 which is not valid age")
# else:
#     print("you are below the age of consent")

num = int(input('Enter the number : '))


# for i in range(num):
#     if(i % 2 == 0 ):
#         continue
#     print(i)

def factorial(num):
    if (num == 1 or num == 0):
        return 1
    return num * factorial(num - 1)

print(f'{num} factorial is {factorial(num)}')