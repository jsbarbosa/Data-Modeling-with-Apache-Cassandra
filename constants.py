KEYSPACE: str = "udacity"

CREATE_KEYSPACE: str = f"""
CREATE KEYSPACE IF NOT EXISTS {KEYSPACE} 
WITH REPLICATION = {{ 'class' : 'SimpleStrategy', 'replication_factor' : 1 }}
"""

CREATE_TABLE_TEMPLATE: str = """
CREATE TABLE IF NOT EXISTS {table}
({fields}, PRIMARY KEY ({primary_keys}))
"""

INSERT_INTO_TEMPLATE: str = """
INSERT INTO {table} ({fields})
VALUES ({values})
"""

DROP_TABLE_TEMPLATE: str = """
DROP TABLE IF EXISTS {table}
"""

DATA_PATH: str = "event_data"

TABLES: dict = {
    'music_app': {
        'table': 'music_app',
        'primary_keys': [
            'sessionId',
            'itemInSession',
            'userId',
            'song'
        ],
        'select_query': "SELECT artist, song, length FROM music_app WHERE sessionId = 338 and itemInSession = 4"
    },
    'music_app1': {
        'table': 'music_app1',
        'primary_keys': [
            'userId',
            'sessionId'
        ],
        'select_query': "SELECT artist, song, length, firstName, lastName FROM music_app1 WHERE userId = 10 and sessionId = 182"
    },
    'music_app2': {
        'table': 'music_app2',
        'primary_keys': [
            'song',
            'userId'
        ],
        'select_query': "SELECT firstName, lastName FROM music_app2 WHERE song = 'All Hands Against His Own' ALLOW FILTERING"
    }
}

TYPES: dict = {
    'text': str,
    'int': int,
    'decimal': float
}

CSV_COLUMNS: list = [
    'artist',
    'firstName',
    'gender',
    'itemInSession',
    'lastName',
    'length',
    'level',
    'location',
    'sessionId',
    'song',
    'userId'
]

CASSANDRA_TABLE_TYPES: list = [
    ('artist', 'text'),
    ('firstName', 'text'),
    ('gender', 'text'),
    ('itemInSession', 'int'),
    ('lastName', 'text'),
    ('length', 'decimal'),
    ('level', 'text'),
    ('location', 'text'),
    ('sessionId', 'int'),
    ('song', 'text'),
    ('userId', 'int')
]

EVENT_DATAFILE: str = "event_datafile_new.csv"
