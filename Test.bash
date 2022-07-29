#!/bin/bash

cat ./TestCase.txt | while read line
do
    echo $line|python3 analyze.py|sed -z 's/\n\(.\)/ \1/g'
done