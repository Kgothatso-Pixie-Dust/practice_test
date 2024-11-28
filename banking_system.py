
# Function to deposit money into an account
def deposit(account: dict, amount: float)-> None:
    res = account['balance'] + amount

    #Or  account['balance'] += amount
    return account.update({'balance': res})

# Function to withdraw money from an account
def withdraw(account: dict, amount: float) -> None:
    res = account['balance'] - amount 
    if amount > account['balance']:
        return (account.update({'balance': res * -1})) 
    else:
        return account.update({'balance': res})   


# Function to transfer money between two accounts
def transfer(from_account: dict, to_account: dict, amount: float) -> None:
    ans = from_account['balance'] - amount
    fin = to_account['balance'] + amount
    return from_account.update({'balance': ans}) or to_account.update({'balance': fin})


# Function to add a new account to the system
def add_account(accounts: dict, owner: str, initial_balance: float) -> None:
    # accounts[owner] = accounts[]
    if owner in accounts:
        return None
    else:
        return accounts.update({owner: {'balance': initial_balance}})

    # diction = {"sam": {'hello': 'world'}}
    # return accounts.update({owner: {'balance': initial_balance}})


# Function to find an account by owner's name
def find_account(accounts: dict, owner: str) -> dict:
    if owner in accounts:
        return accounts[owner]
    else:
        return None
        

# Function to display all accounts in the system
def display_all_accounts(accounts: dict) -> str:
    return '\n'.join([f"{owner}: {account['balance']}" for owner, account in accounts.items()])
