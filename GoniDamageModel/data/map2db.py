import csv
import pandas as pd
import numpy as np

df = pd.read_csv( 'Municipalities_with_Windspeed_Max.csv' )
df2 = pd.read_csv( 'All_Goni_pred.csv' )

# pcodes = np.unique(df2['pcode'])

for i in range(len(df)):
# count = 0
# new_df = {}
# for pcode in pcodes:
    
    wind_speed = df['Max_Wind_Speed'][i]
    pcode = df['Mun_Code'][i]
    # Look pcode in df2
    try:
        indices = np.where( df2['pcode'] == pcode )[0]
        # if pcode=='PH012801000':
        #     a=1
        # Fill df2 col
        # for index in indices:
        df2['Wind.speed.max'][indices[0]] = wind_speed
        # count += 1
        
    except:
        pass

# Save to csv        
df2.to_csv('All_Goni_pred_new.csv')

