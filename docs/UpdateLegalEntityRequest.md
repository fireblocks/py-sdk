# UpdateLegalEntityRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_default** | **bool** | Whether to set this registration as the workspace default | 

## Example

```python
from fireblocks.models.update_legal_entity_request import UpdateLegalEntityRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateLegalEntityRequest from a JSON string
update_legal_entity_request_instance = UpdateLegalEntityRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateLegalEntityRequest.to_json())

# convert the object into a dict
update_legal_entity_request_dict = update_legal_entity_request_instance.to_dict()
# create an instance of UpdateLegalEntityRequest from a dict
update_legal_entity_request_from_dict = UpdateLegalEntityRequest.from_dict(update_legal_entity_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


