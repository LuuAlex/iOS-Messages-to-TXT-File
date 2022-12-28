# iOS-Messages-to-TXT-File
iOS Messages to TXT File is a tool to convert any iOS message backup file to a 
.txt file. 

When backing up, data from the iOS backup folder
are joined to an database file (backupMessages.db) that the 
program creates, updates and stores for you. 
This database contains all the message history. 
When running the program again, from a new backup file, the program will 
automatically add missing messages to the stored database. After creating the database, 
the program will automatically create .txt files that represent the chat history.


## Warnings (Read Carefully)
* **DO NOT** *delete* OR *modify* OR *move* the backup folder in any way. This can corrupt your iOS backup file, rendering you unable to restore the backup
* This program can potentially modify the backup file. **BE SURE** to ***MAKE A COPY*** of the backup file by using *copy/paste*. **DO NOT** *move* the backup file.
* There are **NO** guarantees on this program's ability to back up text messages. Apple may change the structure of backup files anytime, which means this program might not always work.

## How to Use:
1. Download this repo as a zip file and unzip on your computer.
2. Find the backup folder for your iOS device and ***copy/paste*** the contents of the backup folder in the unzipped folder's ***DATA_TO_BACKUP*** directory.
   * **Instructions for Finding Backup Folder**: https://support.apple.com/en-us/HT204215
   * The file name of the backup folder is something similar to: XXXXXXXX-XXXXXXXXXXXXXXXX
   * The inside of ***DATA_TO_BACKUP*** should contain many different folders labeled: "00", "0a", "0b", ... , "01", "1a" ...
4. Run ***EXC.py*** and follow the instructions. Ensure no errors appear.
   * The messages are now stored in ***backupMessages.db***, located in the ***MESSAGE_STORAGE*** directory.
   * The program creates a single .txt file for each chat in the backup. 
   * All .txt files are located in the ***MESSAGE_STORAGE*** folder.
5. When you make a new backup of your phone, repeat step 2-4 and the new messages will be added to ***backupMessages.db***


## How it Works:
1. **backupData.py**
   * Uses SQLite commands to merge 4 tables (message, chat_message_join, handle, chat) in the 3d/3d0d7e5fb2ce288813306e4d4636395e047a3d28 database together to make a temp table.
   * Add rows in the temp table to the *backupMessages.db*.
2. **toTXT.py**
   * Take rows from *backupMessages.db* with the same *chat_id* and write the data in a .txt file. 
   * One .txt file for each chat_id.
3. **backupMessages.db**: SQLite Database with 1 table, named *messages*.
   * *message_id*: unique id for each message sent and received
   * *chat_id*: unique id for each chat group
   * *handle_id*: unique id for each person sending a message
   * *phone_number*: phone number or email of sender of message
   * *display_name*: for named group chats, the given name
   * *is_from_me*: boolean (0 or 1) indicating if user of backup sent the message
   * *date*: (date / 1000000000) represents seconds since 2001-1-1 00:00:00
   * *dateF*: formatted date to YYYY-MM-DD HH:MM:SS
   * *text*: content of text message
   * PRIMARY KEY: composite primary key using (message_id, chat_id, handle_id, phone_number)
