# Programming Milestone 1

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__

* Completed all steps outlined in [Part 2](#part-2-effort-expended) and
[Part 4](#part-4-proposed-data-source-and-topics) below
* Met with Lessley on Sept. 11 to discuss assignment
* Contributed the following `README.md` content for Milestone 1:
    * [Part 4: Proposed Data Source and Topics](#part-4-proposed-data-source-and-topics)
* Created video demo
* Met with Lessley on Sept. 12 to create
video demo](#part-4-proposed-data-source-and-topics)

__Lessley Dennington__

* Completed all steps outlined in [Part 2](#part-2-effort-expended) and
[Part 4](#part-4-proposed-data-source-and-topics) below
* Met with Quinn on 09.11 to discuss assignment
* Contributed the following `README.md` content for Milestone 1:
    * [Part 1: Teamwork](#part-1-teamwork)
    * [Part 2: Effort Expended](#part-2-effort-expended)
* Created video demo
* Met with Quinn on Sept. 12 to create
[video demo](#part-4-proposed-data-source-and-topics)

## Part 2: Effort expended

In order to complete this milestone, we completed the following steps:

### Set up local VM using VirtualBox

1. Set up shared folder on local machine
2. Downloaded/installed VirtualBox
2. Downloaded Ubuntu 20.04 LTS
3. Created and configured a new Virtual Box VM
4. Installed and configured Ubuntu 20.04 LTS from downloaded ISO as guest OS
5. Installed packages required for Guest Additions
6. Installed Guest Additions
7. Enabled access to shared folder on guest OS
8. Disabled password requirement for `sudo` command
9. Installed additional useful packages (e.g. `pip3`, `emacs`)
4. Ran `python3 --version` to confirm it was installed with Ubuntu 20.04

### Set up Instance in Chameleon Cloud

1. Generated key pair and saved private key locally (we were not using
Windows, so we did not need to install/configure PuTTY)
2. Set up an Instance in Chameleon Cloud, including selecting source, flavor,
network, security group(s), and associating our key pairs and floating IPs,
among other steps
3. Discovered Instancce name and confirmed it is accessible via `ssh` on local
VM
4. Ran `python3 --version` to confirm it was installed with Ubuntu 20.04

### Clone scaffolding code and install packages on local VM

1. Cloned
[Programming Assignment Scaffolding Code](https://github.com/asgokhale/CloudComputingCourse)
2. Discovered additional packages needed to run producer code (`kafka`) and
installed with `pip3` (which was installed in the final step of
[section 1 above](#local-vm-setup-using-virtualbox))

## Part 3: Video demo

The following are video walkthroughs of the resources we created and the
packages we installed to complete this milestone:

[Lessley's video](https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EV-7IRgXZaZBr-3MDHyZhm4Bx7Ubet9faWVdkD0CxrZe7A?e=wrWvC9)

[Quinn's Video](https://vanderbilt365-my.sharepoint.com/:v:/g/personal/quinn_r_pommerening_vanderbilt_edu/EdnbybyQTaZAh4EThKnkwUUBEQjUdtwNTu19fiZxVf8s8g?e=5dufPp)

## Part 4: Proposed Data Source and Topics

We will use the [Meetup API](https://www.meetup.com/meetup_api/) as our data
stream source, which will allow us each to create different topics from our
virtual machines. The topics we plan to send to Kafka will be RSVPs for events
located in Seattle, WA and Nashville, TN.

## Installations
[Guide to install Kafka and Zookeeper](https://www.digitalocean.com/community/tutorials/how-to-install-apache-kafka-on-ubuntu-20-04)
- Install Kafka for Python with pip ```pip install kafka-python```

## Starting/Stopping Kafka and Zookeeper

### Kafka Commands
- Start: ```sudo systemctl start kafka```
- Stop: ```sudo systemctl stop kafka```
- Status: ```sudo systemctl status kafka```

### Zookeeper Commands
- Start: ```sudo systemctl start zookeeper```
- Stop: ```sudo systemctl stop zookeeper```
- Status: ```sudo systemctl status zookeeper```

## Dealing with Kafka Topics
NOTE: These steps must be done while on Kafka user from Installation Guide

### Creating Topic with Zookeeper
```
~/kafka/bin/kafka-topics.sh --create --zookeeper localhost:2181 --replication-factor 1 --partitions 1 --topic <topic name>
```

### Watch the Topic with Consumer
```
~/kafka/bin/kafka-console-consumer.sh --bootstrap-server localhost:9092 --topic <topic name> --from-beginning
```
