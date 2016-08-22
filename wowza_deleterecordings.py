# Description: Delete excessive recordings (240p, 360p,...) from Wowza autorecording function.
#
# Usage: Recursively search input folder for "_240p", "_360p", "_480p", "_720p" and "_1080p" files and delete them.
# Script should be used with cronjob or similar tool.
# Before running, define correct path and pattern of files to be deleted

# Import Modules
import os
import fnmatch
import logging

# USER DEFINED: Define input folder path
path = "/path/to/wowza/recording/dir"

# USER DEFINED: Define search pattern
patterntodelete = ["*_240p*.mp4", "*_360p*.mp4", "*_480p*.mp4", "*_720p*.mp4", "*_1080p*.mp4"]

# Logging
logging.basicConfig(format='%(asctime)s %(message)s', filename='/var/log/wowza_delete_recordings.log',level=logging.INFO)
logging.info("Script started")

# Recursively search input folder
filestodelete = []
for root, dir, filenames in os.walk(path):
    for items in patterntodelete:
            for name in fnmatch.filter(filenames, items):
                filestodelete.append(os.path.join(root, name))

# Delete files
if not filestodelete:
    logging.info("Nothing to delete")
else:
    for deleted in filestodelete:
        os.remove(deleted)
        logging.info("Deleted file : %s", deleted)

# Write to log
logging.info("Script ended")
