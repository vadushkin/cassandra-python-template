# Simple template for connecting Python to Cassandra

Instruction
------------


```main.py```

```python
"""
Commands:

* docker run --name test-cassandra-v2 -p 9042:9042 -d cassandra:latest or docker-compose up -d --build
* docker exec -it test-cassandra-v2 bash
* cqlsh
* CREATE KEYSPACE employee WITH replication = {'class' : 'SimpleStrategy', 'replication_factor':2};
* USE employee;
* CREATE TABLE employee_details (id INT, age INT, city TEXT, name TEXT, PRIMARY KEY(id));

# and then run this python file
"""
from cassandra.cluster import Cluster

...
```

Run
---

#### Run Cassandra

```docker
docker-compose up -d --build
```

#### Go to the Docker container

```docker
docker exec -it test-cassandra-v2 bash
```

#### Run Cassandra's shell

```shell
cqlsh
```

#### Create Database

```cassandraql
CREATE KEYSPACE employee WITH replication = {
    'class' : 'SimpleStrategy', 
    'replication_factor':2
};
```

#### Use Database

```cassandraql
USE employee;
```

#### Create Table

```cassandraql
CREATE TABLE employee_details (
    id INT, 
    age INT, 
    city TEXT, 
    name TEXT, 
    PRIMARY KEY(id)
);
```

#### And then Run Python file

```shell
python main.py
```