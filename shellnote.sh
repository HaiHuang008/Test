#!/bin/sh


osCheck=`uname -a | grep "sonic" | awk '{print $2 }'| tr A-Z a-z`
if [ "${osCheck}" = "sonic" ];then
        echo "sonic platform"
else
        echo "other liunx platform"
fi



OPT_RET=`getopt -o hdf:m:a:rkp:t -n '*ERROR' -- "$@"`
if [ $? -ne 0 ];then
    echo "ERROR: exited with doing nothing." >&2
    exit 1
fi
usage()
{
    cat << EOT
    Usage: $__ScriptName [option] ...
    Running this executable script $__ScriptName, the module will be
    installed, a shell of switch SDK will be initialized as well.
    the shell is either BCM shell or remote shell developed by celestica.

    Options:
        -h, Display this message
        -d, The user portion of switch SDK will be running as daemon,
            and a remote shell function will enable.
        -f  FileName, The output content will save to file 'fileName',
            when the user portion becomes daemmon.Please use this option
            together with option '-d'.
        -r, Remove all the related modules and files.
        -m  PortMode, This will assign portmapping type and support {PortNum}x{LaneNum}x{LaneSpeed}-{PAM4|NRZ}
            for example: 64x4x100-PAM4, 32x8x50-PAM4, 128x2x100-PAM4, 64x4x50-PAM4, 256x1x100-PAM4, 128x2x50-PAM4,
                        64x4x25-NRZ, 256x1x50-PAM4, 128x2x25-NRZ, 64x4x10-NRZ, 256x1x25-NRZ, 256x1x10-NRZ.
            The default is 64x4x100-PAM4.
        -a  MAC_addr, This is base MAC address to use the knet interface.
            The MAC address is in AA:BB:CC:DD:EE:FF format.
        -k, Support the knet mode.
        -t, Support the pre-emphasis mode.
        -p, Support medium{eloop|dac|optical}, default is eloop.

    Example:
        1)As a foreground process
            $__ScriptName
        2)As a daemon, and display results with the stardand output
            $__ScriptName -d
        3)As a daemon, and save results to the file 'sdk.log'
            $__ScriptName -d -f sdk.log
        3)As a daemon, and save results to the file 'sdk.log'
            $__ScriptName -d -f sdk.log
        4)Use E-loop module as medium to test
            $__ScriptName -p eloop
        5)Use DAC module as medium to test
            $__ScriptName -p dac
        6)Use optical module as medium to test
            $__ScriptName -p optical

EOT
}


eval set -- "$OPT_RET"
while true ;do
    case "$1" in
        -h)
            usage
            exit 1
            ;;
        -d)
            runningMode=daemon
            shift
            echo $runningMode
            ;;
        -f)
            logFileName=$2
            shift 2
            ;;
        -r)
                osCheck=`uname -a | grep "sonic" | awk '{print $2 }'| tr A-Z a-z`
                if [ "${osCheck}" = "sonic" ];then
                    echo rmmod_sonic_modules
                else
                    echo rmmod_onl_modules
                fi
            exit 0
            ;;
         -m)
            portMode=$2
            shift 2
            echo $portMode
            ;;
        -a)
            macAddr=$2
            shift 2
            ;;
        -k)
            knet="enable"
            shift
            ;;
        -t)
            txFir="enable"
            shift
            ;;
        -p)
            medium=$2
            echo $medium
            shift 2
            ;;
        --)
            shift
            break
            ;;
        *)
            echo "ERROR: internal error!"
            exit 1
            ;;
    esac
done

