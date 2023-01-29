"""Commands:
$ `docker run --name test-cassandra-v2 -p 9042:9042 -d cassandra:latest` or `docker-compose up -d --build`
$ `docker exec -it test-cassandra-v2 bash`
$ `cqlsh`
$ `CREATE KEYSPACE employee WITH replication = {'class' : 'SimpleStrategy', 'replication_factor':2};`
$ `USE employee;`
$ `CREATE TABLE employee_details (id INT, age INT, city TEXT, name TEXT, PRIMARY KEY(id));`
# end then run this python file
"""
from cassandra.cluster import Cluster

# connect to cluster
cluster = Cluster(['0.0.0.0'], port=9042)  # port in docker file or in docker run ... -p `(9042):9042` ...
# before that we need to create keyspace in cassandra (line 5)
session = cluster.connect('employee')

# Writing data into cassandra
session.execute("INSERT INTO employee_details (id, age, city, name) VALUES (99, 20, 'Chicago', 'Max');")
session.execute_async("INSERT INTO employee_details (id, age, city, name) VALUES (400, 25, 'Seattle', 'Bob');")

# Reading Data From Cassandra [simple query]
print("Reading data simply: \n")
rows = session.execute('SELECT * FROM employee_details;')

for e, employee_row in enumerate(rows, start=1):
    print(f"{e}. {employee_row}")
    print(f'Meet {employee_row.name}! He lives in {employee_row.city}.\n')

# ? is your employee_id (line 37)
prepared_statement = session.prepare('SELECT * FROM employee_details WHERE id=?')
# ids for query
employees_to_lookup = [99, 400]

print("\nReading data using prepared statements: \n")

for e, employee_id in enumerate(employees_to_lookup, start=1):
    # give one row from employee_details with employee_id
    employee = session.execute(prepared_statement, [employee_id]).one()

    print(f"{e}. {employee}")
