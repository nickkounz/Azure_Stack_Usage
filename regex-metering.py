import re
import json
import collections

output = []
with open('report.txt','r+') as file:
    file_json = json.load(file)
    #print(file_json['value'])
    for f in file_json['value']:
        output.append(f['properties']['meterId'])
#    print(output)

no_duplicate_result = (set([item for item in output if output.count(item) >1 ]))
for n in no_duplicate_result:
    

    print(n)


# "meterId": "09F8879E-87E9-4305-A572-4B7BE209F857",
