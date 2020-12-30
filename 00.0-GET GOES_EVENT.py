"""
Script to get the information for the GOES Event data set
"""

import pandas as pd
from sunpy.time import TimeRange
from sunpy.instr.goes import get_goes_event_list
from datetime import date, datetime
from dateutil.relativedelta import relativedelta
import re

import sqlite3


def flag_df(df):
    if(df['classFlare'] == 'A'):
        return 0
    elif(df['classFlare'] == 'B'):
        return 1
    elif(df['classFlare'] == 'C'):
        return 2
    elif(df['classFlare'] == 'M'):
        return 3
    elif(df['classFlare'] == 'X'):
        return 4


def get_goes_event_list_sunpy():
    startDate = datetime.strptime('2010.05.01 00:00:00', "%Y.%m.%d %H:%M:%S")

    while startDate.year < 2020:
        startDateString = startDate.strftime('%Y/%m/%d %H:%M')
        startDate = startDate+relativedelta(months=+1)
        endDateString = startDate.strftime('%Y/%m/%d %H:%M')

        print(startDateString+' - '+endDateString)

        time_range = TimeRange(startDateString, endDateString)

        goes_list = get_goes_event_list(time_range)

        df = pd.DataFrame(data=goes_list)

        df['start_time'] = pd.to_datetime(
            df['start_time'], format='%Y-%m-%dT%H:%M:00.000')

        df['peak_time'] = pd.to_datetime(
            df['peak_time'], format='%Y-%m-%dT%H:%M:00.000')

        df['end_time'] = pd.to_datetime(
            df['end_time'], format='%Y-%m-%dT%H:%M:00.000')

        # get only classification
        df['classFlare'] = df['goes_class'].apply(lambda x: x[:1])

        # use fuction to convert text in number class
        df['FlareNumber'] = df.apply(flag_df, axis=1)

        df[['goes_location_fist', 'goes_location_segund']] = pd.DataFrame(
            df['goes_location'].tolist(), index=df.index)

        
        nameFile = "Data set\\00_All_GOES_SUNPY.csv"
        df.to_csv(nameFile, sep=';', encoding='utf-8',
                header=False, index=False, mode='a')



get_goes_event_list_sunpy()
