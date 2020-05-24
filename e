#!/bin/bash
clear
echo "$ elang > $PWD $1 $2 $3 $4 $5 "
python3 passenger_wsgi.py $1 $2 $3 $4 $5
echo ""
exit