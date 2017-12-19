edit dbutils.sh as below:

#!/bin/bash

postgresql_user='postgres'
postgresql_database='xio_ise4'
zip_key='+-sZ~{7kE%&mQ^{5wLUx>m<n~Q<];D8-' #XIO Please find a way to create a unique zip key and keep it updated at the time of restore
temp_file='/tmp/xio_ise.sql'
zip_file='/tmp/xio_ise.zip'

usage() {
    echo "Usage : $0 -b | -r | -c"
    exit 1
}

cleanup() {
    echo "Cleaning Up ..."
    rm -f $zip_file
    rm -f $temp_file
}

backup() {
    echo "Backing up postgresql"
    pg_dump -U $postgresql_user -Fc $postgresql_database > $temp_file
    zip -j -P $zip_key $zip_file $temp_file
}

restore() {
    echo "This will nuke the old schema along with data if any"
    echo "Dropping old databse and creating new one"
    dropdb -U $postgresql_user $postgresql_database --if-exists && createdb -U $postgresql_user $postgresql_database
    echo "Inflating backup file..."
    unzip -d /tmp -P $zip_key $zip_file
    echo "Restoring. Please wait..."
    pg_restore -U $postgresql_user -d $postgresql_database $temp_file
}

if [[ ! $@ =~ ^\-.+ ]]
then
  usage
fi

while getopts brhc option
do
    case "${option}" in
       b) backup;;
       c) cleanup;;
       r) restore;;
       h) usage;;
    esac
done



