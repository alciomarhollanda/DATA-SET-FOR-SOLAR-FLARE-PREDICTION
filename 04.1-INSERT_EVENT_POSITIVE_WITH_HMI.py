"""
To execute this script it is necessary to execute the SQL 
“04.0_CREATE_TABLE_EVENT_POSITIVE_WITH_HMI.sql” in the database beforehand. 
This script will acquire the magnetic data for the positive events.
"""
from datetime import date, datetime
from dateutil.relativedelta import relativedelta

import pandas as pd
import sqlite3


def getSQL(startDate, endDate):
    sql = """
INSERT INTO [04_EVENT_POSITIVE_WITH_HMI] (
  event_date,
  start_time,
  peak_time,
  end_time,
  goes_class,
  goes_location,
  noaa_active_region,
  classFlare,
  FlareNumber,
  Location_1,
  Location_2,
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
  MEANSHR,
  MEANGAM,
  MEANGBT,
  MEANGBZ,
  MEANGBH,
  MEANJZH,
  MEANJZD,
  MEANALP,
  NOAA_AR,
  NOAA_NUM,
  NOAA_ARS,
  QUALITY
)
SELECT
GS.*,
HMI.*
from [03_FILTER_GOES_EVENT_MULT_MAX_BY_AR] AS GS
INNER JOIN [02_HMI_SHARP] AS HMI ON HMI.ROWID = 
(
SELECT 
ROWID FROM [02_HMI_SHARP] AS HMI_SUB 
WHERE 
HMI_SUB.T_REC BETWEEN DATETIME(GS.start_time,'-2 day','start of day') AND DATETIME(GS.start_time,'-1 day') 
AND HMI_SUB.NOAA_AR = GS.noaa_active_region 
--AND HMI_SUB.QUALITY <=65536
ORDER BY T_REC DESC LIMIT 1
)
where GS.start_time BETWEEN "{0}" AND "{1}" and GS.FlareNumber >=3
""".format(startDate, endDate)

    return sql


def get_Hmi_sharp():

    startDate = datetime.strptime('2010-05-01 00:00:00', "%Y-%m-%d %H:%M:%S")

    sqliteConnection = sqlite3.connect('HMI_SHARP_SWPC_FINAL.db')
    cursor = sqliteConnection.cursor()

    while startDate.year <= 2019:
        startDateString = startDate.strftime("%Y-%m-%d %H:%M:%S")
        startDate = startDate+relativedelta(weeks=+1)
        endDateString = startDate.strftime("%Y-%m-%d %H:%M:%S")

        dateString = "Time: {0} ||  {1} - {2}".format(
            datetime.now(), startDateString, endDateString)

        print(dateString)

        sql = getSQL(startDateString, endDateString)

        cursor.execute(sql)

        sqliteConnection.commit()

        print("Record inserted successfully into HMI_SHARP_SWPC table {0}".format(
            cursor.rowcount))

    cursor.close()


get_Hmi_sharp()
