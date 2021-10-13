# Assignment 2 Milestone 2

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Created ansible playbooks for:
    1. Setting `ufw`
    2. Installing and configuring kafka/zookeeper
    3. Running `consumer.py`
* Created `kafka.service`, `zookeeper.service`, and `consumer.service
files
* Created modified `ms2_consumer` (with `couchdb` code removed)
* Met with Lessley on Oct. 12 to troubleshoot and create demo video

__Lessley Dennington__
* Created ansible playbooks for:
    1. Provisioning Chameleon instances
    2. Copying files and installing packages
* Created/configured `requirements.yml` to specify needed collections
* Updated `Vagrantfile` for this
* Created `README.md` for this milestone
* Met with Quinn on Oct. 12 to troubleshoot and create demo video

## Part 2: Effort expended/learning curve

In order to complete this milestone, we did the following:

1. Added `requirements.yml`

   We added a new `requirements.yml` file to specify the Ansible
   collections required for our solution.

2. Updated `Vagrantfile`

   Building off the work from Milestone 1, we:
      1. Specified an `ansible.galaxy_role_file` (`requirements.yml`)
      2. Specified the `ansible.galaxy_command` required to install
      the collections specified in `requirements.yml`

3. Updated `MyInventory`

   Added new `MyPrimaryVM` and `MySecondaryVM` groups to execute
   certain tasks on one Chameleon instance but not the other.

5. Updated `tasks`

   Modified `main.yml` to run the tasks detailed below as plays.

   Removed tasks previously-copied from scaffolding code (except for
   `main.yml`) and added:

   1. `playbook_create_chameleon_instances`: creates Chameleon
   VMs with correct image, security groups, public IP, etc.
   2. `playbook_install_packages`: installs Java packages required
   by kafka and zookeeper on Chameleon VMs
   3. `playbook_copy_files`: copies our `kafka_config` directory
   containing our consumer code, `.service` files, and other kafka-
   required files to Chameleon VMs.
   4. `playbook_set_ufw`: sets correct firewall rules for ssh,
   Zookeeper, Kafka, etc.
   5. `playbook_set_up_kafka.yml`: installs and configures common
   kafka settings on Chameleon VMs
   6. `playbook_kafka_zookeeper_primary`: configures unique kafka
   settings and starts kafka and zookeeper on primary VM; creates
   `MeetUpNewYork` topic
   7. `playbook_run_consumer.yml`: runs `consumer.py` as a background
   service on primary VM
   8. `playbook_kafka_secondary`: configures unique kafka
   settings and starts kafka and zookeeper on secondary VM; creates
   `MeetUpSeattle` topic

6. Added configuration files for kafka

   Added the following kafka configuration files for easy copying to
   Chameleon VMs:

   1. `consumer.service`
   2. `kafka.service`
   3. `zookeeper.service`
   <br/>

   Also added the simplified `ms2_consumer.py` with `couchdb` related
   code removed for the purposes of this milestone only.

## Part 3: Video demo

The following is a demonstration of the work completed for this milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EWV4oxY1wWNIvynwliQMV6kB-BdxHLBJQk4xL4ySqor91A?e=8vHXPr
