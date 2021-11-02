# Assignment 3 Milestone 2

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Created `docker_kubernetes/Compose` directory, which contains:
    * `consumer-compose` docker file
    * `consumer.py`
    * `couchdb-compose`
    * `env.yml`
    * `kafka-compose`
    * `zookeeper-compose`
More details on these files are included below
* Met with Lessley on November 2 to film demos

__Lessley Dennington__
* Determined how to tear down K8s cluster
* Extended `playbook_kubernetes_main.yml` to automatically:
    * Make `kubelet` file
    * Initialize cluster
    * Create `.kube` directory and `Admin.conf` file
    * Install Flannel
    * Generate the join command, save it to a file, and copy the file to the `kubernetes-worker` VM
    * Taint `kubernetes-main`
* Extended `playbook_kubernetes_worker.yml` to:
    * Join `kubernetes-worker` to the cluster
* Created `README.md`
* Met with Quinn on November 2 to film demos

## Part 2: Effort expended/learning curve

In order to complete this milestone, we did the following:

### Determined how to tear down K8s cluster

Quinn's time: N/A

Lessley's time: 0.25 hours

Total time: 0.25 hours

Determined how to correctly tear down K8s cluster and remove associated
files (see Appendix below for details).

### Extended `playbook_kubernetes_main.yml` and `playbook_kubernetes_worker.yml`

Quinn's time: N/A

Lessley's time: 2.5 hours

Total time: 2.5 hours

Extended our `main`/`worker` playbooks to execute steps we previously completed
manually, including:

* Initializing the cluster
* Creating the required configuration files/directories for the cluster
* Installing flannel
* Generating the join command for the worker, writing it to a file, and copying it to the worker
* Running the join command on the worker
* Tainting main

### Added `docker_kubernetes/Compose` directory

Quinn's time: 3.5 hours

Lessley's time: N/A

Total time: 3.5 hours

This new directory contains the following, which allowed us to run the
manual commands below:

* `consumer-compose` - a docker file to install dependencies for and run `consumer.py`
* `consumer.py` - the consumer we've been using throughout the class
* `couchdb-compose` - a yaml file to set up the `couchdb` docker image
* `env.yml` - the `couchdb` config file we've been using throughout the class,
with an updated name for this assignment
* `kafka-compose` - a yaml file to set up the `kafka` docker image
* `zookeeper-compose` - a yaml file to set up the `zookeeper` image

### Total time expended

The total time expended for this milestone for Quinn and Lessley was 6.25 hours.

## Part 3: Video demo

The following are video demonstrations of the work completed for this milestone.
We chose to divide into 2 parts to highlight each team member's contributions and
minimize wasted time running the process end-to-end multiple times to capture an
effective demo.

__Part 1__

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EbywYT_bFDdNtfqdTce6KKgB9J8psBxNjGr4wmBVHexjBg?e=U9Cybo

__Part 2__

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EYuiDbkc9P1CuGhdmXdgaf4BWkU01ve6F5m620X3lHsFXw?e=2TCL1h

## Part 4: Running the code

__Pre-Requisites__

Use any macOS or Linux machine with `vagrant` and `VirtualBox` installed.

__Steps to run__

From the `assignment_3/milestone_2/src/ansible-vagrant` directory:

`vagrant up`

__Pre-Requisites__

One `main` Linux machine with:
* Docker and kubernetes installed/configured
* Name of `kubernetes-main` 
* The `docker_kubernetes` directory from this assignment present
* Steps outlined in [Milestone 1's README](../../milestone_1/README.md)
to initialize cluster, set up flannel, and taint completed

One `worker` Linux machine with:
* Docker and kubernetes installed/configured
* Name of `kubernetes-worker`
* Steps outlined in [Milestone 1's README](../../milestone_1/README.md)
to join the cluster completed

__Steps to run__

From the `docker_kubernetes/Compose` directory:
1. Set up Docker Zookeeper:

    `docker-compose -f zookeeper-compose.yml up -d`

0. Set up Docker Kafka:

    `docker-compose -f kafka-compose.yml up -d`

0. Create Topics

    ```
    docker run --rm ches/kafka kafka-topics.sh --create --topic MeetUpNewYork --replication-factor 1 --partitions 1 --zookeeper 129.114.27.100:2181 &&
    docker run --rm ches/kafka kafka-topics.sh --create --topic MeetUpSeattle --replication-factor 1 --partitions 1 --zookeeper 129.114.27.100:2181
    ```

0. Set up Docker CouchDB:

    `docker-compose -f couchdb-compose.yml up -d`
    `docker exec couchdb curl -X PUT http://admin:password@127.0.0.1:5984/assignment_three`

0. Docker Consumer:

    `docker build -f consumer-compose -t consumer . && sudo docker run -id consumer`

## Appendix: Cleanup and debugging commands

Tearing down cluster:

```
sudo kubeadm reset &&
sudo rm -r /home/cc/.kube &&
sudo rm -r /etc/cni/net.d &&
sudo rm /etc/default/kubelet
```

Viewing logs:

kubectl logs <pod name> -c <container name> to see if a container is running as expected