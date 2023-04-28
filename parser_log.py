for po in range(0,12):
    with open('./cd%d_BER.txt' % po, 'r') as f_input:
            tx_all = []
            ber_all = []
            port_all =[]
            lines = f_input.readlines()
            for l in lines:
                #  print(l)
                port = str(l).strip().split('    ')[0]
                tx = str(l).strip().split('    ')[1]
                ber = str(l).strip().split('    ')[2]
                port_all.append(port)
                tx_all.append(tx)
                ber_all.append(ber)
            size = 4
            sublists_ber = []
            sublists_tx = []
            for i in range(size):
                sublist = [ber_all[j+i] for j in range(0, len(ber_all)-i, size)]
                tx_sublist = [tx_all[j+i] for j in range(0, len(tx_all)-i, size)]
                sublists_ber.append(sublist)
                sublists_tx.append(tx_sublist)



            for lst  in sublists_ber:
                for j in range(len(lst)):
                    if lst[j] == ' LossOfLock' or lst[j] == ' Nolock':
                        lst[j] = '0.1'
                    lst[j] = float(lst[j])

            for min_port, (lst_ber, lst_tx) in enumerate(zip(sublists_ber, sublists_tx)):
                min_val = min(lst_ber)
                min_idx = lst_ber.index(min_val)
                tx_value = lst_tx[min_idx]
                print(f"The minimum value in list cd{po}_{min_port} is {min_val}     {tx_value}")

    f_input.close