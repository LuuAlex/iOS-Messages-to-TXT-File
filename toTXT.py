import sys
import sqlite3


try:
    con = sqlite3.connect("MESSAGE_STORAGE/backupMessages.db")
    cur = con.cursor()
    cur.execute("SELECT * FROM messages")
    print(" --- Connected to backupMessages.db --- ")
except:
    print(" !!! Failed to Connect to backupMessages.db !!! ")
    sys.exit(1)


cur2 = con.cursor()
cur.execute("SELECT DISTINCT chat_id FROM messages")
for row in cur:
    cur2.execute(f"""SELECT * FROM messages WHERE chat_id = {row[0]}""")
    txt = open("MESSAGE_STORAGE/" + str(row[0]) + ".txt", "w")
    for row2 in cur2:
        if int(row2[5]) == 1:
            txt.write(f"ME ({row2[7]}): {row2[8]}" + "\n\n")
        else:
            txt.write(f"{row2[3]} ({row2[7]}): {row2[8]}" + "\n\n")


print(" --- SUCCESSFULLY CREATED AND FORMATTED TXT FILES! --- ")
print()
print()

input("Press enter to exit...")
