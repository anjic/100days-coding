#!/bin/bash
#XIO Init Script
#Copyright Notice Comes here

#initialize default varibales
help_message () {
  echo "Usage: $0 -i <ip_of_ise_vm> [optional] -f /path/to/client_install_folder/main.bundle.js"
  exit 1
}

function valid_ip()
{
    local  ip=$1
    local  stat=1

    if [[ $ip =~ ^[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}$ ]]; then
        OIFS=$IFS
        IFS='.'
        ip=($ip)
        IFS=$OIFS
        [[ ${ip[0]} -le 255 && ${ip[1]} -le 255 \
            && ${ip[2]} -le 255 && ${ip[3]} -le 255 ]]
        stat=$?
    fi
    return $stat
}

if [ $# -eq 0 ];
then
        help_message
        exit 0
fi

while getopts ":hi:f:" arg;
do
  case $arg in
    h )
      help_message
      ;;
    i )
      ISE_IP=$OPTARG
      ;;
    f )
      BUNDLEJS_PATH=$OPTARG
      ;;
  
    esac
done

#echo $ISE_IP

####################################################
#Patching Bundle.js with IP received from -i option
####################################################

if [[ -z "$ISE_IP" ]]; then
  echo "IP Not Provided. Patching Not Successfull. See Usage Below. Quiting..."
  help_message
  exit 0
else
  if  !(valid_ip $ISE_IP); then
    echo ip is not valid. right ip eg. 122.134.60.45
    help_message
    exit 0
  fi  
fi

if [[ -z $BUNDLEJS_PATH ]]; then
    echo "main.budle.js argument not supplied. using default ./bundle.js"
    BUNDLEJS_PATH="./main.bundle.js"
fi

if [ ! -f $BUNDLEJS_PATH ]; then
    echo "main.bundle.js not found!"
    help_message
    exit 0
else
    #Backup
    echo Backing up to $BUNDLEJS_PATH.bak
    cp $BUNDLEJS_PATH $BUNDLEJS_PATH.bak
    #get old ip from bundle.js
    OLD_ISE_IP=$(grep -o '[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}\.[0-9]\{1,3\}' $BUNDLEJS_PATH | uniq)
    if !(valid_ip $OLD_ISE_IP) then
       echo No valid ip to patch. Are you pointing to a wrong main.bundle.js file?
       echo Patch not successfull
       exit 0
    fi
    echo Detected Old IP as $OLD_ISE_IP
    echo Replacing $OLD_ISE_IP with $ISE_IP
    #patch new IP inside main.bundle.js
    sed -i "s/$OLD_ISE_IP/$ISE_IP/w changes.txt"  $BUNDLEJS_PATH
fi

CHANGES=$(wc < changes.txt | tr -s ' '| cut -f2 -d' ')
echo $CHANGES lines patched successfully 
rm changes.txt

