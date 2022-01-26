# https://leetcode.com/problems/simple-bank-system/

class Bank:
    def __init__(self, balance: list[int]):
        self.balances = balance

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        try:
            acc_1_idx = self._get_account_idx(account1)
            acc_2_idx = self._get_account_idx(account2)
        except ValueError:
            return False
        if self.balances[acc_1_idx] < money:
            return False
        if acc_1_idx != acc_2_idx:
            self.balances[acc_1_idx] -= money
            self.balances[acc_2_idx] += money
        return True

    def deposit(self, account: int, money: int) -> bool:
        try:
            acc_idx = self._get_account_idx(account)
        except ValueError:
            return False
        self.balances[acc_idx] += money
        return True

    def withdraw(self, account: int, money: int) -> bool:
        try:
            acc_idx = self._get_account_idx(account)
        except ValueError:
            return False
        if self.balances[acc_idx] < money:
            return False
        self.balances[acc_idx] -= money
        return True

    def _get_account_idx(self, account: int) -> int:
        if 1 <= account <= len(self.balances):
            return account - 1
        raise ValueError(f'Account {account} does not exist')
