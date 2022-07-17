#!/bin/bash

if [[ -f './main.py' ]]
then
    echo 'Welcome to the dog hotel'
    cat help.txt
    python3 main.py
else
    echo 'you dont have the needed files to run this program'
fi
