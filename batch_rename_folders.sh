#!/usr/bin/env bash
# Noah Winters
# Batch renames folders
# Input is a tab-delimited file with old_id in first column and new_id in second
SAVE_IFS=$IFS
IFS=$(echo -en "\n\b")
for row in `cat id_mirna.tsv`
do
    echo $row
    cur_name=`echo $row | awk -F " " '{print $1}'`
    new_name=`echo $row | awk -F " " '{print $2}'`
    mv $cur_name $new_name
done
IFS=$SAVE_IFS
