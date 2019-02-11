# FSND-Project-Logs-Analysis
This project is a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python 
program using the psycopg2 module to connect to the database.

#To test this you need to have vagrant installed on your machine.
*Steps to download vagrant and run tool
1. Download and install Vagrant(https://www.vagrantup.com/) and VirtualBox(https://www.virtualbox.org/).
2. Download/Clone the VM configuration from https://github.com/udacity/fullstack-nanodegree-vm . 
the path where you have downloaded/clone will be used in next steps
3.Download sample data from https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip
4. then, copy the database dump newsdata.sql to the vagrant/ (created in step 2)
5.Download logAnalysis.py into vagrant/ directory
6. Running the analysis tool

*Open shell prompt(use gitbash in windows)
# Installing & Configuring VM
cd ../vagrant
vagrant up

# Logging into machine
vagrant ssh

# Populate database using dump in shared folder 
cd /vagrant 
psql -d news -f newsdata.sql

# Run the program
python logAnalysis.py
