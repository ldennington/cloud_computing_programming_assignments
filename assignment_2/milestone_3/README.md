# Assignment 2 Milestone 3

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Added tasks to `playbook_set_up_couchdb.yml` to configure and start
`couchdb` and to create the Assignment 2 database
* Met with Lessley on Oct. 17 to create demo video

__Lessley Dennington__
* Created new `playbook_set_up_couchdb.yml` playbook
* Added tasks to new playbook to install `couchdb` dependencies, add
the `couchdb` signing key, add the `couchdb` repo to the instance's
sources list, and install `couchdb`
* Made Assignment 2 updates to `ms2_consumer` and `env.yml`
* Tested/troubleshot end-to-end pipeline runs
* Learned about/added tags to only run playbooks applicable to
Milestone 3
* Created/tested `playbook_main_tear_down.yml` and
`playbook_tear_down_chameleon_instances.yml`
* Created `README.md`
* Met with Quinn on Oct. 17 to create demo video

## Part 2: Effort expended/learning curve

In order to complete this milestone, we did the following:

1. Added `playbook_set_up_couchdb.yml`

    Quinn's time: 0.75 hours

    Lessley's time: 2 hours

    Total time: 2.75 hours

    Used ansible tasks to install and configure `couchdb`, including:
    - Installing `couchdb` dependencies
    - Adding the `couchdb` signing key
    - Adding the `couchdb` repository to instance's sources list
    - Installing `couchdb`
    - Configuring `couchdb` (specifying port, bind address, admin
    username/password, etc.)
    - Starting the `couchdb` service
    - Creating the Assignment 2 database

    This involved a good amount of trial and error, including discovery
    of the `apt_repository` and `apt_key` tasks, as well as how to
    programatically configure `couchdb`.

2. Updated `env.yml` and `ms2_consumer.py`

    Quinn's time: N/A

    Lessley's time: 0.15 hours

    Total time: 0.15 hours

    Added `couchdb` code to `ms2_consumer.py` and added correct values
    for `database_host`, `database_port`, `database_name`,
    `database_user`, and `database_password` to `env.yml`.

3. Created `playbook_main_tear_down.yml` and
`playbook_tear_down_chameleon_instances.yml`

    Quinn's time: N/A

    Lessley's time: 0.30 hours

    Total time: 0.30 hours

    Created `playbook_main_tear_down.yml`, which runs 
    `playbook_tear_down_chameleon_instances.yml` to automatically
    remove Chameleon instances.

3. Configured, tested, and troubleshot end-to-end pipeline

   Quinn's time: N/A

   Lessley's time: 2 hours

   Total time: 2 hours

   Ran and debugged issues with `playbook_set_up_couch_db.yml`,
   `playbook_main_tear_down.yml`, and
   `playbook_tear_down_chameleon_instances.yml`, including:
    - Initial use of incorrect IP address when creating database
    - Mistakenly attempting to destroy Chameleon instances from
    Chameleon instances rather than vagrant-created machine

4. Learned about tags to specify which tasks to run

    Quinn's time: N/A

    Lessley's time: 0.30 hours

    Total time: 0.30 hours

    Discovered how to specify which tasks to run with tags and
    added `milestone3` tag to run applicable tasks for this
    milestone. Updated `Vagrantfile` to run `playbook_main_set_up.yml`
    with the `milestone3` tag.

### Total time expended

The total time expended for this milestone for Quinn and Lessley was 5.5 hours.

## Part 3: Video demo

The following is a demonstration of the work completed for this milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EfUkmeanrCVKkqOYzpyt758BbtzkM9gUI_2rbCNGmXH0Uw?e=a5SOCz

## Part 4: Running the code

__Pre-Requisites__

Use any macOS or Linux machine with `vagrant` and `VirtualBox`
installed.

Find/replace all occurrences of `*USER*` in `src` with a username.

Find/replace all occurrences of `*PASSWORD*` in `src` with a password.

__Steps to run__

From the `assignment_2/src/ansible-vagrant` directory:

`vagrant up --no-provision`

`vagrant provision`

`vagrant ssh`

From `~/kafka_config`:

`python3 seattle_producer.py`

`python3 new_york_producer.py`

Accessing the `couchdb` UI:

http://129.114.27.100:5984/_utils/

Log in with the username/password you used in the find/replace called out in the pre-requisites section above.