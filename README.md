
<h1 align="center">DATA SET FOR SOLAR FLARE PREDICTION</h1>

It is known that solar flares can affect the near-Earth space, 
incurring in consequences for radio communications. Therefore, 
there is a need to research systems for monitoring solar events. 
This article presents a data set which can be used in the analysis of such events. 
This data set originated from a set of records from magnetic 
attributes and solar flare data. In order to create this data set, 
authors used the SunPy library which provided access to data from the 
Joint Science Operations Center (JSOC) and Space Weather Prediction Center (SWPC). 
By integrating data from those two sources, 8,874 samples were obtained comprehending 
the period between may, 2010 and December, 2019. The collected data were stored as a CSV data set. 
This data set can be used to support the research of solar flare 
forecasting, as well as to be compared to other data sets or expanded with new attributes.


<a href="https://docs.sunpy.org/en/stable/guide/installation/index.html">🔗 Installing sunpy using Miniconda</a>


```bash

conda config --add channels conda-forge
conda config --set channel_priority strict

conda install sunpy

```
