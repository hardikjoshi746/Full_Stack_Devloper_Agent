import unittest
from accounts import Account, get_share_price

class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account = Account('test_user')

    def test_initial_state(self):
        self.assertEqual(self.account.balance, 0.0)
        self.assertEqual(self.account.transactions, [])
        self.assertEqual(self.account.holdings, {})
        self.assertEqual(self.account.initial_deposit, 0.0)

    def test_deposit_positive_amount(self):
        self.account.deposit_funds(100.0)
        self.assertEqual(self.account.balance, 100.0)
        self.assertEqual(self.account.initial_deposit, 100.0)
        self.assertEqual(len(self.account.transactions), 1)

    def test_deposit_negative_amount(self):
        with self.assertRaises(ValueError):
            self.account.deposit_funds(-100.0)

    def test_withdraw_funds(self):
        self.account.deposit_funds(1000.0)
        result = self.account.withdraw_funds(200.0)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 800.0)
        self.assertEqual(len(self.account.transactions), 2)

    def test_withdraw_insufficient_funds(self):
        self.account.deposit_funds(100.0)
        result = self.account.withdraw_funds(200.0)
        self.assertFalse(result)

    def test_buy_shares(self):
        self.account.deposit_funds(1000.0)
        result = self.account.buy_shares('AAPL', 5)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 1000.0 - 5*150.0)
        self.assertEqual(self.account.holdings['AAPL'], 5)
        self.assertEqual(len(self.account.transactions), 2)

    def test_sell_shares(self):
        self.account.deposit_funds(1000.0)
        self.account.buy_shares('TSLA', 1)
        result = self.account.sell_shares('TSLA', 1)
        self.assertTrue(result)
        self.assertEqual(self.account.balance, 1000.0)
        self.assertEqual(self.account.holdings.get('TSLA', 0), 0)
        self.assertEqual(len(self.account.transactions), 3)

    def test_calculate_portfolio_value(self):
        self.account.deposit_funds(3000.0)
        self.account.buy_shares('GOOGL', 1)
        value = self.account.calculate_portfolio_value()
        self.assertEqual(value, 2700.0)

    def test_calculate_profit_loss(self):
        self.account.deposit_funds(3000.0)
        self.account.buy_shares('GOOGL', 1)
        profit_loss = self.account.calculate_profit_loss()
        self.assertEqual(profit_loss, 300.0)

    def test_list_transactions(self):
        self.account.deposit_funds(3000.0)
        self.assertEqual(len(self.account.list_transactions()), 1)

if __name__ == '__main__':
    unittest.main()