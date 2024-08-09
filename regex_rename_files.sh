#!/usr/bin/env bash
# Noah Winters, April 2022
# This script uses sed to rename files in a directory

FILE=$1
REGEX=$2
REPLACE=$3

mv "$FILE" "`echo $FILE | sed "s/$REGEX/$REPLACE/"`"
