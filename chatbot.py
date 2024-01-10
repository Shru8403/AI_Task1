import random
# Updated banking data with more accounts and transactions
bank_data = {
    '123456789': {'name': 'John Doe', 'balance': 1000, 'transactions': ['Transaction: + Rs 500 (Deposit)', 'Transaction: - Rs 200 (Withdrawal)']},
    '987654321': {'name': 'Jane Smith', 'balance': 500, 'transactions': ['Transaction: + Rs 300 (Deposit)', 'Transaction: + Rs 200 (Deposit)']},
    '111223344': {'name': 'Alice Johnson', 'balance': 1500, 'transactions': []},
    '444556677': {'name': 'Bob Williams', 'balance': 200, 'transactions': []},
    '555667788': {'name': 'Eva Davis', 'balance': 800, 'transactions': []},
    '999888777': {'name': 'Michael Brown', 'balance': 1200, 'transactions': []},
    '333222111': {'name': 'Sophia Miller', 'balance': 300, 'transactions': ['Transaction: + Rs 100 (Deposit)', 'Transaction: - Rs 50 (Withdrawal)']},
    '777666555': {'name': 'David Wilson', 'balance': 100, 'transactions': ['Transaction: + Rs 50 (Deposit)', 'Transaction: - Rs 30 (Withdrawal)']}
}

def greet():
    responses = ["Hello! I'm your Banking Virtual Assistant.",
                 "Welcome! How can I assist you today?",
                 "Hi there! What can I do for you?"]
    return random.choice(responses)

def get_min_max_balance_holders():
    min_balance_holder = min(bank_data, key=lambda k: bank_data[k]['balance'])
    max_balance_holder = max(bank_data, key=lambda k: bank_data[k]['balance'])

    return min_balance_holder, max_balance_holder

def get_account_info(account_number):
    account_info = bank_data.get(account_number)
    if account_info:
        return f"Account Holder: {account_info['name']}\nAccount Balance: Rs {account_info['balance']}"
    else:
        return "Account not found. Please check your account number."

def get_transaction_history(account_number):
    account_info = bank_data.get(account_number)
    if account_info:
        transactions = account_info['transactions']
        if transactions:
            return "\n".join(transactions)
        else:
            return "No transactions found for this account."
    else:
        return "Account not found. Please check your account number."

def perform_transaction(account_number, amount):
    account_info = bank_data.get(account_number)
    if account_info:
        account_info['balance'] += amount
        transaction_description = f"Transaction: + Rs {amount} (Deposit)"
        account_info['transactions'].append(transaction_description)
        return f"Transaction successful. New balance: Rs {account_info['balance']}"
    else:
        return "Account not found. Please check your account number."

def chat():
    print(greet())

    while True:
        user_input = input("You: ")

        if user_input.lower() in ['bye', 'exit', 'quit']:
            print("Goodbye! Have a great day.")
            break
        elif 'account holder with minimum balance' in user_input.lower():
            min_holder = get_min_max_balance_holders()[0]
            min_balance = bank_data[min_holder]['balance']
            print(f"Bot: Account holder with the minimum balance: {bank_data[min_holder]['name']} (Rs {min_balance})")
        elif 'account holder with maximum balance' in user_input.lower():
            max_holder = get_min_max_balance_holders()[1]
            max_balance = bank_data[max_holder]['balance']
            print(f"Bot: Account holder with the maximum balance: {bank_data[max_holder]['name']} (Rs {max_balance})")
        elif 'what is my account balance?' in user_input.lower():
            account_number = input("Enter your account number: ")
            response = get_account_info(account_number)
            print(f"Bot: {response}")
        elif 'show me my transaction history?' in user_input.lower():
            account_number = input("Enter your account number: ")
            response = get_transaction_history(account_number)
            print(f"Bot: {response}")
        elif 'i want to make a deposit' in user_input.lower():
            account_number = input("Enter your account number: ")
            amount = int(input("Enter the deposit amount: "))
            response = perform_transaction(account_number, amount)
            print(f"Bot: {response}")
        else:
            print("Bot: I'm not sure how to respond to that. Ask me something else!")

if __name__ == "__main__":
    chat()