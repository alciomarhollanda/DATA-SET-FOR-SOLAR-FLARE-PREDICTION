"""
To execute this script it is necessary to execute the SQL 
“05.0_CREATE_TABLE_EVENT_NEGATIVE_WITH_HMI.sql” in the database beforehand. 
This script will acquire the magnetic data for the negative events.
"""
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
import sqlite3


def getSQL_NUM_NOAA(startDate, endDate):
    sql = """
SELECT
noaa_active_region
FROM [00_GOES_SUNPY] where event_date between "{0}" AND "{1}" and FlareNumber >=3 and noaa_active_region > 10000
group by noaa_active_region
""".format(startDate, endDate)

    return sql


def getSQL_NOT_FLARE(startDateString, endDateString, rows):

    l = [0]
    for row in rows:
        if row[0] is not None:
            l.append(row[0])

    sql = """
    INSERT INTO [05_EVENT_NEGATIVE_WITH_HMI] (
    startDate,
    endDate,
    T_REC,
    HARPNUM,
    TOTUSJH,
    TOTPOT,
    TOTUSJZ,
    ABSNJZH,
    SAVNCPP,
    USFLUX,
    AREA_ACR,
    MEANPOT,
    R_VALUE,
    SHRGT45,
    NOAA_AR,
    NOAA_NUM,
    NOAA_ARS,
    QUALITY
    )

    select 
    MAX(t.T_REC) as startDate, 
    "{1}" as endDate, 
    t.*
    from [02_HMI_SHARP] AS t 
    where t.T_REC LIKE "{0}%" AND TOTUSJH !=0
    """.format(startDateString, endDateString)

    myquery = sql + " AND NOAA_AR NOT IN (%s)" % ",".join(
        map(str, l))

    myquery = myquery + " GROUP BY NOAA_AR ;"
    return myquery


def getNotFlare():

    startDate = datetime.strptime('2010-05-01 00:00:00', "%Y-%m-%d %H:%M:%S")

    sqliteConnection = sqlite3.connect('HMI_SHARP_SWPC_FINAL.db')
    cursor = sqliteConnection.cursor()

    while startDate.year <= 2019:
        startDateString = startDate.strftime("%Y-%m-%d")
        startDate = startDate+relativedelta(days=+1)

        endDateString = startDate.strftime("%Y-%m-%d")

        dateString = "Time: {0} ||  {1} - {2}".format(
            datetime.now(), startDateString, endDateString)

        print(dateString)

        sql = getSQL_NUM_NOAA(startDateString, endDateString)

        cursor.execute(sql)

        rows = cursor.fetchall()

        myquery = getSQL_NOT_FLARE(startDateString, endDateString, rows)

        cursor.execute(myquery)

        cursor.fetchall()

        sqliteConnection.commit()

        print("Record inserted successfully into HMI_SHARP_SWPC table {0}".format(
            cursor.rowcount))

    cursor.close()


getNotFlare()


# https://stackoverflow.com/questions/283645/python-list-in-sql-query-as-parameter
