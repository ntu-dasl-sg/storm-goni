# Damage Prediction Model: Philippines, Typhoon Goni

## Overview

The model developed by the Disaster Analytics for Society lab (DASL) at the Nanyang Technological University, Singapore is a multivariate logit regression with readily available typhoon characteristics (e.g. wind speed, distance to first impact) and socio-economic parameters as predictors ([510 Global](https://dashboard.510.global/#!/impact_database)). The latter include, building quality, population density and experience with past typhoons, which is a metric developed by DASL for the average number of typhoons withstood by the region where the municipality belongs to, previous to the current typhoon. In contrast to the priority index developed by the Netherlands Red Cross which uses data from 4 past typhoons (Haiyan, Melor, Hagupit and Rammasun) and a Random Forest Regressor to predict the number of damaged houses, our model is trained on data from 12 past typhoons (Bopha, Goni 2015, Hagupit, Haima, Haiyan, Kalmaegi, Koppu, Melor, Nock-Ten, Rammasun, Arika and Utor). The training dataset consists of 15 potential predictors and the final model was chosen after tests for multicollinearity and predictive capacity through cross-validation. 

## Code and Documentation

The Rmd file contains the code used to perform the analysis and generate the damage estimates. Detailed information on the model development and limitations are also provided within. For quick reference, open the html file to view the documentation. 

## Output Data and Graphics

All_Goni_pred.csv in the data folder contains the damage predictions per municipality together with their standard errors:

- Total.damaged.houses..rel..: Estimated damage rate
- Total.damaged.houses..abs..: Estimate of the number of damaged houses
- Total.damaged.houses..rel..se: Standard error of the estimated damage rate
- Total.damaged.houses..abs..se: Standard error of the estimated number of damaged houses
- Completely.damaged..rel..: Estimated complete damage rate
- Completely.damaged..abs..: Estimate of the number of completely damaged houses
- Completely.damaged..rel..se: Standard error of the estimated number of completely damaged houses
- Completely.damaged..abs..se: Standard error of the estimated number of completely damaged houses

In the graphics folder, maps of the estimated damage rate and number of damaged houses are provided. 

## Model limitations (Please Read!)

Based on the limited data available for the model, the damage model cannot predict damage from landslides, lahars or coastal surge. It is a statistical model relating typhoon characteristics (wind speed, distance from 1st impact, etc) and simple vulnerability characteristics to the probability of damage based on 12 past typhoons in the Philippines.

It is **not an observational estimate and has not been validated against damage observations from Typhoon Goni**, and is purely predictive based on data on the typhoon and the municipalities affected. While the predicted values should be taken with caution due to the large expected uncertainty in different sources (e.g. wind speed estimation, data-scarcity in some regions, etc.), they can be interpreted as average order-of-magnitude estimates with the best available data openly available at the moment. Although an objective model selection criteria was used, the model and hence predictions have also been guided by the modeller’s (i.e. DASL) best interpretation of the damaging process and the exploratory data analysis of the available dataset. For that reason, the dataset and the model are made available for the user to test alternative criteria.

Full disclaimer and limitations can be found in the Rmd file. The code is made available for further re-use, but we ask that you contact us if you intend to do so.

## Data Source

The model is based on data from 12 past typhoons obtained from the (Netherlands Red Cross)[https://dashboard.510.global/#!/impact_database] and wind data from the (NOAA/NCEP Global Forecast System (GFS) Atmospheric Model)[https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs].

The municipality level data adopted from Netherlands Red Cross includes the following:
* Number of damaged houses from past typhoons: Department of Social Welfare and Development (DSWD) and the National Disaster Risk Reduction and Management Council (NDRRMC)
* Population: Philippine Statistics Authority; received from UN OCHA (HDX)
* Poverty: Pantawid Pamilyang Pilipino Program
* Geographical features (slope and ruggedness): Netherlands Red Cross
* Building quality (roof and wall materials): Netherlands Red Cross
