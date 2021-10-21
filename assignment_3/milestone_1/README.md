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
    * Set up `flannel`
    * Initialize a cluster
    * Join the machine to a cluster as a worker
    * Taint the master machine to allow it to also function as a worker
    * Deploy deployment/worker pods on the previously-created cluster
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
    2. Adding the appropriate GPG key and repo as an `apt` source
    3. Installing docker
    4. Installing docker SDK for Python

2. Added `playbook_install_kubernetes.yml`

    Quinn's time: 2.5 hours

    Lessley's time: 0.15 hours

    Total time: 2.65 hours

    Determined how to correctly install kubernetes on our Chameleon VMs and added the appropriate tasks to a new playbook, including:

    1. Installing the needed dependencies via `apt`
    2. Adding the appropriate GPG key and repo as an `apt` source
    3. Installing applicable kubernetes packages via `apt`
    4. Permanently disabling swap
    5. Loading the docker daemon and restarting docker

3. Added `playbook_kubernetes_main.yml`

    Quinn's time: 0.5 hours

    Lessley's time: 0.15 hours

    Total time: 0.65 hours

    Determined how to set up `main` VM and added the appropriate tasks to a new playbook, including:

    1. Creating a descriptive hostname
    2. Restarting `kublet`

4. Added `playbook_kubernetes_worker.yml`

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

    * Initializing a cluster
    * Setting up `flannel` to enable network virtualization for cluster/pods
    * Joining a machine to the cluster as a worker
    * Tainting the main machine to allow it to also function as a worker

2. Running `DockerCluster_wKubernetes` scaffolding code

    Quinn's time: N/A

    Lessley's time: 1 hour

    Total time: 1 hour

    Determined how to deploy deployment/worker pods on cluster, including:

    1. Creating a Job pod based on the scaffolding code
    2. Building/tagging a custom Docker image
    3. Creating a registry
    4. Pushing the image to the registry
    2. Creating a Deployment pod based on the scaffolding code

### Total time expended

The total time expended for this milestone for Quinn and Lessley was 10.45 hours.

## Part 3: Video demo

The following are video demonstrations of the work completed for this milestone:

__Part 1:__

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EeGfKbd-0ZRGmV5YwXUhrtkBo7xuHzH7rFWw8YcYp8g4FA?e=7s3hvf

__Part 2:__

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EZ5ep-7tHCxPqQfCcvbz91oBdMLjpm3Och9PtMWM3mUgIA?e=Irczhm

__Note:__ We did not realize running the `Service_Job` was required for this assignment, but we were given an extension and will demo it as part of the next assignment. See [this thread](https://fall2021cs428-6eu5219.slack.com/archives/C02C84ADPEH/p1635217156019300) for details.

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

Cleanup:

`kubectl delete -f <pod_yaml_file>`

```
sudo kubeadm reset &&
sudo rm -r /home/cc/.kube &&
sudo rm -r /etc/cni/net.d
```

