class Account:
    def __init__(self,name: str):

        self.__account_name = name
        self.__account_balance = 0


    def deposit(self,amount: float) -> bool:

        """
        This function deposits money into the users account
        
        :param amount: This is the amount the user wants to deposits

        :Return: Returns Boolean true or false depending on if the money was deposited

        """

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


    def withdrawl(self,amount: float) -> bool:



        """
        This function withdrawls money from the users account

        :param amount: This is the amount of money the user wants to withdrawl

        :Return: This function will return true or false depending on if the withdrawl was successful

        """
        try:
            float(amount)
            self.__withdrawl_amount = amount


            if self.__account_balance <= 0:
                return False

            elif self.__withdrawl_amount <= self.__account_balance:
                self.__account_balance = self.__account_balance - self.__withdrawl_amount
                return True

            elif self.__withdrawl_amount > self.__account_balance:
                return False

        except:
            return False

    def get_balance(self) -> float:


        """
        This function retreives the users account balance
        
        :Return: this will return the account balance

        """
        return self.__account_balance

    def get_name(self) -> str:

        """
        This function retreives the account name

        :Return: this will return the account name
        
        """
        return self.__account_name