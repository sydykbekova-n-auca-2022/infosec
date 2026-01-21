#!/bin/bash

DIR=${1:-.}

if [ ! -d "$DIR"]; then 
	echo "Error: Directory '$DIR' does not exist"
	exit 1
fi

echo "Deleting empty files in: $DIR"
find "$DIR" -type f -empty -print -ok rm {} \;

