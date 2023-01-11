#!/bin/bash

path=$1 # path to directory to analyze
sortby=$2 # option for sorting by size (ascending or descending)
top=$3 # option for displaying only a certain number of entries

if [ -z "$path" ] # if path is not provided
then
    path="./" # use current directory
fi

if [ -z "$sortby" ] || [ "$sortby" != "asc" ] && [ "$sortby" != "desc" ] # if sort option is not provided or invalid
then
    sortby="desc" # default to descending sort
fi

if [ -z "$top" ] # if number of entries option is not provided
then
    top=10 # default to top 10 entries
fi

du -a $path | sort -nr | head -n $top > disk_usage_report.txt

cat disk_usage_report.txt
