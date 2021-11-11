# Assignment 4 Milestone 1

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Met with Lessley on November 13 to film demo

__Lessley Dennington__
* Split data file into 2 csv files and stored in new `resources` directory:
    * `energy-sorted-part-1.csv`
    * `energy-sorted-part-2.csv`
* Re-named producers to `producer1.py` and `producer2.py`, and updated
with the following functionality:
    * Read from respective `csv` files 1000 rows at a time
    * Send lists of 1000 rows to respective kafka topics (`Producer1` and `Producer2`)
* Updated `consumer.py` with the following functionality:
    * Write lists of 1000 records sent by producers to `couchdb`
* Updated custom consumer image to install `requests` Python module
* Created `README.md`
* Met with Quinn on November 13 to film demo

## Part 2: Effort expended/learning curve

In order to complete this milestone, we did the following:

### Split data file

Quinn's time: N/A

Lessley's time: 0.25 hours

Total time: 0.25 hours

Split the data file into two files (`energy-sorted-part-1.csv` and
`energy-sorted-part-2.csv`) with 500,000 records each and put them
into the new `resources` directory.

### Updated producers

Quinn's time: N/A

Lessley's time: 2 hours

Total time: 2 hours

Re-named producers to `producer1.py` and `producer2.py` since they are
no longer streaming MeetUp data. Replaced functionality to stream
MeetUp data with reading from respective `csv` files 1000 rows at a time and publishing these lists to new kafka topics (`Producer1` and `Producer2`).

There were some challenges with this step, including:

1. Ensuring data was mapped to the correct keys
0. Determining how to send lists of 1000 rows to kafka (since
we previously streamed MeetUp data one item at a time) without reading/sending the same rows multiple times

### Updated consumer

Quinn's time: N/A

Lessley's time: 10 hours

Total time: 10 hours

Updated `consumer.py` to write lists of 1000 records from the
`Producer1` and `Producer2` topics to `couchdb`.

There were some challenges with this step, including:

1. Understanding the data structures published to `Producer1` and
`Producer2` topics
    * This involved a lot of trial and error first with the cluster
    then with a manually-created local environment for more rapid
    feedback/testing
0. Determining that the `db.save()` method we previously used to
publish to `couchdb` would not allow us to publish lists
0. Discovering the `requests` library and learning how to use it with
the `couchdb` APIs

### Updated custom consumer image

Quinn's time: N/A

Lessley's time: 0.15 hours

Total time: 0.15 hours

This was a minor change to update our custom consumer image to install the `requests` Python module, since we updated `consumer.py` to use it
to submit `couchdb` requests to save lists.

### Total time expended

The total time expended for this milestone for Quinn and Lessley was
12.4 hours.

## Part 3: Video demo

The following is a video demonstration of the work completed for this
milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EYTTFy6m1pNFuV5zfDkOfsUBtQNyq0gAweY0lvAbh6PahQ?e=svuQtE

## Part 4: Running the code

__Pre-Requisites__

Use any macOS or Linux machine with `vagrant` and `VirtualBox`
installed. Additionally, run this command to ensure the needed Pyhton
packages are installed:

```
pip install pandas &&
pip install requests
```

__Steps to run__

From the `assignment_4/milestone_1/src/ansible-vagrant` directory on
local machine:

`vagrant up`

From `kafka_config` directory in one terminal on local machine:

`python3 producer1.py`

From `kafka_config` directory in another terminal on local machine:

`python3 producer2.py`

Accessing `couchdb` from web browser on local machine:

`http://<IP ADDRESS>:30002/_utils`

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