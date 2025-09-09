# AccountBase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The ID of the account | 
**name** | **str** | The name of the account | 

## Example

```python
from fireblocks.models.account_base import AccountBase

# TODO update the JSON string below
json = "{}"
# create an instance of AccountBase from a JSON string
account_base_instance = AccountBase.from_json(json)
# print the JSON string representation of the object
print(AccountBase.to_json())

# convert the object into a dict
account_base_dict = account_base_instance.to_dict()
# create an instance of AccountBase from a dict
account_base_from_dict = AccountBase.from_dict(account_base_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


