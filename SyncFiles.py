import os
import shutil
import time

try:
    #for Python2
    import Tkinter as tk
except:
    #for Python3
    import tkinter as tk

try:
    #for Python2
    import tkFileDialog as tkfd
except ImportError:
    #for Python3
    import tkinter.filedialog as tkfd

#get the file paths of the two file paths from the user
def getPaths():
    global pathFirst
    global pathSecond
    root = tk.Tk()
    root.withdraw()
    pathFirst = tkfd.askdirectory(title="Select First Folder Path")
    pathSecond = tkfd.askdirectory(title="Select Second Folder Path")

#Copy files from srcDir to dstDir.  Files will only be copied from srcDir to 
#dstDir if dstDir does not have a file.
#@param srcDir - The source directory to copy files from.
#@param dstDir - The destination directory to copy files to.
def copyFolderToFolder(srcDir, dstDir):
    #get list of all files and folders in srcDir
    srcFiles = os.listdir(srcDir)
	
    #check if the destination directory exists
    if not os.path.isdir(dstDir):
        os.makedirs(dstDir)
	
    for thisFile in srcFiles:
        if thisFile[:2] == "~$":
            #thisFile is a Windows backup file
            continue
			
        if thisFile[-1] == '~':
            #thisFile is a *IX backup file
            continue
		
        srcFilePath = os.path.join(srcDir, thisFile)
        dstFilePath = os.path.join(dstDir, thisFile)
		
        if (os.path.isfile(srcFilePath) & (not os.path.isfile(dstFilePath))):
            #The file exists in the source path but not the destination path.
            #Copy the file from the source path to the destination path.
            print("Copying " + srcFilePath)
            shutil.copyfile(srcFilePath, dstFilePath)
        elif os.path.isdir(srcFilePath):
            #thisFile is a folder
            copyFolderToFolder(srcFilePath, dstFilePath)

#Copy files between dir1 and dir2.  Files will only be copied between dir1
#and dir2 if that file is found in both dir1 and dir2.
#@param dir1 - The source directory to copy files from.
#@param dir2 - The destination directory to copy files to.
def copyDuplicateFiles(dir1, dir2):
    #get list of all files and folders in dir1
    dir1Files = os.listdir(dir1)

    #check if the destination directory exists
    if not os.path.isdir(dir2):
        os.makedirs(dir2)

    for thisFile in dir1Files:
        if thisFile[:2] == "~$":
            #thisFile is a Windows backup file and is to be ignored
            continue
			
        if thisFile[-1] == '~':
            #thisFile is a *IX backup file and is to be ignored
            continue
		
        dir1FilePath = os.path.join(dir1, thisFile)
        dir2FilePath = os.path.join(dir2, thisFile)
		
        if (os.path.isfile(dir1FilePath) & os.path.isfile(dir2FilePath)):
            #The file exists in both the source path and the destination path.
            #The newer version of the file will copy over the old version of the file.
            dir1ModifiedTime = os.path.getmtime(dir1FilePath)
            dir2ModifiedTime = os.path.getmtime(dir2FilePath)
            print("Duplicating " + dir1FilePath)
            if dir1ModifiedTime > dir2ModifiedTime:
                shutil.copyfile(dir1FilePath, dir2FilePath)
            elif dir1ModifiedTime < dir2ModifiedTime:
                shutil.copyfile(dir2FilePath, dir1FilePath)
        elif os.path.isdir(dir1FilePath):
            #thisFile is a folder
            copyDuplicateFiles(dir1FilePath, dir2FilePath)

#This script requests two file paths from the user.  It then syncronizes all
#files between the two directories such that both directories will have the same
#files and subfolders as each other.  If both directories already have the same
#file, the most recently updated file will be maintained and overwrite the older
#version.
#main.
getPaths()
print("***Copying from first directory to second directory...")
copyFolderToFolder(pathFirst, pathSecond)
print("***Copying from second directory to first directory...")
copyFolderToFolder(pathSecond, pathFirst)
print("***Copying shared files between first directory and second directory...")
copyDuplicateFiles(pathFirst, pathSecond)
print("Done!")










