# Basic Kafka Operations

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