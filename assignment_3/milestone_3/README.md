# Assignment 3 Milestone 3

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Met with Lessley on November 8 to film demo

__Lessley Dennington__
* Created `playbook_kubernetes_kafka.yml` playbook, which does the following:
    1. Creates a private registry (where we push the custom consumer
    image)
    0. Designates the private registry as insecure and restarts docker
    0. Builds and tags the custom consumer image and pushes it to the
    previously-created registry
    0. Creates the service and deployment pods
    0. Sleeps for 1 minute to ensure pods are created/running
    0. Creates the `assignment_3` couchdb database
    0. Creates the consumer job pod
* Created `README.md`
* Met with Quinn on November 8 to film demo

## Part 2: Effort expended/learning curve

In order to complete this milestone, we did the following:

### Created new `playbook_kubernetes_kafka.yml` file to automate setup of k8s cluster

Quinn's time: N/A

Lessley's time: 8 hours

Total time: 8 hours

Created a new playbook to automate deployment of our k8s pods, including:

1. Creating the private registry - this task replaces the following
command from the manual steps outlined in the
[Milestone 2 `README`](../milestone_2/README.md):

    `sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2`

0. Designating the private registry as insecure and restarting docker -
this replaces the following manual step outlined in the
[Milestone 1 `README`](../milestone_1/README.md):

    Add this line in `/etc/docker/daemon.json`:

    `"insecure-registries": ["<IP Address>:5000"]`

0. Building and tagging the custom consumer image and pushing it
to the previously-created registry - this task replaces the following
commands from the manual steps outlined in the
    [Milestone 2 `README`](../milestone_2/README.md):

    `docker build . -f dockerfile-consumer -t consumer`

    `docker tag consumer:latest <IP Address>:5000/consumer`

    `docker push <IP Address>:5000/consumer`

0. Creating the services and deployment pods - this replaces the
following commands from the manual steps outlined in the
[Milestone 2 `README`](../milestone_2/README.md):

    `kubectl apply -f zookeeper-svc.yml`

    `kubectl apply -f zookeeper-deployment.yml`

    `kubectl apply -f kafka-svc-main.yml`

    `kubectl apply -f kafka-deployment-main.yml`

    `kubectl apply -f kafka-svc-worker.yml`

    `kubectl apply -f kafka-deployment-worker.yml`

    `kubectl apply -f couchdb-svc.yml`

    `kubectl apply -f couchdb-deployment.yml`

0. Sleeping for 1 minute to ensure pods are created/running - this was
not necessary when running commands manually in Milestone 2

0. Creates the `assignment_3` couchdb database - this replaces the
following commands from the manual steps outlined in the
[Milestone 2 `README`](../milestone_2/README.md):

    `curl -X PUT http://admin:password@129.114.27.100:30002/assignment_three`

0. Creating the consumer Job pod  - this replaces the following
commands from the manual steps outlined in the
[Milestone 2 `README`](../milestone_2/README.md):

    `kubectl apply -f consumer-job.yml`

__Note__: This step involved some trial and error, which is why we
logged so many hours. Issues we had to resolve included:

1. Accidentally running the new playbook on the wrong VM
    * This included a few different re-writes of the new playbook with
    different task types to attempt to get things to work
2. Determining which tasks to run with elevated privileges and marking
them correctly
3. Determining how to programatically update the
`/etc/docker/daemon.json` file to mark the registry as insecure
4. Determining that we needed to add a `sleep` task to ensure the
deployment pods were fully up and running before creating the database

### Total time expended

The total time expended for this milestone for Quinn and Lessley was 8
hours.

## Part 3: Video demo

The following is a video demonstration of the work completed for this
milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EW_WYx0NBgVNvNGrEB6si40BHinq5NfO235bT8JpCmj4MA?e=52Fw7B

## Part 4: Running the code

__Pre-Requisites__

Use any macOS or Linux machine with `vagrant` and `VirtualBox` installed.

__Steps to run__

From the `assignment_3/milestone_3/src/ansible-vagrant` directory on
local machine:

`vagrant up`

From `kafka_config` directory in one terminal on local machine:

`python3 seattle_producer.py`

From `kafka_config` directory in another terminal on local machine:

`python3 new_york_producer.py`

Accessing `couchdb` from web browser on local machine:

http://<IP ADDRESS>:30002/_utils

Enter username/password specified in `playbook_kubernetes_kafka.yml`

## Appendix: Cleanup commands

### Tearing down cluster

`kubernetes-main`:

```
sudo kubeadm reset &&
sudo rm -r /home/cc/.kube &&
sudo rm -r /etc/cni/net.d &&
sudo rm /etc/default/kubelet
```

`kubernetes-worker`:

`sudo kubeadm reset`

### Removing custom registry

`docker ps` (to obtain ID)

`docker rm <ID> -f`