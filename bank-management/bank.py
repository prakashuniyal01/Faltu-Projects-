from database import *
import datetime


class Bank:
    def __init__(self, username, account_number):
        self.__username = username
        self.__account_number = account_number
        
    def create_transaction_table(self):
        db_query(f"CREATE TABLE IF NOT EXISTS {self.__username}_transaction "
                 f"( timedate VARCHAR(30),"
                 f"account_number INTEGER,"
                 f"remarks VARCHAR(30),"
                 f"amount INTEGER )")
    
    def balanceequiry(self):
        temp = db_query(f"select balance from customers where username = '{self.__username}';")
        print(f'{self.__username} balance = {temp[0][0]}')
    
    # def deposit(self,  amount):
    #     temp = db_query(f"select balance from customers where username = '{self.__username}';")
    #     test =  amount + temp[0][0]
    #     db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}';")
    #     self.balanceequiry()
    #     db_query(f"insert into {self.__username}_transaction values ("
    #              f"'{datetime.datetime.now()}',"
    #              f"'{self.__account_number}',"
    #              f"'Deposit',"
    #              f"'{amount}';")
    #     print(f'{self.__username} ammount is successfully deposit into your accunt"' )
    def deposit(self, amount):
        temp = db_query(
            f"SELECT balance FROM customers WHERE username = '{self.__username}';")
        test = amount + temp[0][0]
        db_query(
            f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}'; ")
        self.balanceequiry()
        db_query(f"INSERT INTO {self.__username}_transaction VALUES ("
                 f"'{datetime.datetime.now()}',"
                 f"'{self.__account_number}',"
                 f"'Amount Deposit',"
                 f"'{amount}'"
                 f")")
        print(f"{self.__username} Amount is Sucessfully Depositted into Your Account {self.__account_number}")

        
    
    def withdrow(self,amount):
        temp = db_query(f"select balance from customers where username = '{self.__username}';")
        if amount >= temp[0][0]:
            print('Insufficient balance')
        else:
            # print('Transaction Successful')
            test =  amount - temp[0][0]
            self.balanceequiry()
            db_query(f"UPDATE customers SET balance = '{test}' WHERE username = '{self.__username}';")
            self.balanceequiry()
            db_query(f"insert into {self.__username}_transaction values ("
                    f"'{datetime.datetime.now()}',"
                    f"'{self.__account_number}',"
                    f"'withdrow',"
                    f"'{amount}';")
            print(f'{self.__username} ammount is successfully withdrow into your accunt"' )
            
        
    def fundtransfer (self,amount, receive):
        temp = db_query(f"select balance from customers where username = '{self.__username}';")
        if amount >= temp[0][0]:
            print('Insufficient balance')
        else:
            # print('Transaction Successful')
            temp2 = db_query(f"select balance from customers where account_number = '{receive}';")
            temp[0][0] -= amount
            temp2[0][0] += amount
            db_query(f"select balance from customers where username = '{self.__username}';")
            db_query(f"UPDATE customers SET balance = '{temp2[0][0]}' WHERE account_number = '{receive}';")
            self.balanceequiry()
            db_query(f"insert into {self.__username}_transaction values ("
                    f"'{datetime.datetime.now()}',"
                    f"'{self.__account_number}',"
                    f"'fund trasfar => {receive}',"
                    f"'{amount}';")
            print(f'{self.__username} ammount is successfully transections into your accunt"' )
            