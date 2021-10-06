#!/bin/bash
# script for synchronizing the repository with the official GDrive content
# update reclone to 1.56 or higher, https://rclone.org/downloads/
# cf. https://forum.rclone.org/t/rclone-copy-error-failed-to-open-source-object-open-file-failed-googleapi-error-403-only-files-with-binary-content-can-be-downloaded-use-export-with-docs-editors-files-filenotdownloadable/25390/7

# configure rclone: https://wiki.linuxquestions.org/wiki/Rsync_with_Google_Drive
# default: use "drive" as name of the rclone remote

rclone sync "drive:/OntoLex Telco Minutes" minutes/
