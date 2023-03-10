#!/bin/bash

last_file=`ls -t $(dirname $0)/*.md| head -n 1`
tgt=`dirname $last_file`/`date +%Y-%m-%d`.md
echo $last_file $tgt
if [ $last_file = $tgt ]; then \
	echo $last_file up to date 1>&2; \
else \
	wget https://www.w3.org/community/ontolex/wiki/Morphology -O - | \
	pandoc -f html -t markdown > $tgt; \
	if [ `cat $last_file | wc -c ` = `cat $tgt | wc -c` ]; then \
		echo $last_file up to date 1>&2; 
		rm $tgt; 
	else
		echo '- [`'`basename $tgt | sed s/'.md$'//`'`]('`basename $tgt`')' >> `dirname $tgt`/Readme.md;
		echo "Don't forget to git add "`$tgt`"; git commit -a -m 'wiki update'; git commit push" 1>&2;
	fi; \
fi;


