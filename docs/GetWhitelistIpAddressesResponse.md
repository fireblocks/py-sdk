# GetWhitelistIpAddressesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_id** | **str** | The ID of the user | [optional] 
**whitelisted_ips** | **List[str]** | List of whitelisted ip addresses | [optional] 

## Example

```python
from fireblocks_client.models.get_whitelist_ip_addresses_response import GetWhitelistIpAddressesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetWhitelistIpAddressesResponse from a JSON string
get_whitelist_ip_addresses_response_instance = GetWhitelistIpAddressesResponse.from_json(json)
# print the JSON string representation of the object
print GetWhitelistIpAddressesResponse.to_json()

# convert the object into a dict
get_whitelist_ip_addresses_response_dict = get_whitelist_ip_addresses_response_instance.to_dict()
# create an instance of GetWhitelistIpAddressesResponse from a dict
get_whitelist_ip_addresses_response_form_dict = get_whitelist_ip_addresses_response.from_dict(get_whitelist_ip_addresses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


