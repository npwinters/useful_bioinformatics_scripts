#!/usr/bin/env bash
# Noah Winters, May 2022
# Calculates the mean of a column using awk
FILE=$1
echo $FILE
awk '{ total += $1; count++ } END { print total/count }' $FILE
