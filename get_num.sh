#!/bin/bash

function get_line() {
for i in {1..5}
do
         grep -n 'NO_SYNC' PRBS_Test_Group_$i.txt > Group_$i.txt
done
}

get_line
total_count=0
for i in {1..5}
do
        serial=`grep "SERIAL" PRBS_Test_Group_$i.txt`
        step=`grep "STEP" PRBS_Test_Group_$i.txt | tail -n 1`
        echo "-----------------------------------------------------------------------------------------------------------"
        echo $serial
        echo $step
        echo "-----------------------------------------------------------------------------------------------------------"
        while read line
        do
                num=` echo $line |cut -d ":" -f 1 `
                case $i in
                        1)
                        n=` expr $num / 736 + 1 `
                        echo "                      lp#"$n
                        echo "#"$n >> count_1.txt
                        ;;
                        2)
                        n=` expr $num / 736 + 101 `
                        echo "                      lp#"$n
                        echo "#"$n >> count_2.txt
                        ;;
                        3)
                        n=` expr $num / 736 + 201 `
                        echo "                      lp#"$n
                        echo "#"$n >> count_3.txt
                        ;;
                        4)
                        n=` expr $num / 736 + 311 `
                        echo "                      lp#"$n
                        echo "#"$n >> count_4.txt
                        ;;
                        5)
                        n=` expr $num / 736 + 411 `
                        echo "                      lp#"$n
                        echo "#"$n >> count_5.txt
                        ;;
                        *)
                        echo ""
                esac
                echo ${line#*:}
        done < Group_$i.txt
        count=`sort -u count_${i}.txt| wc -l`
        total_count=$((${total_count}+${count}))
        echo "PRBS_Test_Group_${i} failures count: "${count}
done
echo "******************************************************************************"
echo "Total number of failures: "${total_count}

rm count*
rm Group*
rm PRBS_Test_Group_*
