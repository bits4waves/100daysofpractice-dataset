#!/bin/bash

PROJECT=~/sci/100daysofpractice-dataset
PYTHON=$PROJECT/venv/bin/python
SRC=$PROJECT/src
GET_USERNAME="$PYTHON $SRC/get-username.py"
SHORTCODES=$PROJECT/shortcodes/shortcodes-uniq.txt
PROFILES=$PROJECT/profiles
CSV=$PROFILES/shortcode-username.csv

while read SHORTCODE; do
    USERNAME=$($GET_USERNAME $SHORTCODE)
    PAIR=$SHORTCODE,$USERNAME
    echo $PAIR
    echo $PAIR >> $CSV
    instaloader  --login $IG_USER --password $IG_PASSWORD --fast-update $USERNAME
done <$SHORTCODES
