# Assignment 2 Milestone 1

__Team 4: Quinn Pommerening and Lessley Dennington__

## Part 1: Teamwork

__Quinn Pommerening__


__Lessley Dennington__

* Installed vagrant on local machine
* Configured Vagrantfile to:
    1. Provision Ubuntu 20.04 Focal Fossa machine on VirtualBox
    2. Copy needed files from host machine to vagrant-provisioned
       machine
    3. Provision/configure ansible on the vagrant-provisioned machine
* 

## Part 2: Effort expended

In order to complete this milestone, we did the following:

### Installing/configuring `couchdb`

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

We executed the following command to create the `assignment_one` `couchdb`
database on one Chameleon and one AWS instance:

`curl -X PUT http://admin:<password>@0.0.0.0:5984/assignment_one`

### Opening port 

We opened port 5984 on one Chameleon and one AWS Instance:
#### Chameleon
`sudo ufw allow 5984/tcp`

#### AWS
Added custom firewall rule for inbound traffic on port 5984

`sudo ufw allow 5984/tcp`

### Mango queries

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

## Part 3: Video demo

The following is a demonstration of the work completed for this milestone:

