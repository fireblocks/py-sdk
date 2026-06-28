# CreatedConnectedAccountItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the created account. | 
**name** | **str** | Human-readable account name. | 
**parent_account_id** | **str** | Parent account ID — present only for sub-accounts in an NLV2 hierarchy. | [optional] 
**status** | [**ConnectedAccountApprovalStatus**](ConnectedAccountApprovalStatus.md) |  | 

## Example

```python
from fireblocks.models.created_connected_account_item import CreatedConnectedAccountItem

# TODO update the JSON string below
json = "{}"
# create an instance of CreatedConnectedAccountItem from a JSON string
created_connected_account_item_instance = CreatedConnectedAccountItem.from_json(json)
# print the JSON string representation of the object
print(CreatedConnectedAccountItem.to_json())

# convert the object into a dict
created_connected_account_item_dict = created_connected_account_item_instance.to_dict()
# create an instance of CreatedConnectedAccountItem from a dict
created_connected_account_item_from_dict = CreatedConnectedAccountItem.from_dict(created_connected_account_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


