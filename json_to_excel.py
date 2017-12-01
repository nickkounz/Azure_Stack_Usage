import pandas as pd
from pandas.io.json import json_normalize
import json

def pandas_read(file_name):
    with open(file_name, "r") as file:
        df = pd.read_json(file_name)
        # file = json.loads(file.read())
        # df = {}
        # for f in file:
        #     #print(json.dumps(f['properties']))
        #     df.update(json.dumps(f['properties']))
        #df = pd.read_json(json.loads(df))
        #print(df)
        df.to_excel('output.xls', index = False)

#pandas_read('Windows_Mutiple_CoreFROM2017-11-29TO2017-12-1Hourly.txt')

def write_properties_csv(report, xls_file):
    with open(report,"r") as file:
        #df = pd.read_json(file)
        p_file = []
        file = json.loads(file.read())
        for f in file:
            p_file.append(f['properties'])
        p_json_file = json.dumps(p_file)
        df = pd.read_json(p_json_file)
        df.to_excel(xls_file, index = False)
        #json_normalize(file)
        #for f in file:
            #print(json.dumps(f['properties']))
            #df.update(json.dumps(f['properties']))
        # file = pd.read_json(file.read())
        # file = file['properties']
        # file.to_excel(xls_file, index = False)
        #print(file['properties'])
        #with open(csv_file,"w+") as csv_file:
        #     writer = csv.write(csv_file, delimiter=',')
        #     for f in file:
        #         for k,v in f['properties']:

write_properties_csv('Windows_Mutiple_CoreFROM2017-11-29TO2017-12-1Hourly.txt', 'properties_output.xls')
