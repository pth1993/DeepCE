def get_id_test(input_file):
    with open(input_file) as f:
        for line in f:
            line = line.strip().split(',')
            if line[0] == 'test':
                test_id = line[1:]
            elif line[0] == 'dev':
                dev_id = line[1:]
            else:
                raise ValueError("Unknown dataset: %s" % line[0])
    return dev_id, test_id


def read_data_train(input_file, output_file, filter, dev_pert_id, test_pert_id):
    filter_drug = filter["pert_id"] + dev_pert_id + test_pert_id
    with open(input_file, 'r') as f1, open(output_file, 'w') as f2:
        header = f1.readline()  # skip header
        f2.write(header)
        for line in f1:
            tmp = line.strip().split(',')
            assert len(tmp) == 983, "Wrong format"
            if tmp[1] not in filter_drug:
                f2.write(line)


if __name__ == '__main__':
    filter = {"time": "24H", "pert_id": ['BRD-U41416256', 'BRD-U60236422'], "pert_type": ["trt_cp"],
              "cell_id": ['A375', 'HA1E', 'HELA', 'HT29', 'MCF7', 'PC3', 'YAPC'],
              "pert_idose": ["0.04 um", "0.12 um", "0.37 um", "1.11 um", "3.33 um", "10.0 um"]}
    dev_pert_id, test_pert_id = get_id_test('pert_id_eval.txt')
    read_data_train('signature_0_7.csv', 'signature_train.csv', filter, dev_pert_id, test_pert_id)
