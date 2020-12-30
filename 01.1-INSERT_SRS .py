"""
Script to insert the SRS data set information into the database
"""
import pandas as pd
import sqlite3
import numpy as np


def ALL_GOES_REPORT():
    conn = sqlite3.connect('HMI_SHARP_SWPC_FINAL.db')

    columnsPandas=["ID","Number","Carrington_Longitude","Area","Z","Longitudinal_Extent","Number_of_Sunspots","Mag_Type","Latitude","Longitude","issued"]

    df = pd.read_csv('Data set\\01-ALL_SRS.csv',sep=";", index_col=False, names=columnsPandas)
    
    
    df = df.replace(to_replace ="--", value ="0")

    # df['Latitude'] = df['Latitude'].map(lambda x: x.lstrip('+-').rstrip(' deg'))
    # df['Longitude'] = df['Longitude'].map(lambda x: x.lstrip('+-').rstrip(' deg'))

    print(df)

    df.to_sql('01_GOES_SRS', conn, if_exists='replace', index=False)





# Start Pythoon
ALL_GOES_REPORT()
