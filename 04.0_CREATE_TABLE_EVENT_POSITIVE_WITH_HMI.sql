/**
  It is necessary to execute this SQL to create a table in the bank to execute the script 
  “04.1-INSERT_EVENT_POSITIVE_WITH_HMI.py”. 
  This table will store the magnetic data for positive events.  
**/

CREATE TABLE "04_EVENT_POSITIVE_WITH_HMI" (
    event_date         TEXT,
    start_time         TEXT,
    peak_time          TEXT,
    end_time           TEXT,
    goes_class         TEXT,
    goes_location      TEXT,
    noaa_active_region INTEGER,
    classFlare         TEXT,
    FlareNumber        INTEGER,
    Location_1         INTEGER,
    Location_2         INTEGER,
    T_REC              TIMESTAMP,
    HARPNUM            INTEGER,
    TOTUSJH            REAL,
    TOTPOT             REAL,
    TOTUSJZ            REAL,
    ABSNJZH            REAL,
    SAVNCPP            REAL,
    USFLUX             REAL,
    AREA_ACR           REAL,
    MEANPOT            REAL,
    R_VALUE            REAL,
    SHRGT45            REAL,
    NOAA_AR            INTEGER,
    NOAA_NUM           INTEGER,
    NOAA_ARS           TEXT,
    QUALITY            INTEGER
);
