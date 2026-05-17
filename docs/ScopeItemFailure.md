# ScopeItemFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider_id** | **str** | Identifier of the provider for which the request failed. | 
**account_id** | **str** | Identifier of the account for which the request failed (optional). | [optional] 
**error** | [**TradingErrorSchema**](TradingErrorSchema.md) |  | 

## Example

```python
from fireblocks.models.scope_item_failure import ScopeItemFailure

# TODO update the JSON string below
json = "{}"
# create an instance of ScopeItemFailure from a JSON string
scope_item_failure_instance = ScopeItemFailure.from_json(json)
# print the JSON string representation of the object
print(ScopeItemFailure.to_json())

# convert the object into a dict
scope_item_failure_dict = scope_item_failure_instance.to_dict()
# create an instance of ScopeItemFailure from a dict
scope_item_failure_from_dict = ScopeItemFailure.from_dict(scope_item_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


