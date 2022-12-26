import sys
import sqlite3

conD = sqlite3.connect("TEST-BACKUP/3d/3d0d7e5fb2ce288813306e4d4636395e047a3d28")
curD = conD.cursor()

try:
    resD = curD.execute("SELECT ROWID FROM message")
    if resD.fetchone() is None:
        print("Connection Unsuccessful")
        sys.exit(1)
    resD = curD.execute("SELECT ROWID FROM chat")
    if resD.fetchone() is None:
        print("Connection Unsuccessful")
        sys.exit(1)
    resD = curD.execute("SELECT ROWID FROM chat_message_join")
    if resD.fetchone() is None:
        print("Connection Unsuccessful")
        sys.exit(1)
    print("Connection Successful")
except:
    print("Connection Unsuccessful")
    sys.exit(1)

conB = sqlite3.connect("backupMessages.db")
curB = conB.cursor()

curB.execute("""CREATE TABLE messages (
    message_id INTEGER,
    chat_id INTEGER,
    handle_id INTEGER,
    phone_number TEXT,
    display_name INTEGER,
    is_from_me INTEGER,
    date TEXT,
    text TEXT
);""")
