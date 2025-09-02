class Account:
    def __init__(self, username):
        self.username = username
        self.balance = 0.0
        self.transactions = []
        self.holdings = {}
        self.initial_deposit = 0.0

    def deposit_funds(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.initial_deposit += amount if self.initial_deposit == 0 else 0
        self.transactions.append({"type": "deposit", "amount": amount})

    def withdraw_funds(self, amount):
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            return False
        self.balance -= amount
        self.transactions.append({"type": "withdrawal", "amount": amount})
        return True

    def buy_shares(self, symbol, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        price_per_share = get_share_price(symbol)
        total_cost = price_per_share * quantity
        if total_cost > self.balance:
            return False
        self.balance -= total_cost
        self.holdings[symbol] = self.holdings.get(symbol, 0) + quantity
        self.transactions.append({"type": "buy", "symbol": symbol, "quantity": quantity, "price": price_per_share})
        return True

    def sell_shares(self, symbol, quantity):
        if quantity <= 0:
            raise ValueError("Quantity must be positive")
        if self.holdings.get(symbol, 0) < quantity:
            return False
        price_per_share = get_share_price(symbol)
        self.balance += price_per_share * quantity
        self.holdings[symbol] -= quantity
        if self.holdings[symbol] == 0:
            del self.holdings[symbol]
        self.transactions.append({"type": "sell", "symbol": symbol, "quantity": quantity, "price": price_per_share})
        return True

    def calculate_portfolio_value(self):
        value = sum(quantity * get_share_price(symbol) for symbol, quantity in self.holdings.items())
        return value

    def calculate_profit_loss(self):
        return self.balance + self.calculate_portfolio_value() - self.initial_deposit

    def get_holdings(self):
        return dict(self.holdings)

    def get_profit_loss(self):
        return self.calculate_profit_loss()

    def list_transactions(self):
        return list(self.transactions)

def get_share_price(symbol):
    prices = {"AAPL": 150.0, "TSLA": 700.0, "GOOGL": 2700.0}
    return prices.get(symbol, 0.0)