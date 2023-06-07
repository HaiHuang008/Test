# text = """cd8[0] : 7.04e-11
# cd8[0] : 7.60e-12
# cd8[0] : 8.25e-11
# cd8[1] : 3.80e-12
# cd8[1] : 5.00e-11"""

dct = {}
new_dct = {}
with open('F:\\Python\\BER\\ber_log.txt', 'r') as file:
    lines = file.readlines()

    for line in lines:
        new_lines =[line.strip()]
        for line in new_lines:
            key, value = line.split(" : ")
            if key in dct:
                dct[key].append(float(value))
            else:
                dct[key] = [float(value)]

for key in dct:
    avg_value = sum(dct[key]) / len(dct[key])
    new_dct[key] = round(avg_value, 13)

for key, value in new_dct.items():
    print(f"{key}    {value}")
