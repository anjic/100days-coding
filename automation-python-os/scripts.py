import os
import subprocess
#from sh import cd,ls

#os.system("mkdir piprpms")
#os.system("ls -l")
#os.path.isdir("piprpms")
#print("It is directory")
#print(os.environ())
#print(os.getcwd())
#os.chdir("/root/temp/piprpms")
#print(os.getcwd())
#fo = open("foo.txt", "wb")
#print("Name of the file", fo.name)
#fo.write("Python is a great language.\nYeah its great!!\n");
#fo.close()
#os.chdir("/usr/src")
#print(os.getcwd())
#os.system("wget https://www.python.org/ftp/python/2.7.13/Python-2.7.13.tgz")
#os.system("yum install wget")
#os.system("curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py")
#os.system("mv /usr/src/get-pip.py /root/temp/piprpms")
#os.chdir("/root/temp/piprpms")
#os.system("python2.7 get-pip.py")  

os.chdir("/root/temp")

#Extracting yum-utls folder
#print("Extracting yum-utls tar....")
#os.system("tar -xvf yum-utls.tar.gz")

#navigating inside yum-utls folder& installing .rpm files
#os.chdir("/root/temp/yum-utls")
#print("Now am inside of...",os.getcwd())
#os.system("rpm -ivh *.rpm")

#Install unzip with yumdownloader
#os.system("yumdownloader --resolve unzip")
#os.system("rpm -ivh unzip-*.rpm")
print(os.getcwd())

#Installing POSTGRESQL
#os.mkdir("/root/temp/postgres")
os.chdir("/root/temp/postgres")
print(os.getcwd())
#print("installing......pgdg-redhat.......")
#os.system("rpm -ivh pgdg-redhat96-9.6-3.noarch.rpm")
#os.system("curl -OL https://download.postgresql.org/pub/repos/yum/9.6/redhat/rhel-7-x86_64/pgdg-redhat96-9.6-3.noarch.rpm")

#print(os.listdir("/root/temp/postgres"))

#os.mkdir("/root/temp/postgres/postgresrpm")
os.chdir("/root/temp/postgres/postgresrpm")
print(os.getcwd())
#os.system("yumdownloader --resolve postgresql96-server postgresql96-contrib")
#os.system("yumdownloader --resolve postgresql96-server postgresql96-contrib")
#os.system("rpm -ivh *.rpm")
print("....................................................")
print(os.getcwd())
print("....................................................")

#installing psycopg2
#os.system("pip download psycopg2==2.7.3.1")
#os.system("pip install psycopg2-2.7.3.1-cp27-cp27mu-manylinux1_x86_64.whl")

print("Initiating postgresql.....")
#os.system("service postgresql-9.6 initdb")
#os.system("/usr/pgsql-9.6/bin/postgresql96-setup initdb")
#os.system("service postgresql-9.6 initdb")
#os.system("systemctl enable postgresql-9.6.service")
#os.system("service postgresql-9.6 start")
os.system("service postgresql-9.6 status")
print("Editing file...........................!")

#Edit pg_hba file and add below lines to it
#with open("/var/lib/pgsql/9.6/data/pg_hba.conf","a") as conf_file:
#	conf_file.write("local all all trust\nhost all all 127.0.0.1/32 trust")
#	conf_file.write("\nhost\treplication\tpostgres\t::1/128\t\t\tident")
#	conf_file.write("\nhost\tall\t\tall\t\t::1/128\t\t\tmd5")
print("restarting postgres service.......")
#os.system("service postgresql-9.6 restart")
#os.system("service postgresql-9.6 status")

#print("Create user and database.....")
#os.system("psql -U postgres -c \"CREATE USER root WITH PASSWORD 'password';\"")
#print("created psql user......")
#os.system("psql -U postgres -c 'ALTER ROLE root  SET client_encoding TO 'utf8';'")
#os.system("psql -U postgres -c 'ALTER ROLE root SET timezone TO 'UTC';'")
#os.system("psql -U postgres -c \"CREATE DATABASE xio_ise4;\"")
#print("created database.......")
#os.system("psql -U postgres -c \"GRANT ALL PRIVILEGES ON DATABASE xio_ise4 TO root;\"")
#print("Granted all permissions...........")

#Install InfluxDB

print("Installing influxdb................")
#os.system("touch /etc/yum.repos.d/influxdb.repo")
#print("Creating repofile in yum.repos.d")

#with open("/etc/yum.repos.d/influxdb.repo","wr") as repo_file:
#       repo_file.write("[influxdb]")
#       repo_file.write("\nname = InfluxDB Repository - RHEL \$releasever")
#       repo_file.write("\nbaseurl = https://repos.influxdata.com/rhel/\$releasever/\$basearch/stable")
#       repo_file.write("\nenabled = 1")
#       repo_file.write("\ngpgcheck = 1")
#       repo_file.write("\ngpgkey = https://repos.influxdata.com/influxdb.key")
print("created influx repo file.........")

print(os.getcwd())

