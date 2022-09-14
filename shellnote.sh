#!/bin/sh


osCheck=`uname -a | grep "sonic" | awk '{print $2 }'| tr A-Z a-z`
if [ "${osCheck}" = "sonic" ];then
        echo "sonic platform"
else
        echo "other liunx platform"
fi
