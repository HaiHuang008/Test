open_diff = open('./log/R3240F2B162A18AK200238-Maxin-3.txt', 'r')
spilt_num = 550
diff_line = open_diff.readlines()
line_list = []
for line in diff_line:
    line_list.append(line)

count = len(line_list)
print('Source file data lines:', count)


# number of lines of data per file
diff_match_split = [line_list[i:i + spilt_num] for i in range(0, len(line_list), spilt_num)]
for i, j in zip(range(0, int(count / spilt_num + 1)), range(0, int(count / spilt_num + 1))):
    with open('./test/38-3-%d.txt' % j, 'w+') as temp:
        for line in diff_match_split[i]:
            temp.write(line)
            
            
            
