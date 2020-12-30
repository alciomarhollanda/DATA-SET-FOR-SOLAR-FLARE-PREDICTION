"""
Script to filter the most intense solar flares that happened in one day. 
It is worth mentioning that an active region burning more than one event in a day, 
leads us to count them as several distinct positive events.
"""
import pandas as pd
import sqlite3
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import numpy as np


def getsqlFlareAr(dateDay):
  # Pega o maior evento
    sql = """
    select 
    MAX(FlareNumber) as FlareNumber ,
    noaa_active_region 
    from [00_GOES_SUNPY] where start_time like '{0}%' and noaa_active_region > 10000
    GROUP BY noaa_active_region
    """.format(dateDay)

    return sql


conn = sqlite3.connect("HMI_SHARP_SWPC_FINAL.db")

startDate = datetime.strptime('2010-05-01', "%Y-%m-%d")

while startDate.year <= 2019:
    startDateString = startDate.strftime("%Y-%m-%d")
    startDate = startDate+relativedelta(days=+1)
    endDateString = startDate.strftime("%Y-%m-%d")

    dateString = "Time: {0} ||  {1} - {2}".format(
        datetime.now(), startDateString, endDateString)

    print(dateString)

    sql = getsqlFlareAr(startDateString)

    df = pd.read_sql_query(sql, conn)

    dataFrameEventFilter = pd.DataFrame()

    for index, event in df.T.iteritems():

        sqlSunPy = """
        select 
        * 
        from [00_GOES_SUNPY] 
        where 
        noaa_active_region = {0} and start_time like '{1}%' and FlareNumber = {2} 
        
        """.format(event.noaa_active_region, startDateString, event.FlareNumber)

        df2 = pd.read_sql_query(sqlSunPy, conn)
        dataFrameEventFilter = dataFrameEventFilter.append(df2)

    print(dataFrameEventFilter)

    dataFrameEventFilter.to_sql(
        '03_FILTER_GOES_EVENT_MULT_MAX_BY_AR', conn, if_exists='append', index=False)
