# Programming Milestone 3

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__

* Installed and configured `couchdb` on AWS instance
* Created `assignment_one` database on AWS instance
* Modified [`consumer.py`](src/consumer.py) to write to `couchdb` using the new
[`env.yml`](src/env.yml) file
* Met with Lessley on Sept. 21 to create [video demo](#part-3-video-demo)

__Lessley Dennington__

* Installed and configured `couchdb` on Chameleon instance
* Created `assignment_one` database on Chameleon instance
* Created Mango queries to separate Seattle/New York `couchdb` documents
* Created `README.md` for this milestone
* Met with Quinn on Sept. 21 to create [video demo](#part-3-video-demo)

## Part 2: Effort expended

In order to complete this milestone, we did the following:

### Installing/configuring `couchdb`

Quinn's time: 0.15 hours

Lessley's time: 1 hour

Total time: 1.15 hours

We used the following commands to install `couchdb` on one Chameleon and one AWS
instance:

```
sudo apt update && sudo apt install -y curl apt-transport-https gnupg
curl https://couchdb.apache.org/repo/keys.asc | gpg --dearmor | sudo tee /usr/share/keyrings/couchdb-archive-keyring.gpg >/dev/null 2>&1
source /etc/os-release
echo "deb [signed-by=/usr/share/keyrings/couchdb-archive-keyring.gpg] https://apache.jfrog.io/artifactory/couchdb-deb/ ${VERSION_CODENAME} main" \
    | sudo tee /etc/apt/sources.list.d/couchdb.list >/dev/null
sudo apt update
sudo apt install -y couchdb
```
We then set up `couchdb` in single-node configuration with the `0.0.0.0` bind
address and created an admin user/password.

### Creating `assignment_one` database

Quinn's time: 0.25 hours

Lessley's time: 0.10 hours

Total time: 0.35 hours

We executed the following command to create the `assignment_one` `couchdb`
database on one Chameleon and one AWS instance:

`curl -X PUT http://admin:<password>@0.0.0.0:5984/assignment_one`

### Opening port 

Quinn's time: 0.25 hours

Lessley's time: 0.10 hours

Total time: 0.35 hours

We opened port 5984 on one Chameleon and one AWS Instance:
#### Chameleon
`sudo ufw allow 5984/tcp`

#### AWS
Added custom firewall rule for inbound traffic on port 5984

`sudo ufw allow 5984/tcp`

### Modifying consumer code

Quinn's time: 1.5 hours

Lessley's time: N/A

Total time: 1.5 hours

Added ability to write to `assignment_1` database via `env.yml` config
in `consumer.py`.

### Mango queries

Quinn's time: N/A

Lessley's time: 0.30 hours

Total time: 0.30 hours

1. In the `couchdb` UI, created a custom index to filter on `group_city`:

``` json
{
 "type": "json",
 "partitioned": false,
 "def": {
  "fields": [
   {
    "group_city": "asc"
   }
  ]
 }
}
```

2. Queried for Seattle and New York documents:

``` yaml
{
   "selector": {
      "group": {
         "group_city": "Seattle" // "New York"
      }
   }
}
```

### Total time expended

The total time expended for this milestone for Quinn and Lessley was
about 3.65 hours.

## Part 3: Video demo

The following is a demonstration of the work completed for this milestone:

https://vanderbilt365-my.sharepoint.com/:v:/g/personal/lessley_c_dennington_vanderbilt_edu/ETP3QSUP42lCgxB4-_j5lQYBhOiX5RgQ8NpzucuZZKHOKA?e=cDWcpU

## Part 4: Running the code

__Pre-Requisites__

Use the same machine you configured for running the Milestone 1 and
Milestone 2 code. See the
[Milestone 1 README](../milestone_1/README.md) for additional
details.

Additionally, use the same producer/consumer setup you created locally
as described in the [Milestone 2 README](../milestone_2/README.md).
Don't forget to modify the `bootstrap_servers` array!

Finally, ensure you have installed `couchdb`, created your database,
and opened port 5984 using the commands detailed above.

__Steps to run__

Update the contents of `env.yml` to the following:

```
couchdb:
    database_host:     localhost
    database_port:     5984
    database_name:     assignment_one
    database_user:     admin
    database_password: password
```

From the `assignment_1/milestone_3/src` directory, run your configured
producer using the appropriate command:

`python3 seattle_producer.py`

`python3 new_york_producer.py`

From a separate terminal, run your modified consumer:

`python3 consumer.py`

Once you register a "hit" in the producer/consumer, in a browser,
navigate to:

localhost:5984/_utils/#database/assignment_one_all_docs

Log in with the credentials specified in `env.yml` and run the
appropriate Mango query specified above to view hits for the producer
you configured.