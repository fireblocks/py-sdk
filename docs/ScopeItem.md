# ScopeItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | The ID of the provider associated with the account. | 
**account_id** | **str** | The ID of the account associated with the provider. | [optional] 

## Example

```python
from fireblocks.models.scope_item import ScopeItem

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeItem from a JSON string
scope_item_instance = ScopeItem.from_json(json)
# print the JSON string representation of the object
print(ScopeItem.to_json())

# convert the object into a dict
scope_item_dict = scope_item_instance.to_dict()
# create an instance of ScopeItem from a dict
scope_item_from_dict = ScopeItem.from_dict(scope_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


