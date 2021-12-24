FILE_SYNC_SCRIPT_DIR = "."
SRC_DIR = "."
DEST_DIR = "."

import sys
sys.path.insert(0, FILE_SYNC_SCRIPT_DIR)

import file_sync

if __name__== "__main__":
   file_sync.main_process(SRC_DIR, DEST_DIR)