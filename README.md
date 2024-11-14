# Implementing Change Data Capture (CDC) with Kafka Connect and Apache Kafka on Kubernetes

This repository contains the code and configuration files used in the Medium article: [Implementing Change Data Capture (CDC) with Kafka Connect and Apache Kafka on Kubernetes: A Complete Guide for Data Engineers](https://matheusjerico.medium.com/implementing-change-data-capture-cdc-with-kafka-connect-and-apache-kafka-on-kubernetes-a-d3c5ca2fa6d7).

Please refer to the article for a complete guide and detailed instructions on setting up CDC with Kafka Connect and Kafka on Kubernetes.

# Folder structure

The repository is organized as follows:
```
.
├── api
│   ├── Dockerfile
│   ├── fastapi-deployment.yaml
│   └── main.py
├── data-platform.yaml
├── kafka
│   ├── image
│   │   ├── debezium-connector-mysql-2.7.3.Final-plugin.tar.gz
│   │   ├── Dockerfile
│   │   └── plugins
│   │       └── debezium-connector-mysql
│   ├── kafka-cluster.yaml
│   ├── mysql-kafka-connector.yaml
│   └── mysql-kafka-connect.yaml
├── mysql
│   └── mysql-values.yaml
└── README.md
```

# Contributing
Feel free to open issues or submit pull requests for improvements.

# License
This project is licensed under the MIT License.