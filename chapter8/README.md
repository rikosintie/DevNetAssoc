## Chapter 8 Cisco Enterprise Networking Management Platforms and APIs

Chapter 8 is all about the Meraki Cloud API and using the Meraki SDK. After an introduction the Meraki philosophy you log into the dashboard and create your API key. All access to the API requires the API key.

**Useful websites**  
[VSCode Virtual Environments](https://code.visualstudio.com/docs/python/environments)  
It's a best practice to use virtual environments for Python development. This article explains how to set them up in VSCode. I made the mistake of creating the venv in the terminal, not in the VSCode terminal. I had to delete it and start over. But once you realize what to do it's identical, just create it in the VSCode terminal.

[Introduction to Meraki Dashboard API](https://developer.cisco.com/meraki/api-v1/#!introduction/meraki-dashboard-api)  
The certification guide is based on API v0 but that is EOL. So far everything in the book has worked correctly.

[Cisco DNA Center Platform Overview](https://developer.cisco.com/docs/dna-center/#!cisco-dna-center-platform-overview/cisco-dna-center-platform-overview)  
Everything you need to know about DNA center APIs. After readning up to location 5095 in the ebook or page 193 in the print book, you should go to this URL and review.  

[dnacentersdk Quick Start](https://dnacentersdk.readthedocs.io/en/latest/api/quickstart.html)  
Tips on common mistakes and environment variables.


[DNA Sandbox](https://sandboxdnac2.cisco.com)  
Username: devnetuser  
password: Cisco123!  
base64 encoding: ZGV2-bmV0dXNlcjpDaXNjbzEyMyE=  


Note: Only chromium based browsers and Firefox are supported. The certificate is bad, when you get the warning type `thisisunsafe` without clicking on any of the buttons.  

[Introduction to Postman](https://learning.postman.com/docs/getting-started/introduction/)  
Repeated here in case you need a review!  

[Python String Formatting](https://thepythonguru.com/python-string-formatting/)  
[Python String Format Cookbook](https://mkaz.blog/code/python-string-format-cookbook/)  
These two sites do a great job of explaining string formatting. The Cookbook has a section on using f strings. F Strings were introduced in 3.6 and are much easier to use. I rewrote the print statement in the first python script to use f strings as an excercise.  

[Add a keyvalue pair to dictionary in python](add-a-keyvalue-pair-to-dictionary-in-python)  
I had forgotten that this statement adds a key to a dictionary. This site had a good review.

```
PARAMS = {}
#  adds a key of organization_id with a value of 549236
PARAMS["organization_id"] = "549236"  # Demo Organization "DevNet Sandbox"
```
Here is what PARAMS looks like printed  
`PARAMS =  {'organization_id': '549236'}`

### The first Python script to access the API
The book has the entire script so you can just copy it. I was bit confused about this print statement:  
`print("Network ID: {0:20s}, Name: {1:45s}, Tags: {2:<10s} ".format(NET['id'], NET['name'], str(NET['tags'])))`

"network ID:" {0:20s}  
means substitute the first variable in format id, make the field 20 string characters wide.

Name: {1:45s}  
means substitute the second variabale in format name, make this field 45 string characters wide.

Tags: {2:<10s}  
means substitute the third variabale in format tags, left align it, make this field 10 string characters wide.

str(NET['tags']  
This caused me some issues when I converted to use f strings. If you look at the value of the tags field it's the word "None" which is a python reserved word. I kept getting an error that I couldn't format the type None. I finally noticed that they had put the str() function on. I added that `{str(NET.get("tags"))` and it solved the problem.

These "String Formatters" allow the output to reamain aligned as the Name varies. 

```
               20 characters                           45 characters                             10 chars
             12345678901234567890         123456789012345678901234567890123456789012345          1234567890
Network ID:, L_646829496481105433, Name:, DevNet Sandbox ALWAYS ON                      , Tags:, None 
Network ID:, L_646829496481110685, Name:, Mike_test_vmx                                 , Tags:, None  

Note that the "," gets printed but not counted. You can change it to any character. For example, here I chagned the "," after Network ID to a ";".
Network ID: L_646829496481105433; Name: DevNet Sandbox ALWAYS ON                     , Tags: None
```


**The print statement rewritten to use f strings**  
Notice that I used a single quote after the f and double quotes for the variables. If you use single for both you wil get an error that the statement has an open {. It took me quite a while to figure that out!

```
    print(f'Network ID:, {NET.get("id") :20}, Name:, {NET.get("name") :45}, \
Tags:, {str(NET.get("tags")) :<4}')
```

### Basic Authentication for DNA Center
In Postman, you can select Authorization when creating a new request. If you select basic you are prompted to enter a username and password. To see the base64 encoded version of this combination simple click on headers and the first header listed will be "Authorization"

<p align="center" width="100%">
    <img width="95%" src="https://github.com/rikosintie/DevNetAssoc/blob/main/images/BasicAuth-in-Postman.png"> 
</p>  

Here is the equivalent curl command:  

`curl -X POST https://sandboxdnac2.cisco.com/dna/system/api/v1/auth/token -H 'Authorization: Basic ZGV2bmV0dXNlcjpDaXNjbzEyMyE='`

If you want to create the encoding using a site like [base64encode](https://www.base64encode.org) just enter devnetuser:Cisco123! and click `ENCODE`

**DNA Center with Python**  
If you get an SSL error when executing your script add `verify=False` to the `api.DNACenterAPI` call:

```
DNAC = api.DNACenterAPI(username="devnetuser",
                        password="Cisco123!",
                        base_url="https://sandboxdnac2.cisco.com",
                        verify=False)
```
