#!/bin/bash
sudo su
echo "Updating"
yum update -y
echo "Updated"
aws configure set aws_access_key_id $XYZ
aws configure set aws_secret_access_key $XYZ
aws configure set default.region $XYZ
echo "AWS CONFIGURED"
yum -y install tomcat8-webapps tomcat8-docs-webapp tomcat8-admin-webapps
echo "TOMCAT INSTALLED"
sudo rm -rf pip-1.1
sudo rm -rf *.gz
sudo dd if=/dev/zero of=/swapfile bs=1024 count=524288
sudo chmod 600 /swapfile
sudo mkswap /swapfile
sudo swapon /swapfile
yum install python-pip -y
yum install python-devel -y
yum install gcc gcc-devel -y
yum install libxml2 libxml2-devel -y
yum install libxslt libxslt-devel -y
yum install openssl openssl-devel -y
yum install libffi libffi-devel -y
CFLAGS="-O0" pip install lxml
pip install scrapy
scrapy -v
sudo pip install icalendar
sudo pip install vobject
sudo yum -y install git-all
sudo git clone https://github.com/jl-git/talkstream.git /var/lib/tomcat8/webapps/talkstream
sudo service tomcat8 start
