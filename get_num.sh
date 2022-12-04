#!/bin/bash

function get_line() {
for i in {1..5}
do
         grep -n 'NO_SYNC' PRBS_Test_Group_$i.txt > Group_$i.txt
         case $i in
                1)
                   echo "1"
                ;;
                2)
                   echo "2"
                ;;
                *)
                    echo ""
          esac
done
}

get_line
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
                        echo echo "Loop #"` expr $num / 736 + 1 `
                        ;;
                        2)
                        echo "Loop #"` expr $num / 736 + 101 `
                        ;;
                        3)
                        echo "Loop #"` expr $num / 736 + 201 `
                        ;;
                        4)
                        echo "Loop #"` expr $num / 736 + 311 `
                        ;;
                        5)
                        echo "Loop #"` expr $num / 736 + 411 `
                        ;;
                        *)
                        echo ""
                esac
                echo $line
        done < Group_$i.txt
done

rm Group*
