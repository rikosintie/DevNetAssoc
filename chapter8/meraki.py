from meraki_sdk.meraki_sdk_client import MerakiSdkClient

#  Cisco DevNet Sandbox Meraki API key
X_CISCO_MERAKI_API_KEY = '6bec40cf957de430a6f1f2baa056b99a4fac9ea0'

#  Establish a new client connection to the Meraki REST API
MERAKI = MerakiSdkClient(X_CISCO_MERAKI_API_KEY)

#  Get a list of all the organizations for the Cisco DevNet account
ORGS = MERAKI.organizations.get_organizations()
print('ORGS Type: ', type(ORGS))
for ORG in ORGS:
    print(" Org ID: {} and Org Name: {} ".format(ORG['id'], ORG['name']))

PARAMS = {}
#  adds a key of organization_id with a value of 549236
PARAMS["organization_id"] = "549236"  # Demo Organization "DevNet Sandbox"
print('PARAMS = ', PARAMS)

#  Get a list of all the networks for the Cisco DevNet organization
NETS = MERAKI.networks.get_organization_networks(PARAMS)
print('Nets =: ', type(NETS))
for NET in NETS:
    #  print("Network ID: {0:20s}; Name: {1:45s}, Tags: {2:<10s} ".format(NET['id'], NET['name'], str(NET['tags'])))
    print(f'Network ID:, {NET.get("id") :20}, Name:, {NET.get("name") :45}, \
Tags:, {str(NET.get("tags")) :<4}')
#  Get a list of all the devices that are part of the Always On Network
DEVICES = MERAKI.devices.get_network_devices("L_646829496481105433")
for DEVICE in DEVICES:
    print("Device Model: {0:9s}, Serial: {1:14s}, MAC: {2:17}, \
          Firmware: {3:12s} ".format(DEVICE['model'], DEVICE['serial'],
                                     DEVICE['mac'], DEVICE['firmware']))
