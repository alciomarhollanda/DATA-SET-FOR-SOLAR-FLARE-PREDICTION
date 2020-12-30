"""
Script to get the information for the SRS data set
"""

from datetime import date, datetime
from sunpy.net import Fido, attrs as a
from sunpy.io.special import srs
from sunpy.time import parse_time
from dateutil.relativedelta import relativedelta
import pandas as pd
import os
import re

import sqlite3


def joinFileSRS(fileName):
    try:
        print(fileName)
        srs_table = srs.read_srs(fileName)
        # print(srs_table)
        # print(srs_table.colnames)
        print(srs_table.meta['issued'].date())
        outF = open("Data set\\01-ALL_SRS.csv", "a")
        for x in srs_table:


            LatitudeNumber = re.search("\d+", str(x['Latitude']))
            LongitudeNumber = re.search("\d+", str(x['Longitude']))

            stringX = "{0};{1};{2};{3};{4};{5};{6};{7};{8};{9};{10}\n".format(
                x['ID'],
                x['Number'],
                x['Carrington Longitude'],
                x['Area'],
                x['Z'],
                x['Longitudinal Extent'],
                x['Number of Sunspots'],
                x['Mag Type'],
                LatitudeNumber.group(0) if LatitudeNumber else 0,
                LongitudeNumber.group(0) if LongitudeNumber else 0,
                srs_table.meta['issued'].date()
            )
            # print(stringX)
            outF.write(stringX)

        outF.close()


    except KeyError as err:
        print("KeyError: {0}".format(err))


if __name__ == "__main__":
    # os.remove('03-ALL_SRS.csv')
    for root, dirs, files in os.walk("SRS\\", topdown=False):
        for name in files:
            if(name.endswith('.txt')):               
                joinFileSRS(os.path.join(root, name))
    

