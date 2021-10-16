# Assignment 2 Milestone 1

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Added Lessley's public key to `authorized_keys` on his Chameleon instance

__Lessley Dennington__

* Installed vagrant on host machine
* Updated `MyInventory` file with both of team 4's Chameleon VMs
* Updated `bootstrap.sh` with additional directories based on the `Vagrantfile` config described below
* Created `.ansible.cfg` with path to inventory, Python, and the private key to access Chameleon VMs
* Configured `Vagrantfile` to:
    1. Provision Ubuntu 20.04 Focal Fossa machine on VirtualBox
    2. Copy needed files from host machine to vagrant-provisioned
       machine
    3. Provision/configure ansible on the vagrant-provisioned machine
    4. Automatically run `playbook_main.yml` on vagrant-provisioned machine
* Updated tasks from `AnsibleOnly_Local_and_Cloud` to run on Vagrant-provisioned machine

## Part 2: Effort expended/learning curve

In order to complete this milestone, we did the following:

### Reviewing applicable materials

Quinn's time: N/A

Lessley's time: 1 hour

Total time: 1 hour

Watched videos of in-class lectures on ansible/vagrant to ensure basic understanding of these tools before attempting to use them. Also pulled/reviewed the following directories from the Scaffolding Code:

- `AnsibleOnly_Local_and_Cloud`
- `AnsibleVagrantCombo`
- `VagrantOnly`

### Setup

Quinn's time: N/A

Lessley's time: 0.25 hours

Total time: 0.25 hours

1. [Downloaded and installed](https://www.vagrantup.com/downloads) vagrant on host machine.
2. Copied tasks and configuration files from Scaffolding Code into team repo.
3. Generated and downloaded `clouds.yaml` from Chameleon.

### Configuration

Quinn's time: N/A

Lessley's time: 1 hour

Total time: 1 hour

1. `MyInventory` File

   Removed inapplicable NAT machine group/comments and updated `MyChameleonVMs` group with team 4's Chameleon instance IPs.

2. `Vagrantfile`

   Removed inapplicable comments and:
   1. Configured download/deployment of Ubuntu 20.04 Focal Fossa image
   2. Disabled VirtualBox GUI
   3. Set up `bootstrap.sh` to run on Vagrant-provisioned VM
   4. Copied the necessary files to correct directories on Vagrant-provisioned VM:
      * Private key file (into `~/.ssh`)
      * `.ansible.cfg` (into `~`)
      * Tasks from Scaffolding Code (into `~/ansible-vagrant/tasks`)
      * Kafka code, including `seattle_producer.py` and `new_york_producer.py` (into `~/kafka`)
      * `clouds.yaml` (into `~/.config/openstack/clouds.yaml`)
   5. Ensured private key permissions were correct
   6. Configured ansible:
      * Ensured `playbook_main.yml` would run automatically on `vagrant up`
      * Ensured ansible was installed on Vagrant-provisioned VM
      * Specified inventory file name

3. `bootstrap.sh`

   Quinn's time: N/A

   Lessley's time: 0.05 hours

   Total time: 0.05 hours

   Added needed directories according to `Vagrantfile` config:
   * `~/kafka`
   * `~/ansible-vagrant/tasks`

4. `.ansible.cfg`

   Quinn's time: N/A

   Lessley's time: 0.50 hours

   Total time: 0.50 hours

   Created `.ansible.cfg` file that specified:
   * Path to `MyInventory` file
   * Path to Python interpreter to use (`python3`)
   * Path to private key file
   * No host key checking

5. Tasks

   Quinn's time: N/A

   Lessley's time: 1 hour
   
   Total time: 1 hour

   Removed unnecessary comments and:
   * `playbook_get_facts_cloud_vm.yml` and `playbook_get_facts_cloud_vm_newway.yml`:
      * Added correct `cloud` name to align with `clouds.yaml` (`openstack`) and updated `server` to `team4-*`
   * `playbook_install_app_on_cloud_vm.yml` and `playbook_install_app_on_local_vm.yml`:
      * Modernized task style
      * Updated to install `python3-pip` and `python3-openstackclient` as well as `subversion`
   * `playbook_main.yml`:
      * Added pre-task to install `python3-pip` and `python3-openstackclient` (required for `playbook_get_facts_cloud_vm.yml` to execute)

### Total time expended

The total time expended for this milestone for Quinn and Lessley was
about 4.25 hours.

## Part 3: Video demo

The following is a demonstration of the work completed for this milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EeD2yhutc4BMuzq-Z3eH15EBE-DCxFe3smuCKGKPhTVxlw?e=5FpmaE

## Part 4: Running the code

__Pre-Requisites__

Use any macOS or Linux machine with `vagrant` and `VirtualBox`
installed.

Check out commit `24ba23f ` to access the correct `src` for this
Milestone.

__Steps to run__

From the `assignment_2/src/ansible-vagrant` directory:

`vagrant up`

If you would like to run playbooks:

`vagrant ssh`

`cd ansible-vagrant/tasks`

`ansible-playbook <playbook-name>`
