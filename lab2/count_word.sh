#!/bin/bash

FILE=$1
WORD=$2

COUNT=$(grep -oi "$WORD" "$FILE" | wc -l)

echo "The word '$WORD' appears $COUNT times in $FILE."
