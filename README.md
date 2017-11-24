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
* 5th line => app_id_uri (Run the following PowerShell command on asdk to get the app_id_uri.)
```
(Invoke-RestMethod "http://{adminmanagement_url}/metadata/endpoints?api-version=2015-01-01").authentication.audiences[0]
```
* 6th line => directory_id (Login to Microsoft Azure > Azure Active Directory > Properties > Directory ID)
* 7th line => admin_arm_url
```
{adminmanagement_url}
```
