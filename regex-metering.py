import re
import os
import json
import fnmatch
import collections

# load the data, export the meterId
# replace the report_target
report_target = "app_service_subFROM2017-11-27TO2017-11-28Hourly"
output = []

# read files and get meter id
def export_meterid(file_name):
    with open(file_name,'r') as file:
        file_json = json.load(file)
        for f in file_json:
            output.append(f['properties']['meterId'])

# map meter id to data
def map_data(id):
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
}.get(id, id + "meter id not found.")

report_patten = report_target + "*"
for file in os.listdir('.'):
    if fnmatch.fnmatch(file, report_patten):
        export_meterid(file)

no_duplicate_result = (set([item for item in output if output.count(item) >1 ]))
for n in no_duplicate_result:
    print(map_data(n.upper()))

print("There are " + str(len(no_duplicate_result)) + " meter ids available." )
