"""
author : Enes Çavuş
subject : quick automations with python
date : 23 Feb 2021
goal : to practice automating things with python script

"""


import os  # path operations
import shutil # move operations
import time  

#before you run this code, create 2 diffrent files in your desktop or any locations you prefer -> named -> folder1 and folder2
yourRootDirection = "YOUR_PATH"  # prefer this if you have both folders in a same directory, with a "/" character at the end

# path for source folder
sourceFolderPath = os.path.join(yourRootDirection, "folder1")       
# path for destionation folder                                           # can be manually joined like -> "YOUR_PATH_TO_FOLDERS/folder_name"
destionationFolderPath = os.path.join(yourRootDirection, "folder2")

def filesToTransfer(filesToMove):
    '''
        Returns the updated file list to move to an another folder we specified.
    '''
    for filename in os.listdir(sourceFolderPath):
        filePath = os.path.join(sourceFolderPath,filename) # can be manually joined
        filesToMove.append(filePath) # update the files list
    return filesToMove

def moveFiles(filesToMove):
    '''
        Returns NaN, moves files to the destination folder we specified above.
    '''
    for f in range(len(filesToMove)): 
        shutil.move(filesToMove[f], destionationFolderPath)


if __name__ == '__main__':
    '''
        An endless while loop is not suitable for these kind of operations beacuse we are not creating or moving files all the time
        It is better to use a automation script at startup or with a time interval 
    '''
    filesToMove = [] 
    toMove = filesToTransfer(filesToMove) 
    moveFiles(toMove)


# End