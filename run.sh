#!/bin/bash

echo "1-4"

python adult.py > "out_1.csv" &
python adult.py > "out_2.csv" &
python adult.py > "out_3.csv" &
python adult.py > "out_4.csv" &

sleep 130
echo "5-8"


python adult.py > "out_5.csv" &
python adult.py > "out_6.csv" &
python adult.py > "out_7.csv" &
python adult.py > "out_8.csv" &

sleep 130
echo "9-12"

python adult.py > "out_9.csv" &
python adult.py > "out_10.csv" &
python adult.py > "out_11.csv" &
python adult.py > "out_12.csv" &

sleep 130
echo "13-16"

python adult.py > "out_13.csv" &
python adult.py > "out_14.csv" &
python adult.py > "out_15.csv" &
python adult.py > "out_16.csv" &

sleep 130
echo "17-20"

python adult.py > "out_17.csv" &
python adult.py > "out_18.csv" &
python adult.py > "out_19.csv" &
python adult.py > "out_20.csv" &

sleep 130
echo "21-24"

python adult.py > "out_21.csv" &
python adult.py > "out_22.csv" &
python adult.py > "out_23.csv" &
python adult.py > "out_24.csv" &


