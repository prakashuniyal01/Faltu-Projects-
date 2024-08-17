# year = int(input("enter you whats the check for year of leap "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print(f' is leap year {year}') 

# else :
#     print(f'not leap year {year}')


# numbers = [1,2,4,-1,-12,-14,-4,-6,4,6]


# positive_number_count = 0

# for num in numbers:
#     if num > 0:
#         positive_number_count +=1
# print (f'final count {positive_number_count}')



n = 111

sum_even = 0

for i in range(1, n+1):
    if i % 2 == 0:
        sum_even += 1
        print(i)

print(f'even is {sum_even}')