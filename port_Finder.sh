#!/bin/bash


# check number of inputs
if [ $# -lt 0 ]
then

        echo "Missing Ip address"
        echo "EX) ./port_Finder 192.xxx.xxx.xxx."
        echo "Exiting..."

        exit 3

fi

# start scanning for open ports and save them to a file for later scanning
echo "nmap scan of $1 for open ports"
nmap -p- -T4 $1 | grep open | grep -v filtered | cut -d"/" -f1 | tr "\n" "," | sed s/,$// | tee $1.OpenPorts

echo " are open and saved to $1.OpenPorts"