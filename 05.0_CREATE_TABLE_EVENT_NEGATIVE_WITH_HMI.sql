/**
 It is necessary to execute this SQL to create a table in the bank to execute the script 
  “05.1-INSERT_EVENT_NEGATIVE_WITH_HMI.py”. 
  This table will store the magnetic data for negative events.  
**/
CREATE TABLE "05_EVENT_NEGATIVE_WITH_HMI" (
    startDate TIMESTAMP,
    endDate   TIMESTAMP,
    T_REC     TIMESTAMP,
    HARPNUM   INTEGER,
    TOTUSJH   REAL,
    TOTPOT    REAL,
    TOTUSJZ   REAL,
    ABSNJZH   REAL,
    SAVNCPP   REAL,
    USFLUX    REAL,
    AREA_ACR  REAL,
    MEANPOT   REAL,
    R_VALUE   REAL,
    SHRGT45   REAL,
    MEANSHR   REAL,
    MEANGAM   REAL,
    MEANGBT   REAL,
    MEANGBZ   REAL,
    MEANGBH   REAL,
    MEANJZH   REAL,
    MEANJZD   REAL,
    MEANALP   REAL,
    NOAA_AR   INTEGER,
    NOAA_NUM  INTEGER,
    NOAA_ARS  TEXT,
    QUALITY   INTEGER
);
