from accounts import Account
import gradio as gr

# Example: Defining the backend account object
account = Account(username='test_user')

# Define functions to interact with backend
def create_account(username):
    global account
    account = Account(username)
    return f"Account created for {username}."

def deposit_funds(amount):
    try:
        account.deposit_funds(float(amount))
        return f"Deposited {amount}. Current balance: {account.balance}"
    except Exception as e:
        return str(e)

def withdraw_funds(amount):
    try:
        if account.withdraw_funds(float(amount)):
            return f"Withdrew {amount}. Current balance: {account.balance}"
        else:
            return "Insufficient funds."
    except Exception as e:
        return str(e)

def buy_shares(symbol, quantity):
    try:
        if account.buy_shares(symbol, int(quantity)):
            return f"Bought {quantity} shares of {symbol}. Current balance: {account.balance}"
        else:
            return "Insufficient funds to buy shares."
    except Exception as e:
        return str(e)

def sell_shares(symbol, quantity):
    try:
        if account.sell_shares(symbol, int(quantity)):
            return f"Sold {quantity} shares of {symbol}. Current balance: {account.balance}"
        else:
            return "Insufficient shares to sell."
    except Exception as e:
        return str(e)

def get_portfolio_value():
    return f"Total portfolio value: {account.calculate_portfolio_value()}"

def get_profit_loss():
    return f"Profit/Loss: {account.calculate_profit_loss()}"

def list_holdings():
    return str(account.get_holdings())

def list_transactions():
    return str(account.list_transactions())


# Gradio Blocks API implementation
with gr.Blocks() as demo:
    gr.Markdown("# Account Management Dashboard")
    with gr.Row():
        username = gr.Textbox(label="Username for Account Creation")
        create_btn = gr.Button("Create Account")
        create_status = gr.Textbox(label="Account Creation Status")
    create_btn.click(create_account, inputs=[username], outputs=[create_status])

    with gr.Row():
        deposit_amount = gr.Textbox(label="Amount for Deposit", value="0")
        deposit_btn = gr.Button("Deposit Funds")
        deposit_status = gr.Textbox(label="Deposit Status")
    deposit_btn.click(deposit_funds, inputs=[deposit_amount], outputs=[deposit_status])

    with gr.Row():
        withdraw_amount = gr.Textbox(label="Amount for Withdrawal", value="0")
        withdraw_btn = gr.Button("Withdraw Funds")
        withdraw_status = gr.Textbox(label="Withdrawal Status")
    withdraw_btn.click(withdraw_funds, inputs=[withdraw_amount], outputs=[withdraw_status])

    with gr.Row():
        buy_symbol = gr.Textbox(label="Symbol for Buying Shares", value="AAPL")
        buy_quantity = gr.Textbox(label="Quantity for Buying Shares", value="0")
        buy_btn = gr.Button("Buy Shares")
        buy_status = gr.Textbox(label="Buy Shares Status")
    buy_btn.click(buy_shares, inputs=[buy_symbol, buy_quantity], outputs=[buy_status])

    with gr.Row():
        sell_symbol = gr.Textbox(label="Symbol for Selling Shares", value="AAPL")
        sell_quantity = gr.Textbox(label="Quantity for Selling Shares", value="0")
        sell_btn = gr.Button("Sell Shares")
        sell_status = gr.Textbox(label="Sell Shares Status")
    sell_btn.click(sell_shares, inputs=[sell_symbol, sell_quantity], outputs=[sell_status])

    with gr.Row():
        portfolio_btn = gr.Button("Get Portfolio Value")
        portfolio_value = gr.Textbox(label="Portfolio Value")
    portfolio_btn.click(get_portfolio_value, inputs=[], outputs=[portfolio_value])

    with gr.Row():
        profit_btn = gr.Button("Get Profit/Loss")
        profit_loss = gr.Textbox(label="Profit/Loss")
    profit_btn.click(get_profit_loss, inputs=[], outputs=[profit_loss])

    with gr.Row():
        holdings_btn = gr.Button("List Holdings")
        holdings = gr.Textbox(label="Holdings")
    holdings_btn.click(list_holdings, inputs=[], outputs=[holdings])

    with gr.Row():
        transactions_btn = gr.Button("List Transactions")
        transactions = gr.Textbox(label="Transactions")
    transactions_btn.click(list_transactions, inputs=[], outputs=[transactions])

    gr.Markdown("---")

demo.launch()