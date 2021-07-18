#! Python 3
#T.M 18/07/21

import os, shutil, sys

#Task 1: Walking through a folder tree displaying contents to screen.
print('Enter the folder path you want to display its contents.')
targetFolder=input()
filesFound=[]
try:
    for folderName, subFolder, fileName in os.walk(targetFolder):
        #Grab files into list for Task 2
        if fileName != []:
            filesFound.append(fileName)
        print(f'Folder: {folderName}')
        if subFolder != []:
            print(f'Subfolders found here are: {subFolder}')
        else:
            print(f'No subfolders were found here.')
        if fileName != []:
            print(f'Filenames found here are: {fileName}\n')
        else:
            print(f'No files were found here.\n')
    if folderName == []:
        pass  #If folderName not defined will cause a error addressed below, else script will continue.
except:
    print('An error has occured, please ensure your using a correct file path and try again.')
    sys.exit()

#Task 2: Find all python files within the folder and display them to the screen.
try:
    for i in range(len(filesFound)):
        if filesFound[i][0].endswith('.py'):
            print(f'Python File Found: {filesFound[i][0]}')
except:
    print('An error occured, please try again.\n')

#Task 3: Ask do you want to create a backup of the folder and its contents.
print('\nDo you want create a backup of this folder and all its contents?')
answer=input('Enter: \'yes\' or \'y\' if you want to create a backup.\n', )
if answer.lower() in ['yes', 'y']:
    try:
        shutil.copytree(targetFolder, targetFolder+'.backup')
        print('Backup created successfully.\n')
    except:
        print('Backup failed.\n')
else:
    print('Backup not created.\n')

#Task 4: Ask do you want to delete folder and its contents
print('Do you want to delete this folder and all its contents?')
answer2=input('Enter: \'yes\' or \'y\' if you want to delete.\n', )
if answer2.lower() in ['yes', 'y']:
    try:
        shutil.rmtree(targetFolder)
        print('Folder deleted.\n')
    except:
        print('Deleting folder failed.\n')
else:
    print('Folder not deleted.\n')

#Exit program
print('Exiting...')
sys.exit()
