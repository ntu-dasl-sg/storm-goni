import ogr
import csv

N_data = {}
with open( 'All_muni_pred.csv', 'r' ) as theFile:
    reader = csv.DictReader(theFile)
    for line in reader:
        pcode = line["pcode"]
        res = line["num.damage"]
        try:
            a = float(res)
        except:
            a = 0
        N_data[pcode] = a

# get shp layer
source = ogr.Open('Municipality map_added mean wind speed//PH_municipality_results.shp',1)
lyr = source.GetLayer()

# Create new field
n_field = ogr.FieldDefn('td_pred',ogr.OFTReal)
n_field.SetWidth(20)
n_field.SetPrecision(8)
lyr.CreateField(n_field)

featList = range(lyr.GetFeatureCount())
for FID in featList:
    
    # Current feature
    feat = lyr.GetFeature(FID)
    
    # Read mun code
    mun_code = feat.GetField("Mun_Code")
    feat.SetField("td_pred",0)
    
    # Find mun code in csv
    for pcode in N_data.keys():
        if pcode == mun_code:
            feat.SetField('td_pred',N_data[pcode])
            break
            
    # update feature in layer
    lyr.SetFeature(feat)


source = None
