import shlex
import subprocess
import random
import os

eid = str(random.randint(1, 1000000))


if not os.path.exists('output'):
    os.makedirs('output')

with open('output/' + eid + '_output.txt', 'w') as f:
    subprocess.check_call(shlex.split('python main_deepce.py --drug_file '
                                      '"data/drugs_smiles.csv" --dropout 0.1 '
                                      '--train_file "data/signature_train.csv" --dev_file "data/signature_dev.csv" '
                                      '--test_file "data/signature_test.csv" --batch_size 16 --max_epoch 100'), stdout=f)
