# TRLinkResolveActionRequest

Request to resolve a pending TRM action

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** | The action type identifier as defined by the Travel Rule provider. Must match one of the types returned by the get required actions endpoint. Values are provider-specific and may vary across different TRP implementations. | 
**data** | [**TRLinkResolveActionData**](TRLinkResolveActionData.md) |  | [optional] 

## Example

```python
from fireblocks.models.tr_link_resolve_action_request import TRLinkResolveActionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TRLinkResolveActionRequest from a JSON string
tr_link_resolve_action_request_instance = TRLinkResolveActionRequest.from_json(json)
# print the JSON string representation of the object
print(TRLinkResolveActionRequest.to_json())

# convert the object into a dict
tr_link_resolve_action_request_dict = tr_link_resolve_action_request_instance.to_dict()
# create an instance of TRLinkResolveActionRequest from a dict
tr_link_resolve_action_request_from_dict = TRLinkResolveActionRequest.from_dict(tr_link_resolve_action_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


