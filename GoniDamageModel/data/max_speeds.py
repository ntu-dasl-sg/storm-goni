import pandas as pd
import os

direc = 'G:\\My Drive\\Risk_Analytics_for_Society_Lab_Workspace\\6_Projects\\6.21_Typhoons in Philippines\\Goni hazard data\\Wind\\Goni Max Windspeed_Different times\\_CSVs for all'

# Initialize new data frame
df = pd.read_csv( os.path.join(direc, 
                    'Municipalities_with_Windspeed_Max_2020-10-31 T 3.csv') )
new_df = df

# Iterate through files
date = ['10-31', '11-01', '11-02']
filename = 'Municipalities_with_Windspeed_Max_2020-'
num = [0,3,6,9,12,15,18,21]
names = []
for d in date:
    for n in num:
        try:
            df = pd.read_csv( os.path.join(direc,
                            filename + d + ' T '+str(n)+'.csv') )
        except:
            continue
        # Max windspeed
        name = 'wind_'+d+'_'+str(n)
        names.append( name )
        wind = df['Wind_Speed']
        new_df[name] = wind
        
# Max
new_df['Max_Wind_Speed'] = new_df[names].max(1)

    