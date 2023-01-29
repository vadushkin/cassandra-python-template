# Simple template for connecting Python to Cassandra

Instruction
------------

#### Clone repository

```shell
git clone https://github.com/vadushkin/cassandra-python-template.git
```

#### Change directory

```shell
cd cassandra-python-template
```

Run
---

#### Run Cassandra

```docker
docker-compose up -d --build
```

#### Go to the Docker container

```docker
docker exec -it your_name_container bash
```

<details>
  <summary>How to get the container name?</summary>

  <div>
    <h4>Find the last container:</h4>

    docker ps

<h4>Something like that:</h4>
<img src="images/example.png" alt="example"/>
  </div>
<h4>Copy CONTAINER ID: </h4>

    86a1ca...

<h3>The command will be like this:</h3>

    docker exec -it 86a1ca2fcda8 bash

</details>

#### Run Cassandra's shell

```shell
cqlsh
```

#### Create Database

```cassandraql
CREATE KEYSPACE employee WITH replication = {
    'class': 'SimpleStrategy',
    'replication_factor': 2
    };
```

#### Use Database

```cassandraql
USE employee;
```

#### Create Table

```cassandraql
CREATE TABLE employee_details
(
    id   INT,
    age  INT,
    city TEXT,
    name TEXT,
    PRIMARY KEY (id)
);
```

Run Python file
---

#### Create venv

```shell
python -m venv venv
```

#### Activate venv

```shell
.\venv\Scripts\activate
```

#### Update pip

```shell
pip install --upgrade pip
```

#### Install requirements.txt

```shell
pip install -r requirements.txt
```

#### And then Run Python file

```shell
python main.py
```
