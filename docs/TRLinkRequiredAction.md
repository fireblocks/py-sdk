# TRLinkRequiredAction

A required action for processing the TRM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The action type identifier as defined by the Travel Rule provider. Values are provider-specific and may vary across different TRP implementations, so this field is intentionally not restricted to a fixed set of values. | 
**description** | **str** | Human-readable description of the action | [optional] 
**data** | [**TRLinkRequiredActionData**](TRLinkRequiredActionData.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_required_action import TRLinkRequiredAction

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkRequiredAction from a JSON string
tr_link_required_action_instance = TRLinkRequiredAction.from_json(json)
# print the JSON string representation of the object
print(TRLinkRequiredAction.to_json())

# convert the object into a dict
tr_link_required_action_dict = tr_link_required_action_instance.to_dict()
# create an instance of TRLinkRequiredAction from a dict
tr_link_required_action_from_dict = TRLinkRequiredAction.from_dict(tr_link_required_action_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


