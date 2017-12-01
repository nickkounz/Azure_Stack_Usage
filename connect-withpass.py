import requests
import json
import urllib3
import re
import sys

# disable warnings
urllib3.disable_warnings()

# read private credentials from text file
client_id, client_secret, username, password, directory_id, admin_arm_url, *_ = open('_PRIVATEwithPass.txt').read().split('\n')
if (client_id.startswith('*') and client_id.endswith('*')) or \
    (client_secret.startswith('*') and client_secret.endswith('*')):
    print('MISSING CONFIGURATION: the _PRIVATEwithPass.txt file needs to be edited ' + \
        'to add client ID and secret.')
    sys.exit(1)

# get authentication_audiences_url
get_metadata_endpoint = requests.get(admin_arm_url + "/metadata/endpoints?api-version=2015-01-01", verify=False).text
authentication_audiences_url = json.loads(get_metadata_endpoint)['authentication']['audiences'][0]

# acquire access_token
microsoft_url = "https://login.microsoftonline.com/" + directory_id + "/oauth2/token?api-version=1.0"
post_headers = {"Content-Type": "application/x-www-form-urlencoded"}
post_data = {
    "grant_type" : "password",
    "scope" : "openid",
    "resource" : authentication_audiences_url,
    "client_id" : client_id,
    "client_secret" : client_secret,
    "username" : username,
    "password" : password
}

response = requests.post(microsoft_url, data = post_data, headers = post_headers)
# print(response.text)
result_json = json.loads(response.text)
my_token = result_json['access_token']

# get subscriptionId
admin_sub_url = admin_arm_url + "/subscriptions/?api-version=2015-06-01-preview"
get_headers = { "Content-Type": "application/json", "Authorization": "Bearer " + my_token }
get_response = requests.get(admin_sub_url, headers=get_headers, verify=False)
get_response_json = json.loads(get_response.text)
output_subscription_id = get_response_json['value'][0]['subscriptionId']
print("subscription id: " + output_subscription_id)
#print("tenant id: " + output_tenantId)

# get all tenants information
list_tenants_url = admin_arm_url + "/subscriptions/" + output_subscription_id + "/providers/Microsoft.Subscriptions.Admin/subscriptions?api-version=2015-11-01&$filter="
list_tenants_response = requests.get(list_tenants_url, headers=get_headers, verify=False)
list_tenants_response_json = json.loads(list_tenants_response.text)
# print(json.dumps(list_tenants_response_json, indent=4))

# return tenant information
def return_tenant_info(display_name):
    for tenant in list_tenants_response_json['value']:
        if tenant['displayName'] == display_name:
            return json.dumps(tenant,indent=4)

# return tenant id
def return_tenant_id(display_name):
    for tenant in list_tenants_response_json['value']:
        if tenant['displayName'] == display_name:
            return tenant['subscriptionId']

# write report
def write_report(file_name, file_content):
    with open(file_name, 'a+') as report:
        report.write(file_content)

# get usage for tenantId
# define the report rule information
tenant_sub_name = 'Windows_Mutiple_Core'
select_tenantId = return_tenant_id(tenant_sub_name)
print(select_tenantId)
start_time = "2017-11-29"
end_time = "2017-12-1"
granularity = "Hourly"
api_version = "2015-06-01-preview"
usage_url = admin_arm_url + "/subscriptions/" + output_subscription_id + \
            "/providers/Microsoft.Commerce/subscriberUsageAggregates?reportedStartTime=" + start_time + \
            "&reportedEndTime=" + end_time + \
            "&aggregationGranularity=" + granularity  + \
            "&subscriberId=" + select_tenantId + \
            "&api-version=" + api_version
print(usage_url)

# initial get request
usage = requests.get(usage_url, headers=get_headers, verify=False)
usage_json = json.loads(usage.text)
usage_value = usage_json['value']
usage_value_dump = json.dumps(usage_value, indent=4)

# check if nextLink is available
try:
    next_url = usage_json['nextLink']
except:
    print("nextLink is not available.")

# give report a name
report_name_convention = tenant_sub_name + "FROM" + start_time + "TO" + end_time + granularity
report_name = report_name_convention + ".txt"
write_report(report_name, usage_value_dump)

# get next page usage
next_usage = requests.get(next_url, headers=get_headers, verify=False)
next_usage_json = json.loads(next_usage.text)

# if result is more than one page, use the nextLink.
i = 2
while (usage_json['nextLink']):
    usage_next = requests.get(usage_json['nextLink'], headers=get_headers, verify=False)
    usage_next_json = json.loads(usage_next.text)
    usage_next_value = usage_next_json['value']
    usage_next_value_dump = json.dumps(usage_next_value, sort_keys=True, indent=4)
    try:
        usage_json['nextLink'] = usage_next_json['nextLink']
        report_name = report_name_convention + "_Page_" + str(i) + ".txt"
        write_report(report_name, usage_next_value_dump)
        i += 1
        #print(usage_next_value)
    except KeyError:
        print("End of Report.")
        usage_json['nextLink'] = False
