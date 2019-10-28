#!/bin/bash 


# take target url
if [ $# -lt 0 ]
then

        echo "Missing url"
        echo "EX) ./domain_Recon google.com"
        echo "Exiting..."

        exit 3

fi

# Create directory to hold recon output
mkdir $1.recon && touch $1.recon/$1.domains

echo "Starting Sublister..."
sublist3r -d $1 -e Goolge,Yahoo,Bing,Ask,Netcraft,Virustotal,Threatcrowd,PassiveDNS  -o ./$1.recon/$1.domains


#Sorting domains
sort -u $1.recon/$1.domains > $1.recon/$1.uniqueDomains


echo "Starting aquatone..."
cat $1.recon/$1.uniqueDomains | aquatone -out ./$1.recon/$1.aqua

echo "Done!!! output saved to $1.recon/$1.domains"