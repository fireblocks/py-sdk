# UpdateDraftRequest

Request schema for updating draft with policy types and rules

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**policy_types** | [**List[PolicyType]**](PolicyType.md) |  | 
**rules** | [**List[PolicyRule]**](PolicyRule.md) | Array of policy rules | 

## Example

```python
from fireblocks.models.update_draft_request import UpdateDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDraftRequest from a JSON string
update_draft_request_instance = UpdateDraftRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateDraftRequest.to_json())

# convert the object into a dict
update_draft_request_dict = update_draft_request_instance.to_dict()
# create an instance of UpdateDraftRequest from a dict
update_draft_request_from_dict = UpdateDraftRequest.from_dict(update_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


