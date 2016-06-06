FileManager
===========

Contains scripts to perform file backup and folder syncronization

SyncFiles.py is a script that allows a user to syncronize files between 2 directories.  

First a user is asked to select two directories to syncronize.

The two selected directories will be compared with regards to their contents.
 - If a file of a specific name is in one directory but not the other, it will be copied from the one directory to the other.
 - If a file of a specific name is in both directories, both files will be compared with regards to their modification date.  The newer of the two files will be copied into the other directory and overwriting the older copy.

MergeDirectories.py is a script that takes several directories that have subdirectories 'drawable-?dpi' and copies the files in those subdirectories into a single directory that has 'drawable-?dpi' subdirectories.
