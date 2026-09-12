import sqlite3

class UserDatabaseManager:
    def __init__(self, db_path):
        self.conn = sqlite3.connect(db_path)
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                address TEXT,
                mobile TEXT,
                email TEXT
            )
        """)
        self.conn.commit()
    def find_user(self, username):
        self.cursor.execute(
            "SELECT * FROM users WHERE username = ?",
            (username,)
        )
        row = self.cursor.fetchone()
        if row is None:
            return None
        return {
            "id": row[0],
            "username": row[1],
            "address": row[2],
            "mobile": row[3],
            "email": row[4]
        }
    def add_or_update_user(self, username, address, mobile, email):
        user = self.find_user(username)
        if user is not None:
            self.cursor.execute(
                """
                UPDATE users
                SET address = ?, mobile = ?, email = ?
                WHERE username = ?
                """,
                (address, mobile, email, username)
            )
            self.conn.commit()
            return "UPDATED"
        self.cursor.execute(
            """
            INSERT INTO users (username, address, mobile, email)
            VALUES (?, ?, ?, ?)
            """,
            (username, address, mobile, email)
        )
        self.conn.commit()
        return "INSERTED"

    def list_all_users(self):
        self.cursor.execute(
            "SELECT * FROM users ORDER BY username"
        )
        rows = self.cursor.fetchall()
        users = []
        for row in rows:
            user = {
                "id": row[0],
                "username": row[1],
                "address": row[2],
                "mobile": row[3],
                "email": row[4]
            }
            users.append(user)
        return users

def main():
    db = UserDatabaseManager("company.db")
    status1 = db.add_or_update_user(
        "arham_k",
        "Pune, MH",
        "9876543210",
        "arham@cdac.in"
    )
    print(status1)
    user_info = db.find_user("arham_k")
    print(user_info["email"])
    status2 = db.add_or_update_user(
        "arham_k",
        "Bengaluru, KA",
        "9876543210",
        "arham@cdac.in"
    )
    print(status2)
    print(db.list_all_users())
    db.conn.close()

main()