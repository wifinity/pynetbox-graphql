# pynetbox-graphql

Extends pynetbox to support NetBox GraphQL API.


## Quick Start

```python
import pynetbox_graphql

# Initialize the client
netbox = pynetbox_graphql.api(
    url="https://your-netbox-instance.com/graphql/",
    token="your-api-token"
)

# Use REST API in the normal way

device = nb.dcim.devices.get(id=1)

device.serialize()
{'id': 1,
 'url': 'http://localhost:8001/api/dcim/devices/1/',
 'display_url': 'http://localhost:8001/dcim/devices/1/',
 'display': 'hostname',
 'name': 'hostname',
 'device_type': 12,
 'role': 1,
 'tenant': 1,
 'platform': None,
 'serial': 'serial',
 'asset_tag': 'tag',
...

# Make a GraphQL Query

query = '''
{
  site(id: 467) {
    name
    devices {
      name
      primary_ip4 {
        address
      }
      interfaces {
        mac_address
      }
    }
  }
}
'''

nb.gql(query)

{
  "data": {
    "site": {
      "name": "sitename",
      "devices": [
        {
          "name": "hostname",
           "primary_ip4": {
             "address": "192.168.1.100/24"
           },
          "interfaces": [
            {
              "name": "eth1",
              "mac_address": null
            },
            {
              "name": "vlan1",
               "mac_address": "XX:XX:XX:XX:XX:XX"
            }
          ]
        },
        {
          "name": "hostname2",
           "primary_ip4": {
             "address": "192.168.1.101/24"
           },
          "interfaces": [
            {
              "name": "eth1",
              "mac_address": null
            }
          ]
        },
...

```
