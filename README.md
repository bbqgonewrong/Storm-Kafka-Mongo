## Contains working example of storm with kafka spout and mongodb bolts using flux. (Not a wordcount example)

This repo contains implementation for integrating Storm witk kafka and MongoDB.

It is extension of hdinsight-python-storm-wordcount by Azure-samples (https://github.com/Azure-Samples/hdinsight-python-storm-wordcount). However, the extensions are my own.

**Apache Flux** is being used for topology creation and multilang nolt/spout creation

**Topology** consists of a kafka spouta that gets data from kafka server, 2 bolts for processing data i.e one for processing block data and one for processing transaction data, and 2 bolts for dumping these data to mongodb collections.

**How it works:**

1.  `/resources/topology.yaml` - defines what components are in the topology and how data flows between them.
2.  `/multilang/resources` - contains the Python components.

3.  `/pom.xml` - dependencies and how to build the project.

**Steps:**

1.  `mvn clean`
2.  `mvn install`
3.  `mvn clean compile package`
4.  `storm jar target/WordCount-1.0-SNAPSHOT.jar org.apache.storm.flux.Flux -l resources/topology.yaml`

**Main features:**

1.  KafkaSpout: gets data directly from kafka
2.  Uses lates offset to process messages, does not process each msg every time.

**Note:** "-l" argument is meant for testing only, flux destroys the topology after a specific time period. If you want to increase the testing time, pass --sleep argument along the command i.e. pass --sleep 120000 for two minute execution.
Use -r for running topology on cluster after making sure Nimbus and Supervisor are running,.

Will keep updating.
