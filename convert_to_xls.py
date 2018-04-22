import pandas as pd
from pandas.io.json import json_normalize
import json
from meter_mapping import map_data

def pandas_read(file_name):
    with open(file_name, "r") as file:
        df = pd.read_json(file_name)
        df.to_excel('output.xls', index = False)

def write_properties_csv(report, xls_file):
    with open(report,"r") as file:
        p_file = []
        file = json.loads(file.read())
        for f in file:
            data = map_data(f['properties']['meterId'])
            f['properties'].update({'meterName':data})
            p_file.append(f['properties'])
        p_json_file = json.dumps(p_file)
        df = pd.read_json(p_json_file)
        df.to_excel(xls_file, index = False)

file = "Shared-Worker-TierFROM2017-12-8TO2017-12-11Hourly"
file_txt = file + '.txt'
file_xls = file + '.xls'
pre_location = ".\\output\\"
write_properties_csv(pre_location + file_txt, pre_location + file_xls)
