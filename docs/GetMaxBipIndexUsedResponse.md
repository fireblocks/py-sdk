# GetMaxBipIndexUsedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_bip44_address_index_used** | **int** | The maximum BIP44 address index used for the vault account and asset | [optional] 
**max_bip44_change_address_index_used** | **int** | The maximum BIP44 change address index used for the vault account and asset | [optional] 

## Example

```python
from fireblocks.models.get_max_bip_index_used_response import GetMaxBipIndexUsedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMaxBipIndexUsedResponse from a JSON string
get_max_bip_index_used_response_instance = GetMaxBipIndexUsedResponse.from_json(json)
# print the JSON string representation of the object
print(GetMaxBipIndexUsedResponse.to_json())

# convert the object into a dict
get_max_bip_index_used_response_dict = get_max_bip_index_used_response_instance.to_dict()
# create an instance of GetMaxBipIndexUsedResponse from a dict
get_max_bip_index_used_response_from_dict = GetMaxBipIndexUsedResponse.from_dict(get_max_bip_index_used_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


