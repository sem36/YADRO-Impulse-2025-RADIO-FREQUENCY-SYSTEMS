#!/bin/bash

if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <filename> <word>"
    exit 1
fi

grep -i -w "$2" "$1"
