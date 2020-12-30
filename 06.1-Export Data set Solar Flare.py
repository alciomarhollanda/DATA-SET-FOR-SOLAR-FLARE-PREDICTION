"""
The purpose of this script is to combine positive and negative events,
make a filter in Quality, SRS and export the data in to the file 
"06.2-DATA SET FOR SOLAR FLARE PREDICTION.csv".
"""
import pandas as pd
import sqlite3
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import numpy as np


conn = sqlite3.connect("HMI_SHARP_SWPC_FINAL.db")

sql = open("06.0-SELECT_JOIN_EVENT_POSITIVE_AND_NEGATIVE.sql").read()


df = pd.read_sql_query(sql, conn)


nameFile = "06.2-DATA SET FOR SOLAR FLARE PREDICTION.csv"


df.to_csv(nameFile, sep=';', index=False, encoding='utf-8')
