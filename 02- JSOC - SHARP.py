"""
Script to get and insert the SHARP data set information into the database
"""
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import drms
import pandas as pd
import sqlite3


def get_Hmi_sharp():
    c = drms.Client()
    startDate = datetime.strptime('2010.05.01 00:00:00', "%Y.%m.%d %H:%M:%S")

    while startDate.year < 2020:
        startDateString = startDate.strftime('%Y.%m.%d_%H:%M:%S')
        startDate = startDate+relativedelta(weeks=+1)
        endDateString = startDate.strftime('%Y.%m.%d_%H:%M:%S')

        dateString = startDateString+'-'+endDateString
        print(dateString)

        variable = 'T_REC,HARPNUM,TOTUSJH,TOTPOT,TOTUSJZ,ABSNJZH,SAVNCPP,USFLUX,AREA_ACR,MEANPOT,R_VALUE,SHRGT45,NOAA_AR,NOAA_NUM,NOAA_ARS,QUALITY'
        df = c.query('hmi.sharp_720s[]['+dateString+']', key=variable)

        if(df.size == 0):
            continue
        df.T_REC = drms.to_datetime(df.T_REC)

        conn = sqlite3.connect('HMI_SHARP_SWPC_FINAL.db')
        df.to_sql('02_HMI_SHARP', conn, if_exists='append', index=False)
        #nameFile = "All_hmi.sharp_720s.csv"
        #df.to_csv(nameFile, sep=';', encoding='utf-8', header=false,index=False, mode='a')


def get_cgemLorentz():
    c = drms.Client()
    startDate = datetime.strptime('2010.05.01 00:00:00', "%Y.%m.%d %H:%M:%S")

    while startDate.year < 2020:
        startDateString = startDate.strftime('%Y.%m.%d_%H:%M:%S')
        startDate = startDate+relativedelta(weeks=+1)
        endDateString = startDate.strftime('%Y.%m.%d_%H:%M:%S')

        dateString = startDateString+'-'+endDateString
        print(dateString)

        variable = 'HARPNUM, T_REC, TOTFZ, TOTBSQ, EPSZ, QUALITY, NOAA_ARS, NOAA_AR, NOAA_NUM'
        df = c.query('cgem.lorentz[]['+dateString+']', key=variable)

        if(df.size == 0):
            continue

        df.T_REC = drms.to_datetime(df.T_REC)

        conn = sqlite3.connect('HMI_SHARP_SWPC_FINAL.db')
        df.to_sql('02_CGEM_LORENTZ', conn, if_exists='append', index=False)
        #nameFile = "All_hmi.sharp_720s.csv"
        #df.to_csv(nameFile, sep=';', encoding='utf-8', header=false,index=False, mode='a')

# start


get_Hmi_sharp()

get_cgemLorentz()
