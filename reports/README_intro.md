# Opportunity Youth in South King County.
##### An analysis by Leana Critchell, Dann Morr and Johnhoy Stephens

## Aims:
The aims of our analysis are three-fold:

1. To generate an updated estimate on the number of Opportunity Youth in South King County 

2. To gain a deeper understanding of the two defining characteristics of Opportunity Youth:  education and employment.

3. To observe any trends between the 2016 "Opportunity Youth in the Road Map Project Region" report and the data we are reporting on from 2017.

## Definitions:
### Opportunity Youth:
The Opportunity Youth population is defined as persons aged between 16 and 24 who are not in school and are not working.  Throughout this analysis, you may see Opportunity Youth referred to as 'OY'.

We define anyone who is either working or participating in school as Non-Opportunity Youth.

### South King County:
For the purposes of this report, South King County has been defined using the PUMA codes as per the data from the ACS website.  After refining the data from the `puma_names_2010` table down to King County, the regions which identified 'South' in their puma name was assumed to be apart of South King County.  Thus, the PUMA codes we used to define our data set were:  11612, 11613, 11614, 11615

### Notes about the Data:  
- Throughout this analysis, comparisons are sometimes drawn between this report and the 2016 report on Opportunity Youth.  It is important to note that the way the data was defined for the 2016 report differs from how we have defined our data.  The 2016 report includes some data from the wider King County area whereas we have stayed strictly within the four aforementioned PUMA codes.
- The 2016 report uses data from the 2014 PUMS data (collected in the 2010 census).
- Our 2020 report utilises data from the 2017 PUMS data, as provided by the ACS website.
- The 2017 PUMS data represents a sample of the population.  The ACS included person weightings to allow for appropriate scaling.  Numbers quoted in relation to population counts throughout the analysis are based on the person weights. 

## Overview:
This analysis was completed in four stages:
1. A map was generated to help visualise the part of King County that are a part of South King County.

2. An updated estimate of the number of Opportunity Youth in South King County as well as a breakdown of this count by age group, PUMA code, educational attainment and employment availability.  

3. An update of the table "Opportunity Youth Status by Age" from the 2016 report "Opportunity Youth in the Road Map Project Region".

4. A visualisation highlighting a trend between the 2014 data and the current 2017 data.

## Directory of Repo:

```
├── notebooks
│   ├── exploratory
│   └── report
├── references
├── reports
│   └── figures
├── src
│   ├── data
│   │   ├── sql
│   ├── data_cleaning
│   └── requirements
```

