# Basic Kafka Operations

Kafka is a distributed event streaming platform designed for handling real-time data feeds. It acts as a distributed commit log where data is organized into topics, which are partitioned and replicated across a cluster of servers (brokers). Producers publish records (messages) to topics, and consumers subscribe to topics to consume these records. ZooKeeper is a centralized service for maintaining configuration information, providing distributed synchronization, and handling various distributed operations in a distributed system.

## Installation
1. [Install](https://www.linuxtechi.com/how-to-install-apache-kafka-on-ubuntu) apache Kafka and ZooKeeper 
2. [Install](https://cloudinfrastructureservices.co.uk/install-apache-kafka-on-ubuntu-20-04-cluster) Kafka Cluster Manager

## Steps
1. Start Zookeeper ```sudo systemctl start zookeeper```
2. Start Kafka ```sudo systemctl start kafka```
3. Checking running status
```
sudo systemctl status zookeeper 
sudo systemctl status kafka
```
4. Run Cluster Manager for Apache Kafka 
```
cd ~/CMAK/target/universal
unzip cmak-3.0.0.5.zip
cd cmak-3.0.0.5
bin/cmak
```
5. Create cluster and topic from Cluster Manager
6. Run Producer ```python producer.py```
7. Run Consumer ```python consumer.py```