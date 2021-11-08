# Assignment 3 Milestone 2

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Attempted automation of manual steps on AWS
* Met with Lessley on November 8 to film demos

__Lessley Dennington__
* Determined how to tear down K8s cluster
* Created `docker_kubernetes/kafka-pipeline` directory, which contains
our k8s YAML and docker files:
    * `consumer-job.yml`
    * `consumer.py`
    * `couchdb-deployment.yml`
    * `couchdb-svc.yml`
    * `dockerfile-consumer`
    * `env.yml`
    * `kafka-deployment-main`
    * `kafka-deployment-worker`
    * `kafka-svc-main`
    * `kafka-svc-main`
    * `zookeeper-deployment.yml`
    * `zookeeper-svc.yml`
* Extended `playbook_kubernetes_main.yml` to automatically:
    * Make `kubelet` file
    * Initialize cluster
    * Create `.kube` directory and `Admin.conf` file
    * Install Flannel
    * Generate the join command, save it to a file, and copy the file
    to the `kubernetes-worker` VM
    * Taint `kubernetes-main`
* Extended `playbook_kubernetes_worker.yml` to:
    * Join `kubernetes-worker` to the cluster
* Created `README.md`
* Met with Quinn on November 8 to film demos

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

Extended the `main`/`worker` playbooks to execute steps we previously
completed manually, including:

* Initializing the cluster
* Creating the required configuration files/directories for the cluster
* Installing flannel
* Generating the join command for the worker, writing it to a file,
and copying it to the worker
* Running the join command on the worker
* Tainting main

### Attempted automation of manual steps on AWS

Quinn's time: 12 hours

Lessley's time: N/A

Total time: 12 hours

Quinn generally does his development on AWS so that we don't clash on
our Chameleon VMs. He spent around 12 hours attempting to automate
the deployment of zookeeper, the kafka brokers, couchdb, and the
consumer as separate pods. In the end we determined he should shift
focus to our final project while I continued to work on the Chameleon
deployment. Because he spent so much time, however, it would be remiss
not to record those hours here.

### Added `docker_kubernetes/kafka-pipeline` directory

Quinn's time: N/A

Lessley's time: 14 hours

Total time: 14 hours

This new directory contains the following, which allowed us to run the
manual commands below:

* `consumer-job.yml` - k8s yaml file to run our custom-built consumer
docker image as a job pod
* `consumer.py` - the same `consumer.py` we've used in previous
assignments
* `couchdb-deployment.yml` - k8s yaml file to run couchdb as a
deployment pod
* `couchdb-svc.yml` - k8s yaml file to run service that exposes couchdb
for easy connectivity via web browser on local machine
* `dockerfile-consumer` - dockerfile that builds custom consumer image
* `env.yml` - the same `consumer.py` we've used in previous
assignments, with modification of `database_name` and `database_port`
according to this milestone's requirements
* `kafka-deployment-main` - k8s yaml file to run a kafka broker on
`kubernetes-main` as a deployment pod
* `kafka-deployment-worker` - k8s yaml file to run a kafka broker on
`kubernetes-worker` as a deployment pod
* `kafka-svc-main` - k8s yaml file to run service that exposes kafka
broker on `kubernetes-main` for outside `producer` connections
* `kafka-svc-worker` - k8s yaml file to run service that exposes kafka
broker on `kubernetes-worker` for outside `producer` connections
* `zookeeper-deployment.yml` - k8s yaml file to run zookeeper as a
deployment pod
* `zookeeper-svc.yml` - k8s yaml file to run service that exposes
zookeeper for easy connectivity via web browser on local machine

### Total time expended

The total time expended for this milestone for Quinn and Lessley was 29
hours.

## Part 3: Video demo

The following is a video demonstration of the work completed for this
milestone:

## Part 4: Running the code

__Pre-Requisites__

Use any macOS or Linux machine with `vagrant` and `VirtualBox` installed.

__Steps to run__

From the `assignment_3/milestone_2/src/ansible-vagrant` directory:

`vagrant up`

__Pre-Requisites__

One `main` Linux machine with:
* The needed ports and SGs for docker/kubernetes configured
* Docker and kubernetes installed/configured
* Name of `kubernetes-main` 
* The `docker_kubernetes` directory from this assignment present
* Steps outlined in [Milestone 1's README](../../milestone_1/README.md)
to initialize cluster, set up flannel, taint, and designate
insecure registry completed

One `worker` Linux machine with:
* The needed ports and SGs for docker/kubernetes configured
* Docker and kubernetes installed/configured
* Name of `kubernetes-worker`
* Steps outlined in [Milestone 1's README](../../milestone_1/README.md)
to join the cluster completed

__Steps to run__

From the `docker_kubernetes/kafka-pipeline` directory on
`kubernetes_main`:

1. Build/tag/push custom `consumer` image:

    `docker build . -f dockerfile-consumer -t consumer`

    `sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2`

    `docker tag consumer:latest <IP Address>:5000/consumer`

    `docker push <IP Address>:5000/consumer`

0. Set up zookeeper service/pod:

    `kubectl apply -f zookeeper-svc.yml`

    `kubectl apply -f zookeeper-deployment.yml`

0. Set up kafka services/pods:

    `kubectl apply -f kafka-svc-main.yml`

    `kubectl apply -f kafka-deployment-main.yml`

    `kubectl apply -f kafka-svc-worker.yml`

    `kubectl apply -f kafka-deployment-worker.yml`

0. Set up couchdb service/pod/database:

    `kubectl apply -f couchdb-svc.yml`

    `kubectl apply -f couchdb-deployment.yml`

    `curl -X PUT http://admin:password@129.114.27.100:30002/assignment_three`

0. Set up `consumer` pod:

    `kubectl apply -f consumer-job.yml`

From `kafka_config` directory in one terminal on local machine:

    python3 seattle_producer.py

From `kafka_config` directory in one terminal on local machine:

    python3 new_york_producer.py

Accessing `couchdb` from web browser on local machine:

http://<IP ADDRESS>:30002/_utils

Enter username/password specified in `curl` command above

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