import copy


class AccountNotFoundError(Exception):
    pass


class OverdraftError(Exception):
    pass


class InvalidTransactionError(Exception):
    pass


def process_transaction_batch(accounts, batch_list, log_path):
    backup = copy.deepcopy(accounts)

    try:
        for transaction in batch_list:
            acc = transaction["acc"]
            trans_type = transaction["type"]
            amt = transaction["amt"]

            if acc not in accounts:
                raise AccountNotFoundError(f"Account '{acc}' not found.")

            if trans_type != "deposit" and trans_type != "withdraw":
                raise InvalidTransactionError(f"Invalid transaction type '{trans_type}'.")

            if amt <= 0:
                raise InvalidTransactionError("Transaction amount must be positive.")

            if trans_type == "withdraw":
                if accounts[acc] < amt:
                    raise OverdraftError(
                        f"Insufficient funds. Account {acc} has balance {accounts[acc]}, requested {amt}."
                    )
                accounts[acc] -= amt
            else:
                accounts[acc] += amt

    except Exception as e:
        accounts.clear()
        accounts.update(backup)

        with open(log_path, "a") as file:
            file.write(
                f"[ROLLBACK] Batch aborted: {type(e).__name__} - {e}\n"
            )

        raise

    with open(log_path, "a") as file:
        file.write(
            f"[SUCCESS] Batch completed. {len(batch_list)} transaction(s) processed.\n"
        )

    return accounts


def main():
    accounts = {
        "ACC01": 100.0,
        "ACC02": 50.0
    }

    log_file = "transactions.log"

    batch_1 = [
        {"acc": "ACC01", "type": "withdraw", "amt": 30.0},
        {"acc": "ACC02", "type": "deposit", "amt": 20.0}
    ]

    try:
        accounts = process_transaction_batch(accounts, batch_1, log_file)
        print(accounts)
    except Exception as e:
        print(f"Caught: {e}")

    batch_2 = [
        {"acc": "ACC01", "type": "deposit", "amt": 50.0},
        {"acc": "ACC02", "type": "withdraw", "amt": 200.0}
    ]

    try:
        accounts = process_transaction_batch(accounts, batch_2, log_file)
    except Exception as e:
        print(f"Caught: {e}")

    print(accounts)


main()
