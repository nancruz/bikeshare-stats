import os, json, re
import pandas as pd

# this finds our json files
path_to_json = 'data/'
json_files = [pos_json for pos_json in os.listdir(path_to_json) if pos_json.endswith('.json')]

# here I define my pandas Dataframe with the columns I want to get from the json
jsons_data = pd.DataFrame(columns=['station', 'ratio', 'long/lat'])

# we need both the json and an index number so use enumerate()
for index, js in enumerate(json_files):
    timestamp = js[9:]
    timestamp = timestamp[:-5]

    with open(os.path.join(path_to_json, js)) as json_file:
        json_text = json.load(json_file)

        # here you need to know the layout of your json and each json has to have
        # the same structure (obviously not the structure I have here)
        station = json_text['features'][0]['properties']['desig_comercial'] 
        lonlat = json_text['features'][0]['geometry']['coordinates'][0]
        ratio = json_text['features'][0]['properties']['racio']
        # here I push a list of data into a pandas DataFrame at row given by 'index'
        jsons_data.loc[index] = [station, ratio, lonlat]

# now that we have the pertinent json data in our DataFrame let's look at it
print(jsons_data)
print(json_files)
