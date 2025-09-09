# AccountProviderID


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The ID of the provider associated with the account. | 
**account_id** | **str** | The ID of the account associated with the provider. | 

## Example

```python
from fireblocks.models.account_provider_id import AccountProviderID

# TODO update the JSON string below
json = "{}"
# create an instance of AccountProviderID from a JSON string
account_provider_id_instance = AccountProviderID.from_json(json)
# print the JSON string representation of the object
print(AccountProviderID.to_json())

# convert the object into a dict
account_provider_id_dict = account_provider_id_instance.to_dict()
# create an instance of AccountProviderID from a dict
account_provider_id_from_dict = AccountProviderID.from_dict(account_provider_id_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


