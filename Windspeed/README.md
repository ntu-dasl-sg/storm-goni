# Downloading windspeed data from NOAA
Investigating the effect of spatial correlation (e.g. clustered observations) on the tephra inversion model results.

To create a damage model for this typhoon event, we need wind speed values for all municipalities of our study area. Here, we download windspeeds at 10 meter elevation from the [NOAA/NCEP Global Forecast System (GFS) Atmospheric Model](https://www.ncdc.noaa.gov/data-access/model-data/model-datasets/global-forcast-system-gfs) using the [rWind](https://cran.r-project.org/web/packages/rWind/index.html) package, and extract the average/ maximum wind speed value at the location of each municipality. In the end, we produce a CSV file listing all municipalities and the assigned windspeed in km/h.

This code needs a shapefile `PH_municipality.shp` in the folder `/Data/`. This shapefile contains the polygons of all municipalities with associated attributes.

# View results:
1. Get the windspeed outputs as csv files from /Output_CSV. You can either get the mean or maximum windspeed for each municipality.
  * Municipalities_with_Windspeed_Mean.csv
  * Municipalities_with_Windspeed_Max.csv

# How to use RMarkdown file:
View the documentation with the html file. Feel free to edit the Rmarkdown file using the following guide.

1. Place the .RProj file to where you want your home folder to be set.
2. This file needs PH_municipality.shp located in /Data
3. Edit line 148 and 165 if you want to switch between maximum or average windspeeds for each municipality.
4. Output figures are located at /Figures/
5. Output CSV files in /Output_CSV/
