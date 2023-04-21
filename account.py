class Account:
    def __init__(self,name):

        self.__account_name = name
        self.__account_balance = 0

    def deposit(self,amount):

        try:
            float(amount)
            self.__amount = amount

            if self.__amount <= 0:
                return False
            
            elif self.__amount > 0:
                self.__account_balance += self.__amount
                return True

        except:
            return False


    def withdrawl(self,amount):
        try:
            float(amount)
            self.__withdrawl_amount = amount

            if self.__withdrawl_amount <= self.__account_balance:
                self.__account_balance = self.__account_balance - self.__withdrawl_amount
                return True

            elif self.__withdrawl_amount > self.__account_balance:
                return False

        except:
            return False

    def get_balance(self):
        return self.__account_balance

    def get_name(self):
        return self.__account_name