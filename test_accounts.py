
import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('test_user', 1000)

    def test_initial_balance(self):
        self.assertEqual(self.account.balance, 1000)

    def test_deposit(self):
        self.account.deposit(500)
        self.assertEqual(self.account.balance, 1500)

    def test_deposit_negative(self):
        with self.assertRaises(ValueError):
            self.account.deposit(-100)

    def test_withdraw(self):
        self.account.withdraw(200)
        self.assertEqual(self.account.balance, 800)

    def test_withdraw_exceeds_balance(self):
        with self.assertRaises(ValueError):
            self.account.withdraw(2000)

    def test_buy_shares(self):
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.balance, 700)
        self.assertEqual(self.account.holdings['AAPL'], 2)

    def test_buy_shares_insufficient_funds(self):
        with self.assertRaises(ValueError):
            self.account.buy_shares('AAPL', 10)

    def test_sell_shares(self):
        self.account.buy_shares('AAPL', 2)
        self.account.sell_shares('AAPL', 1)
        self.assertEqual(self.account.holdings['AAPL'], 1)
        self.assertEqual(self.account.balance, 850)

    def test_sell_shares_not_enough(self):
        self.account.buy_shares('AAPL', 1)
        with self.assertRaises(ValueError):
            self.account.sell_shares('AAPL', 2)

    def test_total_portfolio_value(self):
        self.account.deposit(1000)
        self.account.buy_shares('AAPL', 1)
        self.assertEqual(self.account.total_portfolio_value(), 1000 + 150)

    def test_profit_or_loss(self):
        self.account.deposit(1000)
        self.account.buy_shares('AAPL', 1)
        self.assertEqual(self.account.profit_or_loss(), 150)

    def test_report_holdings(self):
        self.account.buy_shares('AAPL', 2)
        self.assertEqual(self.account.report_holdings(), {'AAPL': 2})

    def test_list_transactions(self):
        self.account.deposit(500)
        self.account.withdraw(200)
        transactions = self.account.list_transactions()
        self.assertIn('Deposited: 500', transactions)
        self.assertIn('Withdrew: 200', transactions)

if __name__ == '__main__':
    unittest.main()
