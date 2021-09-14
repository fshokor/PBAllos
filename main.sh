#!/bin/bash

sh Utils/data.sh $1
sh Utils/encoding.sh $1
sh Utils/stat.sh $1
python main.py --input_path out/$1/"$1"_seq.PB.flat --output_dir out/$1 --start_idx $2 --end_idx $3 --data_size $4
echo "Done"


