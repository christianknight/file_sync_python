# file_sync.py
# 10/15/21
# Christian Knight (christianknight9@gmail.com)

# Compares the contents of two directory addresses passed in as agruments and 
# finds the unique files in each directory. Copies files from the source
# directory to the destination directory if they are not already present.
# Deletes "Thumbs.db" file(s) commonly found in Windows systems if present.

# Usage: python generate.py <source directory> <destination directory>

import os, shutil, sys

def main_process(source_dir, dest_dir):
    file_list_src = []     # for storing a list of files in the source directory
    file_list_dest = []    # for storing a list of files in the destination directory

    # Get a list of files already in the destination directory
    for root, dirs, files in os.walk(dest_dir):
        for file in files:
            if file == "Thumbs.db":
                print("Deleting ", os.path.join(root, file))
                os.remove(os.path.join(root, file))
            else:
                file_list_dest.append(file)

    # Get a list of files in the source directory
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            if file == "Thumbs.db":
                print("Deleting ", os.path.join(root, file))
                os.remove(os.path.join(root, file))
            else:
                file_list_src.append(file)

    # Find matches between source and destination and print list
    file_matches = set(file_list_src) & set(file_list_dest)
    files_only_in_src = set(file_list_src) - set(file_matches)
    files_only_in_dest = set(file_list_dest) - set(file_matches)
    print("Number of source files:", len(file_list_src))
    print("Number of destination files:", len(file_list_dest))
    print("Number of matches:", len(file_matches))
    print("Number of files only in source directory:", len(files_only_in_src))
    print(str(files_only_in_src))
    print("Number of files only in destination directory:", len(files_only_in_dest))
    print(str(files_only_in_dest))

    # Check if the files only in the destination directory should be copied to the source directory or deleted
    if len(files_only_in_dest) > 0:
        val1 = input("Do you want to delete files only in destination? (y/n): ")
        if val1 == 'y':
            for root, dirs, files in os.walk(dest_dir):
                for file in files:
                    if file in files_only_in_dest:
                        os.remove(os.path.join(root, file))
        elif val1 == 'n':
            val2 = input("Ok, do you want to copy them to the source directory instead? (y/n): ")
            if val2 == 'y':
                for file in files_only_in_dest:
                    print(file, "not in src! Copying...")
                    file_list_src.append(file)
                    path_file = os.path.join(dest_dir, file)
                    shutil.copy2(path_file, source_dir)

    # Check if the files only in the source directory should be deleted or copied to the destination directory
    if len(files_only_in_src) > 0:
        val1 = input("Do you want to copy files only in source directory to the destination directory? (y/n): ")
        if val1 == 'y':
            for file in files_only_in_src:
                print(file, "not in dest! Copying...")
                file_list_dest.append(file)
                path_file = os.path.join(source_dir, file)
                shutil.copy2(path_file, dest_dir)
        elif val1 == 'n':
            val2 = input("Ok, do you want to delete them instead? (y/n): ")
            if val2 == 'y':
                for root, dirs, files in os.walk(source_dir):
                    for file in files:
                        if file in files_only_in_src:
                            os.remove(os.path.join(root, file))

if __name__== "__main__":
    # Get source and destination directories from command line arguments
    if len(sys.argv) == 3:
        DIR_SRC = sys.argv[1]
        DIR_DEST = sys.argv[2]
        main_proccess(DIR_SRC, DIR_DEST)
    else:
        print("Incorrect usage!")
        exit()