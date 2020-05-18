#!/bin/bash
clear
echo "$ elang > $PWD $1 $2 $3 $4 $5 "
python3 __app__.py $1 $2 $3 $4 $5
echo ""
exit