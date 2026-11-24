# GetWhitelistIpAddressesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID of the user | [optional] 
**whitelisted_ips** | **List[str]** | Allowlist entries. Each item is an IPv4 address (10.0.0.1), an IPv4 CIDR (10.0.0.0/24), an IPv4 range (10.0.0.1-10.0.0.50), or an IPv6 address (2001:db8::1). | [optional] 

## Example

```python
from fireblocks.models.get_whitelist_ip_addresses_response import GetWhitelistIpAddressesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWhitelistIpAddressesResponse from a JSON string
get_whitelist_ip_addresses_response_instance = GetWhitelistIpAddressesResponse.from_json(json)
# print the JSON string representation of the object
print(GetWhitelistIpAddressesResponse.to_json())

# convert the object into a dict
get_whitelist_ip_addresses_response_dict = get_whitelist_ip_addresses_response_instance.to_dict()
# create an instance of GetWhitelistIpAddressesResponse from a dict
get_whitelist_ip_addresses_response_from_dict = GetWhitelistIpAddressesResponse.from_dict(get_whitelist_ip_addresses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


