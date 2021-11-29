#!/bin/bash
# script for synchronizing the repository with the official GDrive content
# update reclone to 1.56 or higher, https://rclone.org/downloads/
# cf. https://forum.rclone.org/t/rclone-copy-error-failed-to-open-source-object-open-file-failed-googleapi-error-403-only-files-with-binary-content-can-be-downloaded-use-export-with-docs-editors-files-filenotdownloadable/25390/7

# configure rclone: https://wiki.linuxquestions.org/wiki/Rsync_with_Google_Drive
# default: use "drive" as name of the rclone remote

#
# of course, all of this requires the data to be shared with you ;)
#

# retrieve sample data
rclone sync "drive:/OntoLex Morph Vocabulary Test Data/" data/gdrive --drive-shared-with-me

# retrieve GDoc content: minutes
rclone sync "drive:/OntoLex Telco Minutes" minutes/ --drive-shared-with-me

# normalize names
OIFS="$IFS"
IFS=$'\n'
src=`find data/gdrive/ minutes/ | egrep -m 1 '[^_a-zA-Z0-9\/\.\-]'`
while echo $src | egrep . >/dev/null; do
	tgt=`echo $src | sed -e s/'[^_a-zA-Z0-9\/\.\-]'/'_'/g -e s/'___*'/'_'/g`
	echo $src ">" $tgt 1>&2;
	if [ -e $tgt ]; then 
		rm -rf $tgt;
	fi;
	mv $src $tgt;
	src=`find data/gdrive/ minutes/ | egrep -m 1 '[^_a-zA-Z0-9\/\.\-]'`
done;

# export to text format to facilitate search
# requires pandoc and w3m
for file in `find minutes/ | grep 'docx$'`; do
  tgt=`echo $file | sed s/'minutes'/'minutes_txt'/`.txt
  dir=`dirname $tgt`
  if [ ! -d $dir ]; then
    mkdir -p $dir
  fi
  pandoc $file | w3m -T text/html > $tgt
done
