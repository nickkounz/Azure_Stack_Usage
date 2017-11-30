# Working with asdk usage
Use Python to get Admin/Tenants usage from Azure Stack Development Tookit environment.
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
## Components
* connect-withpass.py - get the reports
* regex-metering.py - get the meter ids with no duplications
* _PRIVATEwithPass.txt - declare all your credentials
## More
[Use this link to see more](http://www.nikknz.com/2017/11/use-python-to-get-admintenants-usage.html)
