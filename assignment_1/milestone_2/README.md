# Programming Milestone 2

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__

* Installed producer code on local Ubuntu VM
* Set up local producer code to stream to `MeetUpNewYork` topic
on Chameleon/AWS instances
* Installed Apache Kafka on Chameleon/AWS instances
* Set up `server.properties` to enable streaming from local Ubuntu VM to
Chameleon instance
* Set up Zookeeper on Chameleon/AWS instances
* Installed consumer on Chameleon/AWS instances
* Set up consumer to receive data from `MeetUpNewYork` and `MeetUpSeattle`
topics
* Met with Lessley on Sept. 19 to discuss assignment/pair program
* Met with Lessley on Sept. 21 to create [video demo](#part-3-video-demo)

__Lessley Dennington__

* Installed producer code on local Ubuntu VM
* Set up local producer code to stream to `MeetUpSeattle` topic
on Chameleon instance
* Installed Apache Kafka on Chameleon instance
* Set up `server.properties` to enable streaming from local Ubuntu VM to
Chameleon instance and to stream to Zookeeper on Quinn's Chameleon instance
* Created `README.md`
* Met with Quinn on Sept. 19 to discuss assignment/pair program
* Met with Quinn on Sept. 21 to create [video demo](#part-3-video-demo)

## Part 2: Effort expended

In order to complete this milestone, we completed the following steps:

### Local Ubuntu VMs

We set up created separate producer code to publish to topics on Chameleon/AWS
VMs. See [`seattle_producer`](src/seattle_producer.py) and
[`new_york_producer`](src/new_york_producer.py) for details.

### Chameleon Instances

We installed Apache Kafka on both our Chameleon VM instances. We each updated
our instance's `server.properties` file to enable streaming from local Ubuntu
VM to the instance.

We installed and configured Zookeeper on 1 VM instance and created
our `MeetUpNewYork` and `MeetUpSeattle` topics. We modified both
`server.properties` files to stream to Zookeeper on this single instance.

Finally, we modified the [`consumer.py`](src/consumer.py) code to subscribe to
both our topics and deployed it to the same Chameleon instance that is running
Zookeeper.

### AWS Instances

<Quinn to complete>

## Part 3: Video demo

The following is a demonstration of the work completed for this Milestone:

<Insert link here>
