## Chapter 8 Cisco Enterprise Networking Management Platforms and APIs

Chapter 8 is all about the Meraki Cloud API and using the Meraki SDK. After an introduction the Meraki philosophy you log into the dashboard and create your API key. All access to the API requires the API key.

**Useful websites**  
[VSCode Virtual Environments](https://code.visualstudio.com/docs/python/environments)  
It's a best practice to use virtual environments for Python development. This article explains how to set them up in VSCode. I made the mistake of creating the venv in the terminal, not in the VSCode terminal. I had to delete it and start over. But once you realize what to do it's identical, just create it in the VSCode terminal.

[Introduction to Meraki Dashboard API](https://developer.cisco.com/meraki/api-v1/#!introduction/meraki-dashboard-api)  
The certification guide is based on API v0 but that is EOL. So far everything in the book has worked correctly.

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
means substitute the third variabale in format tags, convert the type to string, left align it, make this field 10 string characters wide.

These "String Formatters" allow the output to be aligned. 

```
               20 characters                           45 characters                         10 chars
            12345678901234567890        123456789012345678901234567890123456789012345        1234567890
Network ID: L_646829496481105433, Name: DevNet Sandbox ALWAYS ON                     , Tags: None 

Note that the "," gets printed but not counted. You can change it to any character. For example, here I chagned the "," after Network ID to a ";".
Network ID: L_646829496481105433; Name: DevNet Sandbox ALWAYS ON                     , Tags: None
```


**The print statement rewritten to use f strings**  
Notice that I used a single quote after the f and double quotes for the variables. If you use single for both you wil get an error that the statement has an open {. It took me quite a while to figure that out!

```
    print(f'Network ID:, {NET.get("id") :20}, Name:, {NET.get("name") :45}, \
Tags:, {str(NET.get("tags")) :<4}')
```
