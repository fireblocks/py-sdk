# TRLinkGetRequiredActionsResponse

Response containing the list of required actions for a TRM

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**actions** | [**List[TRLinkRequiredAction]**](TRLinkRequiredAction.md) | List of required actions for the TRM | 

## Example

```python
from fireblocks.models.tr_link_get_required_actions_response import TRLinkGetRequiredActionsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkGetRequiredActionsResponse from a JSON string
tr_link_get_required_actions_response_instance = TRLinkGetRequiredActionsResponse.from_json(json)
# print the JSON string representation of the object
print(TRLinkGetRequiredActionsResponse.to_json())

# convert the object into a dict
tr_link_get_required_actions_response_dict = tr_link_get_required_actions_response_instance.to_dict()
# create an instance of TRLinkGetRequiredActionsResponse from a dict
tr_link_get_required_actions_response_from_dict = TRLinkGetRequiredActionsResponse.from_dict(tr_link_get_required_actions_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


