Fill the "PRIVATEwithPass.txt" with following without space:
1st line => client_id

2nd line => client_secret

3rd line => username

4th line => password

5th line => app_id_uri
app_id_uri is getting from asdk, run the following powershell command on asdk to get the app_id_uri
(Invoke-RestMethod "http://{adminmanagement_url}/metadata/endpoints?api-version=2015-01-01").authentication.audiences[0]

6th line => directory_id
To get the directory_id. Login to Microsoft Azure > Azure Active Directory > Properties > Directory ID

7th line => admin_arm_url
https://adminmanagement.domain
