import os
import shutil

sourceDirectories = ['drawable-ldpi', 'drawable-mdpi', 'drawable-hdpi', 'drawable-xhdpi', 'drawable-xxhdpi', 'drawable-xxxhdpi']
downloadDirectory = '/home/mscannell/androidDeveloperDownloads'
consolidatedDirectory = '/home/mscannell/androidDeveloperAssets'

if not os.path.isdir(consolidatedDirectory):
    os.makedirs(consolidatedDirectory)

assetDirectories = os.listdir(downloadDirectory)

for folder in assetDirectories:
    directoryPath = os.path.join(downloadDirectory, folder)
    directoryPath = os.path.join(directoryPath, 'android')
    for srcDirectory in sourceDirectories:
        srcPath = os.path.join(directoryPath, srcDirectory)
        if os.path.isdir(srcPath):
            dstPath = os.path.join(consolidatedDirectory, srcDirectory)
            if not os.path.isdir(dstPath):
                os.makedirs(dstPath)
            srcFiles = os.listdir(srcPath)
            for imageFile in srcFiles:
                srcFilePath = os.path.join(srcPath, imageFile)
                if os.path.isfile(srcFilePath):
                    dstFilePath = os.path.join(dstPath, imageFile)
                    shutil.copyfile(srcFilePath, dstFilePath)
