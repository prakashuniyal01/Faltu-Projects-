# User registration signin signed up
from database import *
from customer import *
from bank import Bank
import random

def SignUp():
    username = input('create username: ')
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        print('Username already exists. Please try again.')
        SignUp()
    else:
        print('Username is Available Please proceed')
        password = input('create password: ')
        name = input('full name: ')
        age = int(input('age: '))
        city = input('city: ')
        while True:
            account_number = random.randint(00000000, 99999999)
            temp = db_query(f"SELECT account_number from customers where account_number = '{account_number}';")
            if temp:
                continue
            else:
                print(account_number)
                break
    
    cusObj = Customer(username, password, name, age, city, account_number )
    cusObj.createuser()
    bobj = Bank(username, account_number)
    bobj.create_transaction_table()
    
def SignIn():
    username = input('enter username: ')
    temp = db_query(f"SELECT username FROM customers where username = '{username}';")
    if temp:
        while True:
            password = input(f'Welcome {username.capitalize()} please enter your password:  ')
            temp = db_query(f"SELECT password FROM customers where username = '{username}';")
            # print('Login Successful')
            # print(temp[0][0])
            if temp[0][0] == password:
                print('Login Successful')
                return username
            else:
                print('Invalid password. Please try again.')
                continue
            
    else:
        print('Invalid credentials. Please try again.')
        SignIn()
# SignUp()