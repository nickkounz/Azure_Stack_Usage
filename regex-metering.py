import re
import os
import json
import fnmatch
import collections

# load the data, export the meterId
# replace the report_target
report_target = "vm_subFROM2017-11-27TO2017-11-28Hourly"

output = []
def export_meterid(file_name):
    with open(file_name,'r') as file:
        file_json = json.load(file)
        for f in file_json:
            output.append(f['properties']['meterId'])

report_patten = report_target + "*"

for file in os.listdir('.'):
    if fnmatch.fnmatch(file, report_patten):
        export_meterid(file)

no_duplicate_result = (set([item for item in output if output.count(item) >1 ]))
for n in no_duplicate_result:
    print(n)

print("There are " + str(len(no_duplicate_result)) + " meter ids available." )
