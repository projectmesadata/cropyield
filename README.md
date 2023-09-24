# Crop Yield Data Pipeline

This repository uses the Famine Land Data Assimilation System (FLDAS)* operated by the U.S. National Air and Space Administration. This data can then be used to explore the water status and related soil condition in a given area over time as an indicator of crop yields.

This repository has three main files: 

* Crop Yield Data Download Interactive (must be run first)
* Crop Yield Location Interactive
* Crop Yield Regional Interactive (best for ABMs)

In an effort to make them more user friendly so users can focus on either exploring the data or rapidly integrating the data outputs into ABMs each of these files is skill scalable, where they can be run with only inputs and no code or where users can explore and manipulate the code themselves. This is why each files has an interactive designation. 

A quick overview of each file is below.  

## Crop Yield Data Download 
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/projectmesadata/cropyield/HEAD?urlpath=%2Flab%2FCrop%20Yield%20-%20Data%20Download%20(must%20run%20first)-Interactive.ipynb)


This file retrieves the data. You will need to complete the following two steps to get to the data.    

1. An Earthdata username and password are required to run this program 

>["How to" get an EarthData account](https://wiki.earthdata.nasa.gov/display/EL/How+To+Register+For+an+EarthData+Login+Profile)

2. You must also activate data access **Failure to do this will give you an error in the other scripts**

>["How To" activate the archive download](https://disc.gsfc.nasa.gov/earthdata-login)

***

\* [More information about FLDAS](https://ldas.gsfc.nasa.gov/FLDAS/) 

## Crop Yield Location  
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/projectmesadata/cropyield/HEAD?urlpath=%2Flab%2FCrop%20Yield%20Location%20Interactive.ipynb)

This  file takes the downloaded data and allows the user to select a location within the desired area. From this data the scripts creates plots of that locations water satisfaction requirement index (WSRI) and allows the users to select different crop types based on the United Nations Food and Agricultural handbook to assess the maximal yields. It is important to point out that the algorithms used (described in more detail in the file) can only provide the maximal crop yields and does not account for sub-optimal farming techniques or socio-economic dynamics.

## Crop Yield Regional
[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/projectmesadata/cropyield/HEAD?urlpath=%2Flab%2FCrop%20Yield%20Regional%20Interactive.ipynb)

This files allows the user to either narrow the region of interest or see the whole region and get the WRSI for each latitude and longitude (as well as web Mercator coordinates). It plots the WRSI as a heat map over the region. Finally, this files allows the user to download the output as a csv file so users can easily feed into and ABM in order to have a more rigorous synthetic terrain for their models. 

##### Help Wanted

The goal of Mesa Data and these data pipelines is to create a robust simulation ecosystem so researchers and practitioners can rapidly create, explore and reproduce rigorous models to explore complex phenomenon. Any help in improving this data pipelines or building a new one is more than welcome!



*McNally, A., Arsenault, K., Kumar, S., Shukla, S., Peterson, P., Wang, S., Funk, C., Peters-Lidard, C.D., & Verdin, J. P. (2017). A land data assimilation system for sub-Saharan Africa food and water security applications. Scientific Data, 4, 170012*
