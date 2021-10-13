#!/bin/sh

# Bootstrapping steps to create needed directories on the guest
mkdir -p ~/.ssh
mkdir -p ~/.ansible
mkdir -p ~/.config
mkdir -p ~/.config/openstack
mkdir -p ~/kafka_config
mkdir -p ~/ansible-vagrant/tasks