# AddedConnectedAccountItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**account_id** | **str** | ID of the created account. | 
**name** | **str** | Human-readable account name. | 
**parent_account_id** | **str** | Parent account ID — present only for sub-accounts in an NLV2 hierarchy. | [optional] 
**status** | [**ConnectedAccountApprovalStatus**](ConnectedAccountApprovalStatus.md) |  | 

## Example

```python
from fireblocks.models.added_connected_account_item import AddedConnectedAccountItem

# TODO update the JSON string below
json = "{}"
# create an instance of AddedConnectedAccountItem from a JSON string
added_connected_account_item_instance = AddedConnectedAccountItem.from_json(json)
# print the JSON string representation of the object
print(AddedConnectedAccountItem.to_json())

# convert the object into a dict
added_connected_account_item_dict = added_connected_account_item_instance.to_dict()
# create an instance of AddedConnectedAccountItem from a dict
added_connected_account_item_from_dict = AddedConnectedAccountItem.from_dict(added_connected_account_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


