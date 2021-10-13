# generate.py
# 10/13/21
# Christian Knight (christianknight9@gmail.com)

# Compares the contents of two directory addresses passed in as agruments and 
# finds the unique files in each directory. Copies files from the source
# directory to the destination directory if they are not already present.
# Deletes "Thumbs.db" file(s) commonly found in Windows systems if present.

# Usage: python generate.py <source directory> <destination directory>

import os, shutil, sys

def main():
    # Get source and destination directories from command line arguments
    if len(sys.argv) == 3:
        DIR_SRC = sys.argv[1]
        DIR_DEST = sys.argv[2]
    else:
        print("Incorrect usage!")
        exit()

    file_list_src = []     # for storing a list of files in the source directory
    file_list_dest = []    # for storing a list of files in the destination directory

    # Get a list of files already in the destination directory
    for root, dirs, files in os.walk(DIR_DEST):
        for file in files:
            if file == "Thumbs.db":
                print(os.path.join(root, file))
                val = input("Delete file? (y/n): ")
                if val == 'y':
                   os.remove(os.path.join(root, file))
            else:
                file_list_dest.append(file)

    # Get a list of files in the source directory, copy to destination directory if not already present
    for root, dirs, files in os.walk(DIR_SRC):
        for file in files:
            if file == "Thumbs.db":
                print("Deleting ", os.path.join(root, file))
                os.remove(os.path.join(root, file))
            else:
                file_list_src.append(file)

            if file in file_list_src and file not in file_list_dest:
                print(file, "not in dest! Copying...")
                path_file = os.path.join(root, file)
                shutil.copy2(path_file, DIR_DEST)
                file_list_dest.append(file)

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

    # Check with the user if the files in the destination should be deleted
    if len(files_only_in_dest) > 0:
        val1 = input("Do you want to delete files only in destination? (y/n): ")
        if val1 == 'y':
            for file in files_only_in_dest:
                os.remove(os.path.join(DIR_DEST, file))
        elif val1 == 'n':
            val2 = input("Ok, do you want to copy them to the source directory? (y/n): ")
            if val2 == 'y':
                for file in files_only_in_dest:
                    path_file = os.path.join(DIR_DEST, file)
                    shutil.copy2(path_file, DIR_SRC)

if __name__== "__main__":
   main()