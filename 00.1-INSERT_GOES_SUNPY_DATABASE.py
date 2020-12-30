"""
    Script to insert the GOES Event data set information into the database
"""

import pandas as pd
import sqlite3


def ALL_GOES_REPORT():
    conn = sqlite3.connect('HMI_SHARP_SWPC_FINAL.db')

    columnsPandas=["event_date","start_time","peak_time","end_time","goes_class","goes_location","noaa_active_region","classFlare","FlareNumber","Location_1","Location_2"]

    df = pd.read_csv('Data set\\00_All_GOES_SUNPY.csv',sep=";", index_col=False, names=columnsPandas)

    print(df)

    df.to_sql('00_GOES_SUNPY', conn, if_exists='replace', index=False)


# Start Pythoon
ALL_GOES_REPORT()
