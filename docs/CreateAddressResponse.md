# CreateAddressResponse


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**address** | **str** |  | [optional] 
**legacy_address** | **str** |  | [optional] 
**enterprise_address** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**bip44_address_index** | **int** |  | [optional] 

## Example

```python
from fireblocks_client.models.create_address_response import CreateAddressResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAddressResponse from a JSON string
create_address_response_instance = CreateAddressResponse.from_json(json)
# print the JSON string representation of the object
print CreateAddressResponse.to_json()

# convert the object into a dict
create_address_response_dict = create_address_response_instance.to_dict()
# create an instance of CreateAddressResponse from a dict
create_address_response_form_dict = create_address_response.from_dict(create_address_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


