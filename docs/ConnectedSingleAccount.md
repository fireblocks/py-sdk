# ConnectedSingleAccount


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sub_accounts_ids** | **List[str]** | IDs of sub-accounts associated with this connected account. | [optional] 

## Example

```python
from fireblocks.models.connected_single_account import ConnectedSingleAccount

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedSingleAccount from a JSON string
connected_single_account_instance = ConnectedSingleAccount.from_json(json)
# print the JSON string representation of the object
print(ConnectedSingleAccount.to_json())

# convert the object into a dict
connected_single_account_dict = connected_single_account_instance.to_dict()
# create an instance of ConnectedSingleAccount from a dict
connected_single_account_from_dict = ConnectedSingleAccount.from_dict(connected_single_account_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


