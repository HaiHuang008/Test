import os

open_diff = open('F:/Python/pythonProject/AK200266-Serdes-Port-Sum.txt', 'r')
spilt_num = 39
diff_line = open_diff.readlines()
line_list = []
for line in diff_line:
    line_list.append(line)

count = len(line_list)
print('Source file data lines:', count)

# number of lines of data per file
diff_match_split = [line_list[i:i + spilt_num] for i in range(0, len(line_list), spilt_num)]
for i, j in zip(range(0, int(count / spilt_num + 1)), range(0, int(count / spilt_num + 1))):
    with open('F:/Python/pythonProject/AK200266-Serdes-Port-%d.txt' % j, 'w+') as temp:
        for line in diff_match_split[i]:
            temp.write(line)


def every_nth(lst, nth):
    return lst[nth - 1::nth]


def Process_one_log_get_rx_list(log_path):
    file = open(log_path, "r")
    lines_list = []
    rx_list = []
    for lines in file:
        lines_list.append(lines)
    file.close()
    lines_list = list(filter(lambda x: x != "--\n", lines_list))
    for string in every_nth(lines_list, 4):
        rx_list.append(string.split("|")[1])
    return rx_list


def Get_one_port_each_rx_value(one_log_path):
    rx_value_list = Process_one_log_get_rx_list(one_log_path)
    lf_list = []
    hf_list = []
    bw_list = []
    g1_list = []
    g2_list = []

    for string in rx_value_list:
        lf_list.append(int(string.split()[1]))
        hf_list.append(int(string.split()[2]))
        bw_list.append(int(string.split()[3]))
        g1_list.append(int(string.split()[4]))
        g2_list.append(int(string.split()[5]))
    return lf_list, hf_list, bw_list, g1_list, g2_list


for i in range(0, 32):
    rx_lf_list, rx_hf_list, rx_bw_list, rx_g1_list, rx_g2_list = Get_one_port_each_rx_value('F:/Python/pythonProject'
                                                                                            '/AK200266-Serdes-Port-%d'
                                                                                            '.txt' % i)
    print("ifcs set devport %d rx_ctle_lf " % (i + 1), rx_lf_list)
    print("ifcs set devport %d rx_ctle_hf " % (i + 1), rx_hf_list)
    print("ifcs set devport %d rx_ctle_bw " % (i + 1), rx_bw_list)
    print("ifcs set devport %d rx_gainshape1 " % (i + 1), rx_g1_list)
    print("ifcs set devport %d rx_gainshape2 " % (i + 1), rx_g2_list)
    # print("\n")
    if os.path.exists('F:/Python/pythonProject/AK200266-Serdes-Port-%d.txt' % i):
        os.remove('F:/Python/pythonProject/AK200266-Serdes-Port-%d.txt' % i)
    else:
        print('no such file:%s' % 'F:/Python/pythonProject/AK200266-Serdes-Port-%d.txt' % i)
