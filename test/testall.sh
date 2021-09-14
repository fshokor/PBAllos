
for data_file in C674R L721R L721V WT ; do

  sh Utils/data.sh $data_file
  sh Utils/encoding.sh $data_file
  sh Utils/stat.sh $data_file
  python main.py --input_path out/$data_file/"$data_file"_seq.PB.flat --output_dir out/$data_file --start_idx 0 --end_idx 850 --data_size 200


done;

echo "Done"
