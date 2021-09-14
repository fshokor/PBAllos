#!/bin/bash 


mkdir out
mkdir out/$1

#install the data:

wget https://www.dsimb.inserm.fr/~debrevern/Calf-1Projekt/"$1".tar.gz -nc -O out/$1/$1.tar.gz


#untar 

tar -xf out/$1/$1.tar.gz -C out/$1

#exttract the frames file

cp -R out/$1/data/goguet/DM_Calf-1_$1/production_global/Frames  out/$1/$1_Frames

#rename the files
cd out/$1/$1_Frames
for file in $1_*; do mv "$file" "${file#$1_}";done;

#adding 0
for a in [0-9]*.pdb; do mv $a `printf %04d.%s ${a%.*} ${a##*.}`; done;

cd -

rm -r out/$1/data
