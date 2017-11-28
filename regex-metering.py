import re
import json
import collections

# load the data, export the meterId
output = []
def export_meterid(file_name):
    with open(file_name,'r') as file:
        file_json = json.load(file)
        for f in file_json:
            output.append(f['properties']['meterId'])

export_meterid('vm_subFROM2017-11-27TO2017-11-28Hourly.txt')
export_meterid('vm_subFROM2017-11-27TO2017-11-28Hourly_Page_2.txt')
export_meterid('vm_subFROM2017-11-27TO2017-11-28Hourly_Page_3.txt')

no_duplicate_result = (set([item for item in output if output.count(item) >1 ]))
for n in no_duplicate_result:
    print(n)

# output = []
# with open('vm_subFROM2017-11-27TO2017-11-28Hourly.txt','r+') as file:
#     file_json = json.load(file)
#     #print(file_json['value'])
#     for f in file_json:
#         output.append(f['properties']['meterId'])
# #    print(output)
#
# # remove duplicate meterId
# no_duplicate_result = (set([item for item in output if output.count(item) >1 ]))
# for n in no_duplicate_result:
#     print(n)

# "meterId": "09F8879E-87E9-4305-A572-4B7BE209F857",


# 'vm_subFROM2017-11-27TO2017-11-28Hourly.txt'
