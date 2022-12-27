import sys
import sqlite3
from datetime import datetime

print()
print(" --- Starting Script --- ")


# Convert seconds since "2001-1-1 00:00:00" to "YYYY-MM-DD HH:MM:SS" Format
def convert_datetime(sec):
    sec = sec / 1000000000
    sec += 978307200
    date = datetime.fromtimestamp(sec)
    return date.strftime("%Y-%m-%d %H:%M:%S")


# CONNECT TO iOS BACKUP FILE
conD = sqlite3.connect("DATA_TO_BACKUP/3d/3d0d7e5fb2ce288813306e4d4636395e047a3d28")
curD = conD.cursor()
try:
    resD = curD.execute("SELECT ROWID FROM message")
    if resD.fetchone() is None:
        print(" !!! Connection Unsuccessful !!! ")
        sys.exit(1)
    resD = curD.execute("SELECT ROWID FROM chat")
    if resD.fetchone() is None:
        print(" !!! Connection Unsuccessful !!! ")
        sys.exit(1)
    resD = curD.execute("SELECT ROWID FROM chat_message_join")
    if resD.fetchone() is None:
        print(" !!! Connection Unsuccessful !!! ")
        sys.exit(1)
    print(" --- Connection Successful! --- ")
except:
    print(" !!! Connection Unsuccessful !!! ")
    sys.exit(1)


# MAKE TEMP TABLES
conD.create_function("CONVERTDATETIME", 1, convert_datetime)
try:
    curD.execute("""CREATE TABLE tempX1 AS
        SELECT ROWID AS message_id, chat_id, handle_id, is_from_me, date, CONVERTDATETIME(date) AS dateF, text
        FROM message
        INNER JOIN chat_message_join
            ON message.ROWID = chat_message_join.message_id
    ;""")
    curD.execute("""CREATE TABLE tempX2 AS
        SELECT message_id, chat_id, handle_id, id AS phone_number, is_from_me, date, dateF, text
        FROM tempX1
        INNER JOIN handle
            ON tempX1.handle_id = handle.ROWID
    ;""")
    curD.execute("""CREATE TABLE tempX3 AS
        SELECT message_id, chat_id, handle_id, phone_number, display_name, is_from_me, date, dateF, text
        FROM tempX2
        INNER JOIN chat
            ON tempX2.chat_id = chat.ROWID
        ORDER BY date
    ;""")
    print(" --- Created Temp Tables! --- ")
except:
    print(" !!! Failed to Make Temp Tables !!! ")
    curD.execute("DROP TABLE IF EXISTS tempX1")
    curD.execute("DROP TABLE IF EXISTS tempX2")
    curD.execute("DROP TABLE IF EXISTS tempX3")
    sys.exit(1)


# CONNECT/MAKE BACKUPMESSAGES TABLE
conB = sqlite3.connect("backupMessages.db")
curB = conB.cursor()
try:
    curB.execute("""CREATE TABLE messages (
        message_id INTEGER NOT NULL,
        chat_id INTEGER NOT NULL,
        handle_id INTEGER NOT NULL,
        phone_number TEXT NOT NULL,
        display_name TEXT,
        is_from_me INTEGER,
        date TEXT,
        dateF TEXT,
        text TEXT,
        PRIMARY KEY (message_id, chat_id, handle_id, phone_number)
    );""")
    print(" --- New Table Made! --- ")
except:
    print(" --- Previous Table Found! --- ")


# ADD TEMPX3 TABLE TO BACKUPMESSAGES TABLE
curD.execute("SELECT * FROM tempX3")
data = curD.fetchall()

fields = ','.join('?' for desc in curD.description)
curB.executemany("INSERT OR IGNORE INTO messages values ({})".format(fields), data)
conB.commit()

# CLEANUP AND CLOSE
curD.execute("DROP TABLE IF EXISTS tempX1")
curD.execute("DROP TABLE IF EXISTS tempX2")
curD.execute("DROP TABLE IF EXISTS tempX3")
conD.close()
conB.close()

print(" --- SUCCESSFULLY BACKED UP MESSAGES! --- ")
print()
print()

input("Press enter to exit...")
