

path = "E:\\Y\\project\\"
num = 15
name_list = ["Load and initial test",
             "version check test",
             "64x4x100-PAM4 mode initial load test",
             "32x8x50-PAM4 mode initial load test",
             "128x2x100-PAM4 mode initial load test",
             "64x4x50-PAM4 mode initial load test",
             "256x1x100-PAM4 mode initial load test",
             "128x2x50-PAM4 mode initial load test",
             "64x4x25-NRZ mode initial load test",
             "256x1x50-PAM4 mode initial load test",
             "128x2x25-NRZ mode initial load test",
             "64x4x10-NRZ mode initial load test",
             "256x1x25-NRZ mode initial load test",
             "256x1x10-NRZ mode initial load test",
             "Remote shell test"
             ]

def create_txt(file_path, number, namelist):
    for n, name in zip(range(1, number+1), namelist):
        full_path = file_path + "T0" + str(n) + "-" + name + '.log'
        file = open(full_path, 'w')
        file.close()



create_txt(path, num, name_list)
