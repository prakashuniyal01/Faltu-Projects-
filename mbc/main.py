file = open('prakash.txt' , 'w')

try:
    file.write("kya hal h tere")
finally:
    file.close()

with open("name.py", 'w') as file:
    file.write("a = 3")