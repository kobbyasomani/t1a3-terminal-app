#!/bin/bash
if ! [[ -x "$(command -v python3)" ]]
then
  echo "Error: 
It looks like you don't have Python3 installed.
Download and install it from this address: https://www.python.org/downloads/" >&2
  exit 1
else
    if [[ $1 == help ]]; then
        echo
        cat ./guess_help.txt
    else
        python3 ./guess/main.py
    fi
fi