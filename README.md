# Working with azure stack usage
Use Python to get Admin/Tenants usage from Azure Stack. This script works for both asdk and the integrated systems.

## Components
* generate_usage_rep.py - generate the reports
* calc_meters.py - calculate the meter ids with no duplications
* convert_to_excel.py - convert the report from json to excel format
* PRIVATEwithPass.txt - declare all your credentials

## Get Started
Create and fill the "PRIVATEwithPass.txt" with following without space
* 1st line => client_id
* 2nd line => client_secret
```
client_id and client_secret are the values that generated from Azure AD app registration.
```
* 3rd line => username
* 4th line => password
```
username and password are the credentials that you use to authenticate with Azure.
```
* 5th line => directory_id
```
Login to Microsoft Azure > Azure Active Directory > Properties > Directory ID
```
* 6th line => admin_arm_url
```
{adminmanagement_url} for example, https://adminportal.local.azurestack.external
```

## How to use the script
Edit the variables below to suit to your environment in generate_usage_rep.py. A json file will be generated.
* tenant_sub_name = 'Shared-Worker-Tier'
* start_time = "2017-12-8"
* end_time = "2017-12-11"
* granularity = "Hourly"
Change 'file' variable in conver_to_xls.py and execute the script. A excel spreadsheet will be generated under the output folder.
