#!/bin/bash

sudo apt install python3-pip
pip3 install --upgrade pip3
pip3 install --upgrade ipython jupyter
pip3 install matplotlib
pip3 install sklearn
pip3 install seaborn
pip3 install missingno
pip3 install numpy
pip3 install pandas
pip3 install tensorflow

# sudo apt-get install mysql-server mysql-client
# sudo /etc/init.d/mysql restart
# sudo netstat -tap | grep mysql
# sudo sed 's/bind-address/# bind-address/g' /etc/mysql/mysql.conf.d/mysqld.cnf
# sudo apt-get install nodejs
# sudo apt install npm
# sudo npm install -g vue-cli