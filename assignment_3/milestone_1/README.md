# Assignment 3 Milestone 1

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Added tasks to install and configure docker and kubernetes, including:
    * Installing needed dependencies
    * Adding the docker/kubernetes gpg keys and repos as `apt` sources
    * Installing docker/kubernetes
    * Configuring docker/kubernetes
* Met with Lessley on October 25 to record demo

__Lessley Dennington__
* Determined how to re-size Chameleon VM
* Split out docker/kubernetes tasks into 4 new playbooks:
    * `playbook_install_docker.yml`
    * `playbook_install_kubernetes.yml`
    * `playbook_kubernetes_main.yml`
    * `playbook_kubernetes_worker.yml`
* Determined how to manually:
    * Set up docker/kubernetes `ufw` rules on Chameleon VMs
    * Initialize/configure a cluster
    * Set up `flannel`
    * Join the machine to a cluster as a worker
    * Taint the master machine to allow it to also function as a worker
    * Deploy various pods on the cluster
* Created `README.md`
* Met with Quinn on October 25 to record demo

## Part 2: Effort expended/learning curve

In order to complete this milestone, we did the following:

### Reviewing applicable materials

Quinn's time: 1 hour

Lessley's time: 1 hour

Total time: 2 hours

Watched videos of in-class lectures and reviewed self-study slides on docker/kubernetes to ensure basic understanding of these tools before attempting to use them. Also pulled/reviewed the following directories from the Scaffolding Code:

- `DockerCluster_wKubernetes`

### Re-sizing Chameleon VM

Quinn's time: N/A

Lessley's time: 0.25 hours

Total time: 0.25 hours

Determined how to resize Chameleon VM from `m1.small` to `m1.medium`.

### Adding playbooks to install/configure docker and kubernetes

1. Added `playbook_install_docker.yml`

    Quinn's time: 2.5 hours

    Lessley's time: 0.15 hours

    Total time: 2.65 hours

    Determined how to correctly install docker on our Chameleon VMs and added the appropriate tasks to a new playbook, including:

    1. Installing the needed dependencies via `apt`
    0. Adding the appropriate GPG key and repo as an `apt` source
    0. Installing docker
    0. Installing docker SDK for Python

0. Added `playbook_install_kubernetes.yml`

    Quinn's time: 2.5 hours

    Lessley's time: 0.15 hours

    Total time: 2.65 hours

    Determined how to correctly install kubernetes on our Chameleon VMs and added the appropriate tasks to a new playbook, including:

    1. Installing the needed dependencies via `apt`
    0. Adding the appropriate GPG key and repo as an `apt` source
    0. Installing applicable kubernetes packages via `apt`
    0. Permanently disabling swap
    0. Loading the docker daemon and restarting docker

0. Added `playbook_kubernetes_main.yml`

    Quinn's time: 0.5 hours

    Lessley's time: 0.15 hours

    Total time: 0.65 hours

    Determined how to set up `main` VM and added the appropriate tasks to a new playbook, including:

    1. Creating a descriptive hostname
    0. Restarting `kubelet`

0. Added `playbook_kubernetes_worker.yml`

    Quinn's time: 0.1 hours

    Lessley's time: 0.15 hours

    Total time: 0.25 hours

    Determined how to set up `worker` VM and added the appropriate tasks to a new playbook, including:

    1. Creating a descriptive hostname

### Manual setup/running scaffolding code

1. Manual VM setup

    Quinn's time: N/A

    Lessley's time: 1 hour

    Total time: 1 hour
    
    Determined how to execute manual configuration required for the assignment on VMs, including:

    1. Initializing a cluster
    0. Setting up `flannel` to enable network virtualization for cluster/pods
    0. Joining a machine to the cluster as a worker
    0. Tainting the main machine to allow it to also function as a worker

0. Running `DockerCluster_wKubernetes` scaffolding code

    Quinn's time: N/A

    Lessley's time: 2 hours

    Total time: 2 hours

    Determined how to deploy pods on cluster, including:

    1. Adding the `KUBERNETES_PORTS` Security Group and docker/kubernetes ufw rules to Chameleon VMs
    0. Adding insecure registry to `/etc/docker/daemon.json`
    0. Creating a Job pod based on the scaffolding code
    0. Building/tagging a custom Docker image
    0. Creating a registry
    0. Pushing the image to the registry
    0. Creating a Deployment pod based on the scaffolding code
    0. Creating a Service_Job pod based on the scaffolding code

### Total time expended

The total time expended for this milestone for Quinn and Lessley was 11.45 hours.

## Part 3: Video demo

The following are video demonstrations of the work completed for this milestone.
We added parts 2 and 3 after the full scope of the assignment was clarified in Slack.

__Part 1:__

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EeGfKbd-0ZRGmV5YwXUhrtkBo7xuHzH7rFWw8YcYp8g4FA?e=7s3hvf

__Part 2:__

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EZ5ep-7tHCxPqQfCcvbz91oBdMLjpm3Och9PtMWM3mUgIA?e=Irczhm

__Part 3:__

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EZ7ksvu5ZZFFvcO3HiWQHEMBio-3CU1IEhrTlcnLdBn7Ug?e=NbfJps

## Part 4: Running the code

### Part 1: Installing docker/kubernetes on Chameleon VMs

__Pre-Requisites__

Use any macOS or Linux machine with `vagrant` and `VirtualBox`
installed.

__Steps to run__

From the `assignment_3/milestone_1/src/ansible-vagrant` directory:

`vagrant up`

### Part 2: Manual setup/running scaffolding code

__Pre-Requisites__

Use any macOS or Linux machine with:
* Docker and kubernetes installed
* Nodes named `kubernetes-main` and `kubernetes-worker`
* The `DockerCluster_wKubernetes` scaffolding code present

__Steps to run__

Initialize cluster:

```
sudo kubeadm init --node-name kubernetes-main --pod-network-cidr=10.244.0.0/16 &&
mkdir -p $HOME/.kube &&
sudo cp -i /etc/kubernetes/admin.conf $HOME/.kube/config &&
sudo chown $(id -u):$(id -g) $HOME/.kube/config
```

Set up flannel:

`kubectl apply -f https://raw.githubusercontent.com/coreos/flannel/master/Documentation/kube-flannel.yml`

Join worker:

__Note:__ The full command is in the output of the `kubeadm init` command run above.

`sudo kubeadm join 10.60.5.196:6443 --token <token> --discovery-token-ca-cert-hash <hash>`

Taint:

`kubectl taint nodes kubernetes-main node-role.kubernetes.io/master:NoSchedule-`

Show control plane pods are running and `kubernetes-main` and `kubernetes-worker` are in cluster:

`kubectl get pods -A`

`kubectl get nodes`

Create `Deployment` pod:

From the `Deployment` directory of `DockerCluster_wKubernetes`:

`kubectl apply -f nginx-deployment.yaml`

`kubectl get deployments`

`kubectl get pods --all-namespaces`

Create `Job` pod:

From the `Job` directory of `DockerCluster_wKubernetes`:

`sudo docker build . -f dockerfile -t my_matinv` (on `kubernetes-main` and `kubernetes-worker`)

`sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2`

`sudo docker ps`

`sudo docker tag my_matinv:latest localhost:5000/my_matinv`

`sudo docker push localhost:5000/my_matinv`

`docker images`

`kubectl apply -f matinv-job_wLocalImage.yaml`

`kubectl apply -f matinv-job_wCorrectRegistry.yaml`

`kubectl get pods`

Create `Service_Job` pod:

From the `Service_Job` directory of `DockerCluster_wKubernetes`:

`sudo docker build . -f dockerfile_server -t matinv_server`

`sudo docker run -d -p 5000:5000 --restart=always --name registry registry:2`

`sudo docker tag matinv_server:latest <IP address>:5000/matinv-server`

`sudo docker push <IP address>:5000/matinv-server`

`kubectl apply -f matinv-server-svc.yaml`

`kubectl apply -f matinv-server-job.yaml`

`kubectl get pods`

`kubectl exec -it <pod name> -- /usr/bin/bash`

`ps -ef | grep python`

From separate VM:

`python3 matinv_client.py -a <IP address>:30000 -d 3000 results.txt`

Cleanup:

`kubectl delete -f <pod_yaml_file>`

```
sudo kubeadm reset &&
sudo rm -r /home/cc/.kube &&
sudo rm -r /etc/cni/net.d
```

