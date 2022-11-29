#!/usr/bin/python3
import re


def split_logs_into_multiple(original_file, target_files, segment):
    open_diff = open(original_file, 'r')
    diff_line = open_diff.readlines()
    line_list = []
    for line in diff_line:
        line_list.append(line)
    count = len(line_list)
    print('Source file data lines:', count)
    # number of lines of data per file
    diff_match_split = [line_list[i:i + int(count / segment)] for i in range(0, count, int(count / segment))]
    for i, j in zip(range(0, segment), range(0, segment)):
        with open(target_files % (j + 1), 'w+') as temp:
            for line in diff_match_split[i]:
                temp.write(line)


def get_keyword_contents(logs, key_1, key_2):
    f = open(logs, 'r')
    buff = f.read()
    #  Clear line break, please cancel the next line comment
    # buff = buff.replace('\n', '')
    pat = re.compile(key_1 + '(.*?)' + key_2, re.S)
    res = pat.findall(buff)
    return res


def get_serder_list(logs, key_1, key_2, num):
    serder_result = []
    for n in range(0, num):
        res = get_keyword_contents(logs % (n + 1), key_1, key_2)
        for item in res:
            serder_result.append(item)
    return serder_result


def get_tx_rx_list(logs, key_1, key_2, num):
    res = get_serder_list(logs, key_1, key_2, num)
    tx_list = []
    rx_list = []
    for port_serder in res:
        serder = port_serder.strip("\n\t")
        ports_serder_list = list(filter(None, serder.split('########## SerDes')))
        for one_port in ports_serder_list:
            one_port_list = list(filter(None, one_port.split("\n")))
            tx_list.append(one_port_list[4].split()[-5:])
            rx_list.append(one_port_list[-1].split("|")[1].split())
    return tx_list, rx_list


def get_port_tx_rx_value(logs, key_1, key_2, num, rx=True):
    tx_value_list, rx_value_list = get_tx_rx_list(logs, key_1, key_2, num)
    p3_l = []
    p2_l = []
    p1_l = []
    atn_l = []
    pst_l = []
    lf_l = []
    hf_l = []
    bw_l = []
    g1_l = []
    g2_l = []
    if rx:
        for string in rx_value_list:
            lf_l.append(string[1])
            hf_l.append(string[2])
            bw_l.append(string[3])
            g1_l.append(string[4])
            g2_l.append(string[5])
        return lf_l, hf_l, bw_l, g1_l, g2_l
    else:
        for string in tx_value_list:
            p3_l.append(string[0])
            p2_l.append(string[1])
            p1_l.append(string[2])
            atn_l.append(string[3])
            pst_l.append(string[4])
        return p3_l, p2_l, p1_l, atn_l, pst_l


def set_rx_value(logs, key_1, key_2, num, rx=True):
    lf_l, hf_lg, bw_l, g1_l, g2_l = get_port_tx_rx_value(logs, key_1, key_2, num, rx=True)
    lf_l_split = [lf_l[i:i + 256] for i in range(0, len(lf_l), 256)]
    print(lf_l_split)
    print(len(lf_l_split))
    for i in range(0, num):
        print("Get the RX of the num %d log to set" % (i+1))
        lf_list = lf_l_split[i]
        lf = [lf_list[i:i + 8] for i in range(0, len(lf_list), 8)]
        for j in range(0, 32):
            print("ifcs set devport %d rx_ctle_lf " % (j + 1), lf[j])


file = 'F:/Python/pythonProject/log/288-01_%d.log'
k1 = 'serdes_parameter_dump_v1p1.txt'
k2 = 'SERDES Parameter'
set_rx_value(file, k1, k2, 5, rx=True)

