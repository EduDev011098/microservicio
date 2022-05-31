#!/bin/bash
sudo yum update
sudo yum install git
sudo amazon-linux-extras install nginx1 
pip3 install virtualenv
git clone https://github.com/EduDev011098/microservicio.git
pip3 install flask
pip3 install pytz