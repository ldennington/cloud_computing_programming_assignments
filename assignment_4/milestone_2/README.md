# Assignment 4 Milestone 2

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__
* Wrote code to read from `assignment_four` database and write to
`assignment_four_averages` database in `mapreduce.py`
* Wrote `plot.py` code to graph execution times for different numbers
of Map/Reduce tasks
* Met with Lessley on December 1 to film demo

__Lessley Dennington__
* Created `spark_dockerfile` to build image for Spark Driver
* Created `spark-driver.conf`, `spark-worker.conf`, and `spark-env.sh`
to customize driver/worker configuration (e.g. ports, number of
map/reduce tasks, cores per worker, etc.)
* Created the following Job/Deployment K8s pods for Spark:
    * `spark-driver-job.yaml`
    * `spark-master-deploy.yaml`
    * `spark-worker-deploy.yaml`
* Solved MapReduce averaging problem (see [`mapreduce.py`](src/mapreduce.py))
* Created `run_iters.sh` to run multiple iterations of `spark-submit`
automatically
* Formatted data to be plotted with `plot.py`
* Created `README.md`
* Met with Quinn on December 1 to film demo

## Part 2: Effort expended/learning curve

In order to complete this milestone, we did the following:

### Created Spark config files and pods and deployed to K8s

Quinn's time: N/A

Lessley's time: 1.5 hours

Total time: 1.5 hours

Created the following dockerfile to build Spark driver image:

`spark_dockerfile`

Created the following config files for Spark:

* `spark-driver.conf`
* `spark-worker.conf`
* `spark-env.sh`

Created the following pods and ran on existing K8s
cluster:

* `spark-driver-job.yaml`
* `spark-master-deploy.yaml`
* `spark-worker-deploy.yaml`

The majority of time spent on this piece of the assignment was
reviewing slides/scaffolding code to understand the correct pod
structure and appropriate configs for Spark running in K8s.

### Read 1,000,000 records from `assignment_four` couchdb database

Quinn's time: 0.75 hours

Lessley's time: N/A

Total time: 0.75 hours

Read data from `assignment_four` couchdb database into pandas
dataframe in `mapreduce.py`.

### Transformed data from `assignment_four` database into average work and average load for 3-tuple key

Quinn's time: N/A

Lessley's time: 10 hours

Total time: 10 hours

Used `map`, `mapValues`, and `aggregateByKey` functions of `pyspark.RDD`
to transform input records from `assignment_four` couchdb in the
first format below into a collection of records in the second format
below in [`mapreduce.py`](src/mapreduce.py):

```
{
  "id": 753579,
  "timestamp": 1377986853,
  "value": 0,
  "property": 1,
  "plug_id": 6,
  "household_id": 13,
  "house_id": 28
}
```

```
{
  "key": [
    20,
    0,
    7
  ],
  "average_work": 173.8676588628762,
  "average_load": 107.01016722408026
}
```
There were some challenges with this step, including:

1. Learning curve associated with understanding RDDs and their
associated functions.
0. Deciding which RDD function was the correct one to use.
0. Understanding how to compute multiple averages based on a variable
field.

### Wrote code to write output to `assignment_four_averages` couchdb database

Quinn's time: 0.5 hours

Lessley's time: N/A

Total time: 0.5 hours

Wrote records containing averages produced via `pyspark.RDD`
functions to `assignment_four_averages` couchdb database.

### Created `run_iters.sh` to run multiple iterations of `spark-submit` automatically

Quinn's time: N/A

Lessley's time: 3 hours

Total time: 3 hours

Created `run_iters.sh` to automatically run 10 iterations of
`spark-submit`. Note that we manually changed the
`spark.default.parallelism` and `spark.sql.shuffle.partitions` to
update the number of Map/Reduce tasks between sets of 10 runs. After
updating we re-built, re-tagged, and re-pushed the `spark_dockerfile`
image and then started a new `spark-driver-job` pod.

There were some challenges with this step, including:

1. Determining how to format output of `time` command and write to a text file.
0. Determining how to install correct version of `time` in K8s pod.
0. Collecting times before the job completed.

### Wrote `plot.py` code to graph execution times for each set of Map/Reduce tasks

Quinn's time: 2 hours

Lessley's time: 0.5 hours

Total time: 2.5 hours

We decided to plot the results from our experiments with different
numbers of Map and Reduce tasks using `matplotlib`. We have
included a screenshot of the resulting plot [here](src/img/mr_completion.png).

We copied the output files from the 3 runs of `run_iters.sh`
executed by our Spark driver to `10_2.csv`, `50_5.csv`, and
`100_10.csv` in the `data` directory.

There were some challenges with this step, including:

1. Learning how to use `matplotlib` to plot our results
2. Customizing the plot to meet our needs (e.g. showing 90th, 95th,
and 99th percentiles)

### Total time expended

The total time expended for this milestone for Quinn and Lessley was
18.25 hours.

## Part 3: Video demo

The following is a video demonstration of the work completed for this
milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/EeWrV3v5D2ZEn_6uYZE5O3gBTFo2uWeVQa_aokxFyjiRCQ?e=zEoTii

## Part 4: Running the code

__Pre-Requisites__

* A Linux machine with a running K8s cluster and private registry
    * You will need to update the `image` IP address and
    `kubernetes.io/hostname` field in `spark-driver-job.yaml`,
    `spark-master-deploy.yaml`, and `spark-worker-deploy.yaml` for
    your cluster.
* A couchdb database running on your cluster containing the output
from Milestone 1 of this assignment and another database in which
to store the output of this Milestone
    * You will need to update the couchdb admin names/passwords, IP
    addresses, ports, and names in the `get_data` and `write_data`
    `mapreduce.py` methods accordingly.
* A machine with `python`, `numpy`, `matplotlib`, and `pandas`
installed 

__Steps to run__

[_mapreduce.py_](src/mapreduce.py)

From the `assignment_4/milestone_2/src` directory on
machine with K8s cluster:

`docker build . -f spark_dockerfile -t my-spark`

`docker tag my-spark:latest 129.114.27.100:5000/my-spark`

`docker push 129.114.27.100:5000/my-spark`

`kubectl apply -f spark-master-deploy.yaml`

`kubectl apply -f spark-worker-deploy.yaml`

`kubectl apply -f spark-driver-job.yaml`

The driver will automatically call `run_iters.sh` to run the
`mapreduce.py` code.

Accessing `couchdb` from web browser on local machine:

`http://<IP ADDRESS>:<port>/_utils`

Enter username/password.

[_plot.py_](src/plot.py)

From the `assignment_4/milestone_2/src` directory on the machine with
`numpy`, `matplotlib`, and `pandas` installed:

`python3 plot.py`