#!/bin/sh

# Bootstrapping steps to create directories and install packages
mkdir -p ~/.ssh
mkdir -p ~/.ansible
mkdir -p ~/.config
mkdir -p ~/.config/openstack
mkdir -p ~/kafka_config
mkdir -p ~/ansible-vagrant/tasks
sudo apt-get update
sudo apt-get -y install python3-pip
pip install kafka-python
