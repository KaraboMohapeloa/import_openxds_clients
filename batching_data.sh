#!/bin/bash
FILENAME=test_batch.csv
HDR=$(head -1 $FILENAME)
split -l 20000 $FILENAME xyz
n=1
for f in xyz*
do
	     if [ $n -gt 1 ]; then 
		               echo $HDR >Batch${n}_$FILENAME
			            fi
				         cat $f >>Batch${n}_$FILENAME
					      rm $f
					           ((n++))
					   done
