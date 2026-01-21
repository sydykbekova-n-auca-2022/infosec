#!/bin/bash

H=$(date +%H)
M=$(date +%M)

HOURS_LEFT=$((17 - 10#$H))
MINS_LEFT=$((60 - 10#$M))

if [ $HOURS_LEFT -lt 0 ]; then
    echo "The workday is already over!"
else
    echo "Current time: $H:$M."
    echo "Work day ends after $HOURS_LEFT hours and $MINS_LEFT minutes."
fi
