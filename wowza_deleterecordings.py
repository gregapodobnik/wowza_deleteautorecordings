"""
Description: Delete excessive recordings (240p, 360p,...)
from Wowza autorecording function.

Usage: Recursively search input folder for "_240p", "_360p", "_480p",
"_720p" and "_1080p" filesnames and delete them.

Script should be used with cronjob or similar tool.
Before running, define correct path and pattern of files to be deleted.
"""

import os
import fnmatch
import logging

# USER DEFINED: Define input folder path
PATH = "/path/to/wowza/recording/dir"

# USER DEFINED: Define search pattern
DELPATTERN = ["*_240p*.mp4",
              "*_360p*.mp4",
              "*_480p*.mp4",
              "*_720p*.mp4",
              "*_1080p*.mp4"]

# Logging
logging.basicConfig(format='%(asctime)s %(message)s',
                    filename='/var/log/wowza_delete_recordings.log',
                    level=logging.INFO)
logging.info("Script started")

# Recursively search input folder
FILESTODELETE = []
for root, dirs, filenames in os.walk(PATH):
    for items in DELPATTERN:
        for name in fnmatch.filter(filenames, items):
            FILESTODELETE.append(os.path.join(root, name))

# Delete files
if not FILESTODELETE:
    logging.info("Nothing to delete")
else:
    for deleted in FILESTODELETE:
        os.remove(deleted)
        logging.info("Deleted file : %s", deleted)

# Write to log
logging.info("Script ended")
