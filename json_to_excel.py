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

def map_data(id):
    id = id.upper()
    return {
        'F271A8A388C44D93956A063E1D2FA80B' : 'Static IP Address Usage per IP addresses',
        '9E2739BA86744796B465F64674B822BA' : 'Dynamic IP Address Usage per IP addresses',
        'B4438D5D-453B-4EE1-B42A-DC72E377F1E4' : 'TableCapacity per GB*hours',
        'B5C15376-6C94-4FDD-B655-1A69D138ACA3' : 'PageBlobCapacity per GB*hours',
        'B03C6AE7-B080-4BFA-84A3-22C800F315C6' : 'QueueCapacity per GB*hours',
        '09F8879E-87E9-4305-A572-4B7BE209F857' : 'BlockBlobCapacity per GB*hours',
        'B9FF3CD0-28AA-4762-84BB-FF8FBAEA6A90' : 'TableTransactions per Request count in 10,000s',
        '50A1AEAF-8ECA-48A0-8973-A5B3077FEE0D' : 'TableDataTransIn per Ingress data in GB',
        '1B8C1DEC-EE42-414B-AA36-6229CF199370' : 'TableDataTransOut per Outgress in GB',
        '43DAF82B-4618-444A-B994-40C23F7CD438' : 'BlobTransactions per Requests count in 10,000s',
        '9764F92C-E44A-498E-8DC1-AAD66587A810' : 'BlobDataTransIn per Ingress data in GB',
        '3023FEF4-ECA5-4D7B-87B3-CFBC061931E8' : 'BlobDataTransOut per Outgress in GB',
        'EB43DD12-1AA6-4C4B-872C-FAF15A6785EA' : 'QueueTransactions per Requests count in 10,000s',
        'E518E809-E369-4A45-9274-2017B29FFF25' : 'QueueDataTransIn per Ingress data in GB',
        'DD0A10BA-A5D6-4CB6-88C0-7D585CEF9FC2' : 'QueueDataTransOut per Outgress in GB',
        'FAB6EB84-500B-4A09-A8CA-7358F8BBAEA5' : 'Base VM Size Hours per Virtual core minutes',
        '9CD92D4C-BAFD-4492-B278-BEDC2DE8232A' : 'Windows VM Size Hours per Virtual core minutes',
        '6DAB500F-A4FD-49C4-956D-229BB9C8C793' : 'VM size hours per VM hours',
        'EBF13B9F-B3EA-46FE-BF54-396E93D48AB4' : 'Key Vault transactions per Request count in 10000s'
}.get(id, "unknown meter id")

def write_properties_csv(report, xls_file):
    with open(report,"r") as file:
        #df = pd.read_json(file)
        p_file = []
        file = json.loads(file.read())
        for f in file:
            data = map_data(f['properties']['meterId'])
            f['properties'].update({'meterName':data})
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

write_properties_csv('Linux_Single_CoreFROM2017-12-2TO2017-12-4Hourly.txt', 'Linux_Single_Core_output.xls')
