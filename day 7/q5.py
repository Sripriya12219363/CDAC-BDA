import sqlite3
from datetime import datetime

class TransactionError(Exception):
    pass

class BankingLedger:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS accounts (
                account_id TEXT PRIMARY KEY,
                holder_name TEXT,
                balance REAL
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS audit_log (
                tx_id INTEGER PRIMARY KEY AUTOINCREMENT,
                from_acc TEXT,
                to_acc TEXT,
                amount REAL,
                timestamp TEXT
            )
        """)

        self.conn.commit()

    def create_account(self, account_id, holder_name, initial_deposit):
        if initial_deposit < 0:
            raise ValueError("Initial deposit cannot be negative.")
        self.cursor.execute(
            """
            INSERT INTO accounts (account_id, holder_name, balance)
            VALUES (?, ?, ?)
            """,
            (account_id, holder_name, initial_deposit)
        )
        self.conn.commit()

    def transfer_funds(self, from_acc, to_acc, amount):
        try:
            if amount <= 0:
                raise TransactionError("Transfer amount must be positive.")
            self.cursor.execute(
                "SELECT balance FROM accounts WHERE account_id = ?",
                (from_acc,)
            )
            from_account = self.cursor.fetchone()
            if from_account is None:
                raise TransactionError(
                    f"Account {from_acc} does not exist."
                )
            self.cursor.execute(
                "SELECT balance FROM accounts WHERE account_id = ?",
                (to_acc,)
            )
            to_account = self.cursor.fetchone()
            if to_account is None:
                raise TransactionError(
                    f"Account {to_acc} does not exist."
                )

            if from_account[0] < amount:
                raise TransactionError(
                    f"Insufficient funds in account {from_acc}"
                )

            self.cursor.execute(
                """
                UPDATE accounts
                SET balance = balance - ?
                WHERE account_id = ?
                """,
                (amount, from_acc)
            )
            self.cursor.execute(
                """
                UPDATE accounts
                SET balance = balance + ?
                WHERE account_id = ?
                """,
                (amount, to_acc)
            )
            self.cursor.execute(
                """
                INSERT INTO audit_log
                (from_acc, to_acc, amount, timestamp)
                VALUES (?, ?, ?, ?)
                """,
                (from_acc, to_acc, amount, datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
            )
            self.conn.commit()
        except TransactionError:
            self.conn.rollback()
            raise
    def get_balance(self, account_id):
        self.cursor.execute(
            "SELECT balance FROM accounts WHERE account_id = ?",
            (account_id,)
        )
        row = self.cursor.fetchone()
        if row is None:
            raise TransactionError(
                f"Account {account_id} does not exist."
            )
        return row[0]

def main():
    bank = BankingLedger("bank.db")
    bank.create_account("ACC101", "Arham", 5000.0)
    bank.create_account("ACC102", "Lisa", 2000.0)
    bank.transfer_funds("ACC101", "ACC102", 1500.0)
    print(bank.get_balance("ACC101"))
    print(bank.get_balance("ACC102"))
    try:
        bank.transfer_funds("ACC101", "ACC102", 10000.0)
    except TransactionError as e:
        print(e)
    print(bank.get_balance("ACC101"))
    print(bank.get_balance("ACC102"))
    bank.conn.close()

main()