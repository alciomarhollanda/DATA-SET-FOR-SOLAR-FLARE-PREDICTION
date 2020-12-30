/**
This SQL will be executed by the Script "06.1-Export Data set Solar Flare.py".

**/
SELECT  
       1 as FlareNumber,
       HMI.T_REC,
       HMI.NOAA_AR,
       HMI.QUALITY,
       SRS.Longitude,
       HMI.TOTUSJH,
       CL.TOTBSQ,
       HMI.TOTPOT,
       HMI.TOTUSJZ,
       HMI.ABSNJZH,
       HMI.SAVNCPP,
       HMI.USFLUX,
       HMI.AREA_ACR,
       CL.TOTFZ,
       HMI.MEANPOT,
       HMI.R_VALUE,
       CL.EPSZ,
       HMI.SHRGT45
FROM [04_EVENT_POSITIVE_WITH_HMI] AS HMI
INNER JOIN [02_CGEM_LORENTZ] AS CL ON CL.T_REC = HMI.T_REC AND CL.HARPNUM = HMI.HARPNUM and CL.NOAA_AR = HMI.NOAA_AR
INNER JOIN [01_GOES_SRS] AS SRS ON SRS.issued = date(HMI.start_time) and SRS.Number = HMI.noaa_active_region

WHERE  
    CL.QUALITY <=65536 
    AND SRS.Longitude >= -70 AND SRS.Longitude <=70
    AND (CL.TOTBSQ AND CL.TOTFZ AND CL.EPSZ) NOT NULL 
    AND HMI.FlareNumber >=3
    AND HMI.T_REC !='2012-06-12 23:12:00'

GROUP BY HMI.start_time

------------------------------------- END FIRST SQL --------------------------------------------
UNION

SELECT 
       0 as FlareNumber,
       HMI.T_REC,
       HMI.NOAA_AR,
       HMI.QUALITY,
       SRS.Longitude,
       HMI.TOTUSJH,
       CL.TOTBSQ,
       HMI.TOTPOT,
       HMI.TOTUSJZ,
       HMI.ABSNJZH,
       HMI.SAVNCPP,
       HMI.USFLUX,
       HMI.AREA_ACR,
       CL.TOTFZ,
       HMI.MEANPOT,
       HMI.R_VALUE,
       CL.EPSZ,
       HMI.SHRGT45
       
FROM [05_EVENT_NEGATIVE_WITH_HMI]  AS HMI
    INNER JOIN [02_CGEM_LORENTZ] AS CL ON CL.T_REC = HMI.T_REC AND CL.HARPNUM = HMI.HARPNUM and CL.NOAA_AR = HMI.NOAA_AR
    INNER JOIN [01_GOES_SRS] AS SRS ON SRS.issued = date(HMI.T_REC) and SRS.Number = HMI.NOAA_AR

WHERE  CL.QUALITY <=65536 AND HMI.QUALITY <=65536
    AND SRS.Longitude >= -70 AND SRS.Longitude <=70
    AND (CL.TOTBSQ AND CL.TOTFZ AND CL.EPSZ) NOT NULL 
    AND HMI.TOTUSJH != 0

GROUP BY  
strftime('%Y-%m-%d',HMI.T_REC) , HMI.HARPNUM
