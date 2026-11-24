# CreateOmnibusAddressesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[OmnibusAddress]**](OmnibusAddress.md) | The created deposit addresses | 

## Example

```python
from fireblocks.models.create_omnibus_addresses_response import CreateOmnibusAddressesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOmnibusAddressesResponse from a JSON string
create_omnibus_addresses_response_instance = CreateOmnibusAddressesResponse.from_json(json)
# print the JSON string representation of the object
print(CreateOmnibusAddressesResponse.to_json())

# convert the object into a dict
create_omnibus_addresses_response_dict = create_omnibus_addresses_response_instance.to_dict()
# create an instance of CreateOmnibusAddressesResponse from a dict
create_omnibus_addresses_response_from_dict = CreateOmnibusAddressesResponse.from_dict(create_omnibus_addresses_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


