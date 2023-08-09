# UpdateDraftRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rules** | [**List[PolicyRule]**](PolicyRule.md) | rules to update the draft with | [optional] 

## Example

```python
from fireblocks_client.models.update_draft_request import UpdateDraftRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDraftRequest from a JSON string
update_draft_request_instance = UpdateDraftRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDraftRequest.to_json()

# convert the object into a dict
update_draft_request_dict = update_draft_request_instance.to_dict()
# create an instance of UpdateDraftRequest from a dict
update_draft_request_form_dict = update_draft_request.from_dict(update_draft_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


