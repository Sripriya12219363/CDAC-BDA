audit_transaction = 0
def create_bank_account(owner_name, initial_balance):
    bal = float(initial_balance)
    his = [f"Account created with {initial_balance}"]
    def deposit(amount):
        global audit_transaction
        nonlocal bal, his
        bal += amount
        his.append(f"deposit {amount}")
        audit_transaction += 1
    def withdraw(amount):
        global audit_transaction
        nonlocal bal, his
        if bal >= amount:
            bal -= amount
            his.append(f"withdraw {amount}")
            audit_transaction += 1
        else:
            raise ValueError("Insufficient balance")
    def get_statement():
        return owner_name, bal, his.copy()
    return {
        "deposit": deposit,
        "withdraw": withdraw,
        "statement": get_statement
    }
def main():
    print(audit_transaction)
    acc = create_bank_account("Arham", 1000.0)
    acc["deposit"](200.0)
    acc["withdraw"](150.0)
    try:
        acc["withdraw"](2000.0)
    except ValueError as e:
        print(e)
    owner, bal, txn_history = acc["statement"]()
    print(owner)
    print(bal)
    print(txn_history)
    print(audit_transaction)

main()