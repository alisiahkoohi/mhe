#!/bin/bash -l

src_dir=$HOME/Desktop/Ali/mhe/src/mhe
data_dir=$HOME/Desktop/Ali/mhe/data/2d/overthrust

set -e

cd $data_dir
sample_num_old=0
for filename in myfile*.dat; do
	sample_num_new=${filename: 7:-4}

	echo Processing sample number: $sample_num_new
	
	sed -i "s|ffile = \"myfile_${sample_num_old}\"|ffile = \"myfile_${sample_num_new}\"|g" $src_dir/demo2.py
	sample_num_old=$sample_num_new

	cd $src_dir
	./jy demo2.py
done

