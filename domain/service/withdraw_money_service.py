from domain.model.base.role import Role
from domain.model.account.money_collector import MoneyCollector
from domain.model.account import account_repo


class WithdrawMoneyService(object):

    def __init__(self):
        self.repo = account_repo.get()

    def execute(self, account_id, amount):
        account = self.repo.get(account_id)
        Role.cast(account, MoneyCollector).withdraw(amount)

    def get_amount(self, account_id):
        account = self.repo.get(account_id)
        return Role.cast(account, MoneyCollector).get_amount()