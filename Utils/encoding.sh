#!/bin/bash 


#assign pb 
PBassign -p out/$1/$1_Frames/ -o out/$1/$1_unsorted


# sorting 
sed 's/^>/\x00&/' out/$1/$1_unsorted.PB.fasta  | sort -z | tr -d '\0' > out/$1/$1_seq.PB.fasta


# flatten
cat out/$1/$1_seq.PB.fasta | sed "s/^>.*/\t/" | tr -d "\n" | tr "\t" "\n" > out/$1/$1_seq.PB.flat

# delete first line 
sed '1d' out/$1/$1_seq.PB.flat > out/$1/$1_seq ; mv out/$1/$1_seq out/$1/$1_seq.PB.flat


rm - out/$1/$1_unsorted.PB.fasta