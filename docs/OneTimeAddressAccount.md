# OneTimeAddressAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_time_address** | **str** |  | 
**tag** | **str** |  | [optional] 

## Example

```python
from fireblocks_client.models.one_time_address_account import OneTimeAddressAccount

# TODO update the JSON string below
json = "{}"
# create an instance of OneTimeAddressAccount from a JSON string
one_time_address_account_instance = OneTimeAddressAccount.from_json(json)
# print the JSON string representation of the object
print(OneTimeAddressAccount.to_json())

# convert the object into a dict
one_time_address_account_dict = one_time_address_account_instance.to_dict()
# create an instance of OneTimeAddressAccount from a dict
one_time_address_account_from_dict = OneTimeAddressAccount.from_dict(one_time_address_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


