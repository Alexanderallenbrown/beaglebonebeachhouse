#!/bin/sh
# launcher.sh
# navigate to home directory, then to this directory, then execute 
#python script, then back home
ntpdate -b -s -u pool.ntp.org
cd /
cd /home/root/beaglebonebeachhose/scripts/
python tempscript.py
cd /

