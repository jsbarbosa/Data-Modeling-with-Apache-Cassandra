import pandas as pd
from cassandra.cluster import Cluster
from constants import INSERT_INTO_TEMPLATE, TABLES, KEYSPACE, CASSANDRA_TABLE_TYPES

# To establish connection and begin executing queries, need a session
cluster = Cluster()
session = cluster.connect(
    keyspace=KEYSPACE
)

# read data from csv
csv_data = pd.read_csv('event_datafile_new.csv')

for table in TABLES.values():
    query = INSERT_INTO_TEMPLATE.format(
        table=table['table'],
        fields=", ".join([col for col, _ in CASSANDRA_TABLE_TYPES]),
        values=", ".join(["%s" for item in CASSANDRA_TABLE_TYPES])
    )

    for _, row in csv_data.iterrows():
        session.execute(query, list(row.values))

    rows = session.execute(table['select_query'])
    for row in rows:
        print(row)
    print()

session.shutdown()
cluster.shutdown()