#!/bin/bash

SHORTCODES=~/sci/100daysofpractice-dataset/shortcodes/shortcodes-test.txt
PYTHON=~/sci/100daysofpractice-dataset/venv/bin/python
CSVFILE=shortcode-username.csv

while read SHORTCODE; do
    USERNAME=$($PYTHON get-username.py $SHORTCODE)
    PAIR=$SHORTCODE,$USERNAME
    echo $PAIR
    echo $PAIR >> $CSVFILE
done <$SHORTCODES
