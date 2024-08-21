from register import *
from bank import *
status = False
print('welcome to the banking menangement system')
while True:
    try:
       register = int(input("1. Register\n2. SignIn  ")) 
       if register == 1 or register == 2:
           if register == 1:
               SignUp()
           elif register == 2:
               user = SignIn()
               status = True
               print(f"wecome to our bank  ")
               break
       else:
           print("Invalid choice. Please try again.")
           continue
    except ValueError:
       print("Invalid choice. Please enter a number.")
       continue
   
account_number = db_query(f"SELECT account_number FROM customers WHERE username = '{user}';")
print(account_number[0][0])



while status:
    print(f"Welcome to {user.capitalize()} for choosing our banking services ")
    try:
       facility = int(input("1. balance enquiry\n2. cash deposit\n3. cash withdrawal\n4, fund transfer ")) 
       if facility >= 1 or facility <= 4:
           if facility == 1:
              bobj = Bank(user, account_number[0][0])
              bobj.balanceequiry()
           elif facility == 2:
               while True:
                   try:
                       amount = int(input("enter your amount how can you deposit"))
                       bobj = Bank(user, account_number[0][0])
                       bobj.deposit(amount)
                       break
                   except ValueError:
                       print("Invalid choice. Please enter a number.")
                       continue
           elif facility == 3:
               while True:
                   try:
                       amount = int(input("enter your amount how can you withdraw"))
                       bobj = Bank(user, account_number[0][0])
                       bobj.withdrow(amount)
                       break
                   except ValueError:
                       print("Invalid choice. Please enter a number.")
                       continue
            #    amount = int(input("enter your amount how can you withdraw"))
            #    bobj = Bank(user, account_number[0][0])
            #    bobj.withdrow(amount)
           elif facility == 4:
               while True:
                   try:
                       receive = int(input("Enter receiving account number"))
                       amount = int(input("Enter tranfar money amount"))
                       bobj = Bank(user, account_number[0][0])
                       bobj.fundtransfer(receive, receive)
                       break
                   except ValueError:
                       print("Invalid choice. Please enter a number.")
                       continue
       else:
           print("Invalid choice. Please try again.")
           continue
    except ValueError:
       print("Invalid choice. Please enter a number.")
       continue