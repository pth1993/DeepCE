#!/usr/bin/env bash
dir="../DeepCE/data"
if [ ! -d "$dir" ]; then
    mkdir "../DeepCE/data'"
fi
file="../DeepCE/data/drugbank_gene_expression.zip"
dir1="../DeepCE/data/drugbank_gene_expression"
if [ -d "$dir1" ]; then
	echo "$dir1 found."
else
	url="https://drive.google.com/uc?export=download&id=1B2s2HOcB3sWGi3qYcYTcdD4EbLPSnpQN"
    wget --load-cookie cookie.txt --save-cookie cookie.txt "${url}" -O tmp
    c=`grep -o "confirm=...." tmp`
    wget --load-cookie cookie.txt --save-cookie cookie.txt "${url}&$c" -O "${file}"
    rm cookie.txt tmp
    unzip "${file}" -d "${dir}"
    rm "${file}"
fi
