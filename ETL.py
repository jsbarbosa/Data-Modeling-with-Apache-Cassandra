import pandas as pd
from cassandra.cluster import Cluster
from constants import INSERT_INTO_TEMPLATE, TABLES, KEYSPACE

# To establish connection and begin executing queries, need a session
cluster = Cluster()
session = cluster.connect(
    keyspace=KEYSPACE
)

# read data from csv
csv_data = pd.read_csv('event_datafile_new.csv')

for table in TABLES:
    query = INSERT_INTO_TEMPLATE.format(
        table=table['table'],
        fields=", ".join(table['fields']),
        values=", ".join(["%s"] * len(table['fields']))
    )

    for _, row in csv_data.iterrows():
        session.execute(
            query,
            [row[field] for field in table['fields']]
        )

    rows = session.execute(table['select_query'].format(
        table=table['table'])
    )
    for row in rows:
        print(row)
    print()

session.shutdown()
cluster.shutdown()
