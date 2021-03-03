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


CASSANDRA_TABLE_TYPES: dict = dict(
    [
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
)

TABLES: list = [
    {
        'table': 'music_heard_in_session',
        'primary_keys': [
            'sessionId',
            'itemInSession',
        ],
        'fields': [
            'sessionId',
            'itemInSession',
            'song',
            'artist',
            'length',
        ],
        'select_query': "SELECT artist, song, length FROM {table} WHERE sessionId = 338 and itemInSession = 4"
    },
    {
        'table': 'user_music_session',
        'primary_keys': [
            '(userId, sessionId)',
            'itemInSession'
        ],
        'fields': [
            'userId',
            'sessionId',
            'itemInSession',
            'artist',
            'song',
            'firstName',
            'lastName'
        ],
        'select_query': "SELECT artist, song, firstName, lastName FROM {table} WHERE userId = 10 and sessionId = 182"
    },
    {
        'table': 'song_listening_activity',
        'primary_keys': [
            'song',
            'userId',
        ],
        'fields': [
            'song',
            'userId',
            'firstName',
            'lastName'
        ],
        'select_query': "SELECT firstName, lastName FROM {table} WHERE song = 'All Hands Against His Own'"
    }
]

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


EVENT_DATAFILE: str = "event_datafile_new.csv"
