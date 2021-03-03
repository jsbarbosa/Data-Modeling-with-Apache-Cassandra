import os
import pandas as pd
from glob import glob

from constants import DATA_PATH, CSV_COLUMNS, TYPES, CASSANDRA_TABLE_TYPES, EVENT_DATAFILE

# get path to the files in event_data sorted
file_path_list = sorted(
    glob(
        os.path.join(
            DATA_PATH,
            '*.csv'
        )
    )
)

# build single dataframe containing all rows of all files. Ignore those with empty artist
# Only relevant columns are kept. Futhermore, types are enforced.
full_data = pd.concat(
    [
        pd.read_csv(path) for path in file_path_list
    ]
).dropna(
    subset=['artist']
)[CSV_COLUMNS].astype(
    {
        col: TYPES[col_type] for col, col_type in CASSANDRA_TABLE_TYPES.items()
    }
)

# save to csv
full_data.to_csv(
    EVENT_DATAFILE,
    index=False
)
