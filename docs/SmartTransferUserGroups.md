# SmartTransferUserGroups

Data object with result data

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_group_ids** | **List[str]** | Data object with result data | 

## Example

```python
from fireblocks.models.smart_transfer_user_groups import SmartTransferUserGroups

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferUserGroups from a JSON string
smart_transfer_user_groups_instance = SmartTransferUserGroups.from_json(json)
# print the JSON string representation of the object
print(SmartTransferUserGroups.to_json())

# convert the object into a dict
smart_transfer_user_groups_dict = smart_transfer_user_groups_instance.to_dict()
# create an instance of SmartTransferUserGroups from a dict
smart_transfer_user_groups_from_dict = SmartTransferUserGroups.from_dict(smart_transfer_user_groups_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


