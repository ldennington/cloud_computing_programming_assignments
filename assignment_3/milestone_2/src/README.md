## Docker Zookeeper: 
    docker-compose -f zookeeper-compose.yml up -d

## Docker Kafka:
    Will need to change IP Address for commands
    docker-compose -f kafka-compose.yml up -d && docker run --rm ches/kafka kafka-topics.sh --create --topic MeetUpNewYork --replication-factor 1 --partitions 1 --zookeeper 3.80.96.186:2181 && docker run --rm ches/kafka kafka-topics.sh --create  --topic MeetUpSeattle --replication-factor 1 --partitions 1 --zookeeper 3.80.96.186:2181

## Docker CouchDB: 
    docker-compose -f couchdb-compose.yml up -d && docker exec couchdb curl -X PUT http://admin:password@127.0.0.1:5984/assignment_three

## Docker Consumer: 
    docker build -f consumer-compose -t consumer . && docker run -id consumer