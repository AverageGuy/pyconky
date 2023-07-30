A Python script to update the .conkyrc file with correct device names
for wired and wireless devices.

Requirements
============

The script requires that python3 and pip be installed on the system.

The easiest way to do that is by the apt command.

sudo apt install python3 python3-pip -y

Python also requires the netifaces package. Most likely it is already
installed by default. If not you can install it with:

python3 -pip install netifaces

Installation 
============

git clone <https://github.com/AverageGuy/pyconky.git>

Usage
=====

This script should be run from the location in which the .conkyrc file
exists, most likely the user's home directory. Assuming you were in your
home directory when you issued the above git command, simply run:

pyconky/pyconky.py

This will read the .conkyrc file and write a file named conkyrc.txt.
View it with your favorite editor and see if it looks OK. Then backup
your .conkyrc file and copy the conkyrc.txt file to .conkyrc. This
script would do.

cp .conkyrc .conkyrc.orig\
cp cronkrc.txt .cronkrc

Look at the pyconky/pyconky.py file to learn how it works.
