def generateTable(n):
    table = ""
    for i in range(1, 11):
        table += f"{n} X {i}  = {n * i}\n"

    with open(f'tables/table_{n}.txt', 'w') as f:
        f.write(table)

num = int(input('enter you generate tables : '))

for i in range( num):
    generateTable(i)