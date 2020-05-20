#!/usr/bin/env bash

CUDA_VISIBLE_DEVICES=0 python ../DeepCE/main_deepce.py --drug_file "../DeepCE/data/drugs_smiles.csv" --dropout 0.1 \
--train_file "../DeepCE/data/signature_train.csv" --dev_file "../DeepCE/data/signature_dev.csv" \
--test_file "../DeepCE/data/signature_test.csv" --batch_size 16 --max_epoch 1 > ../DeepCE/output/output.txt