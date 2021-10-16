# Programming Milestone 2

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__

* Set up new Ubuntu 20.04 AWS instance
* Installed necessary packages (e.g. `default-jre` and `default-jdk`) and Apache
Kafka on AWS instance
* Set up Chameleon instance `server.properties` to enable streaming from local
Ubuntu VM to Chameleon instance and AWS `server.properties` to enable streaming
from local Ubuntu VM to AWS instance
* Installed/configured Zookeeper on Chameleon instance and created
 `MeetUpNewYork` and `MeetUpSeattle` topics
* Installed consumer on Chameleon instance and updated it to subscribe to
 `MeetUpNewYork` and `MeetUpSeattle` topics
* Installed producer code on local Ubuntu VM
* Set up local producer code to stream to `MeetUpNewYork` topic
on Chameleon/AWS instances
* Met with Lessley on Sept. 19 to discuss assignment/pair program
* Met with Lessley on Sept. 21 to create [video demo](#part-3-video-demo)

__Lessley Dennington__

* Set up new Ubuntu 20.04 AWS instance
* Installed necessary packages (e.g. `default-jre` and `default-jdk`) and Apache
Kafka on AWS instance
* Set up Chameleon instance `server.properties` to enable streaming from local
Ubuntu VM to Chameleon instance and AWS `server.properties` to enable streaming
from local Ubuntu VM to AWS instance
* Installed/configured Zookeeper on AWS instance and created
 `MeetUpNewYork` and `MeetUpSeattle` topics
* Installed consumer on AWS instance and updated it to subscribe to
 `MeetUpNewYork` and `MeetUpSeattle` topics
* Installed producer code on local Ubuntu VM
* Set up local producer code to stream to `MeetUpSeattle` topic
on Chameleon/AWS instances
* Met with Quinn on Sept. 19 to discuss assignment/pair program
* Met with Quinn on Sept. 21 to create [video demo](#part-3-video-demo)

## Part 2: Effort expended

In order to complete this milestone, we did the following:

### Local Ubuntu VMs

We set up separate producer code to publish to topics on our
Chameleon/AWS VMs. See [`seattle_producer`](src/seattle_producer.py) and
[`new_york_producer`](src/new_york_producer.py) for details.

### Chameleon Instances

Quinn's time: 120 minutes
Lessley's time: 60 minutes
Total time: 180 minutes

We installed necessary packages and Apache Kafka on both our Chameleon VM instances.
We each updated our instance's `server.properties` file to enable streaming from
our local Ubuntu VMs to the instance.

We installed and configured Zookeeper on 1 VM instance and created
our `MeetUpNewYork` and `MeetUpSeattle` topics. We modified both
`server.properties` files to stream to Zookeeper on this single instance.

Finally, we modified the [`consumer.py`](src/consumer.py) code to subscribe to
both our topics and deployed it to the same Chameleon instance that is running
Zookeeper.

### AWS Instances

Quinn's time: 90 minutes
Lessley's time: 20 minutes
Total time: 110 minutes

We installed necessary packages and Apache Kafka on both our AWS VM instances.
We each updated our instance's `server.properties` file to enable streaming from
our local Ubuntu VMs to the instance.

We installed and configured Zookeeper on 1 VM instance and created
our `MeetUpNewYork` and `MeetUpSeattle` topics. We modified both
`server.properties` files to stream to Zookeeper on this single instance.

Finally, we modified the [`consumer.py`](src/consumer.py) code to subscribe to
both our topics and deployed it to the same AWS instance that is running
Zookeeper.

### Total time expended

The total time expended for this milestone for Quinn and Lessley was
290 minutes, or 4.8 hours.

## Part 3: Video demo

The following is a demonstration of the work completed for this Milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/ET8khfheBFtAjUX9cwHiLcABbAeOT_zQBTS4YcpmJ8me2Q?e=X5mJtr

## Part 4: Running the code

__Pre-Requisites__

Use the same machine you configured for running the Milestone 1 code.
See the
[Milestone 1 README](../milestone_1/README.md) for additional
details.

__Steps to run__

From the `assignment_1/milestone_2/src` directory:

`python3 seattle_producer.py`

`python3 new_york_producer.py`

__Additional notes__

If you would like to verify streaming to `consumer.py` locally, please
do the following:

1. Modify the `bootstrap_servers` array value in either
`seattle_producer.py` or `new_york_producer.py` to `'localhost:9092'`.
2. Modify the `bootstrap_servers` array value in `consumer.py` to
`'localhost:9092'`.
3. Open a terminal, navigate to `assignment_1/milestone_2/src`, and
run the producer you modified.
4. Open a second terminal, navigate to `assignment_1/milestone_2/src`,
and run the modified consumer.
5. The running consumer will print "hits" from the running producer.
