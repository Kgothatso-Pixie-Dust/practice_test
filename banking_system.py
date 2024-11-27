
# Function to deposit money into an account
def deposit(account: dict, amount: float)-> None:
    res = account['balance'] + amount

    #Or  account['balance'] += amount
    return account.update({'balance': res})

# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:
    res = account['balance'] - amount 
    if amount < account['balance']:
        return res 
    else:
        return res
    

    return account.update({'balance': res})

# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    pass

# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    new = accounts.update({owner: initial_balance})
    return new

# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
    if accounts[owner] not in accounts:
        return None
    else:
        accounts[owner]
        

# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return '\n'.join([f"{owner}: {account['balance']}" for owner, account in accounts.items()])
