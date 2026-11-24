# CreateOmnibusAddressesRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** | The number of deposit addresses to create | 
**descriptions** | **List[str]** | Descriptions of the newly created addresses, in order. Must match &#x60;count&#x60; when provided. Each entry is trimmed; an empty string leaves that address without a description. | [optional] 

## Example

```python
from fireblocks.models.create_omnibus_addresses_request import CreateOmnibusAddressesRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOmnibusAddressesRequest from a JSON string
create_omnibus_addresses_request_instance = CreateOmnibusAddressesRequest.from_json(json)
# print the JSON string representation of the object
print(CreateOmnibusAddressesRequest.to_json())

# convert the object into a dict
create_omnibus_addresses_request_dict = create_omnibus_addresses_request_instance.to_dict()
# create an instance of CreateOmnibusAddressesRequest from a dict
create_omnibus_addresses_request_from_dict = CreateOmnibusAddressesRequest.from_dict(create_omnibus_addresses_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


