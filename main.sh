#!/bin/bash

if [ "$1" = "-h" ]
then
  echo "This program takes your .pdb files and compute the mutual information between the residues of protein sequence"
  echo ""
  echo "It use the Protein Blocks (PBs) as a structural alphabet, to encode the sequences  "
  echo ""
  echo "Usage : sh `basename $0` -a <file_name> <strain_name>  <start_idx>   <end_idx>   <data_size>"
  echo ""
  echo "This Help File: sh `basename $0` -h"
  echo ""
  echo "PBAllos"

else

  sh Utils/data.sh $1
  sh Utils/encoding.sh $1
  sh Utils/stat.sh $1
  python main.py --input_path out/$1/"$1"_seq.PB.flat --output_dir out/$1 --start_idx $2 --end_idx $3 --data_size $4
  echo "Done"

fi


