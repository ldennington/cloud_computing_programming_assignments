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

Quinn's time: 0.25 hours

Lessley's time: 0.25 hours

Total time: 0.50 hours

We set up separate producer code to publish to topics on our
Chameleon/AWS VMs. See [`seattle_producer`](src/seattle_producer.py) and
[`new_york_producer`](src/new_york_producer.py) for details.

### Chameleon Instances

Quinn's time: 2.00 hours

Lessley's time: 1.00 hour

Total time: 3.00 hours

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

Quinn's time: 1.50 hours

Lessley's time: 0.30 hours

Total time: 1.80 hours

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

The total time expended for this milestone for Quinn and Lessley was about 5.30 hours.

## Part 3: Video demo

The following is a demonstration of the work completed for this Milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/ET8khfheBFtAjUX9cwHiLcABbAeOT_zQBTS4YcpmJ8me2Q?e=X5mJtr