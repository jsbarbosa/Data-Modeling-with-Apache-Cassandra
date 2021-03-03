from cassandra.cluster import Cluster
from constants import CREATE_KEYSPACE, CREATE_TABLE_TEMPLATE, KEYSPACE,\
    DROP_TABLE_TEMPLATE, TABLES, CASSANDRA_TABLE_TYPES

# To establish connection and begin executing queries, need a session
cluster = Cluster()
session = cluster.connect()

# create keyspace
session.execute(CREATE_KEYSPACE)

# set keyspace
session.set_keyspace(KEYSPACE)

# build column names and types for CREATE TABLE query
for table in TABLES:
    # drop table if exist
    session.execute(
        DROP_TABLE_TEMPLATE.format(
            table=table['table']
        )
    )

    # build primary keys string
    primary_keys = ", ".join(table['primary_keys'])
    fields = ", ".join(
        [
            f"{field} {CASSANDRA_TABLE_TYPES[field]}"
            for field in table['fields']
        ]
    )
    # create table
    session.execute(
        CREATE_TABLE_TEMPLATE.format(
            table=table['table'],
            fields=fields,
            primary_keys=primary_keys
        )
    )

session.shutdown()
cluster.shutdown()

