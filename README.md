# iOS-Messages-to-TXT-File
iOS Messages to TXT File is a tool to convert any iOS message backup file to a 
.txt file. 

When backing up, data from the iOS backup folder (named BACKUP) 
are joined to an database file (backupMessages.db) that the 
program creates, updates and stores for you. 
This database contains all the message history. 
When running the program again, from a new backup file, the program will 
automatically add missing messages to the stored database.


## Warnings (Read Carefully)
* **DO NOT** *delete* OR *modify* OR *move* the backup folder in any way. This can corrupt your iOS backup file, rendering you unable to restore the backup
* This program can potentially modify the backup file. **BE SURE** to ***MAKE A COPY*** of the backup file by using *copy/paste*. **DO NOT** *move* the backup file

## How to Use:
1. Download this repo as a zip file and unzip on your computer.
2. Find the backup folder for your iOS device and ***copy/paste*** the entire backup folder in the unzipped folder.
   * **On Mac**: Finder -> Go to Folder... -> ~/Library/Application Support/MobileSync/Backup
   * **On Windows**:
   * The file name of the backup folder is something similar to: XXXXXXXX-XXXXXXXXXXXXXXXX
3. Rename the backup file as: ***DATA_TO_BACKUP***
4. Run ***backupData.py***. Ensure no errors appear.
   * The messages are now stored in ***backupMessages.db***
5. When you make a new backup of your phone, repeat step 2-4 and the new messages will be added to ***backupMessages.db***