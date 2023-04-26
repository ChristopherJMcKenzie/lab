import pytest
from account import *

class Test:

    def setup_method(self):
        self.a1 = Account('John')




    def test_withdrawl(self):
        assert self.a1.withdrawl(-1) == False
        assert self.a1.withdrawl(0) == False
        assert self.a1.withdrawl(1) == False
        assert self.a1.deposit(5) == True
        assert self.a1.get_balance() == 5
        assert self.a1.withdrawl(4) == True
        assert self.a1.withdrawl('a') == False
        assert self.a1.withdrawl(.5) == True
        assert self.a1.withdrawl(.5) == True
        assert self.a1.withdrawl(1) == False


    def test_deposit(self):
        assert self.a1.deposit(10) == True
        assert self.a1.deposit(-5) == False
        assert self.a1.deposit('s') == False
        assert self.a1.deposit(0) == False
        assert self.a1.deposit(5.5) == True
        assert self.a1.deposit(-5.5) == False



