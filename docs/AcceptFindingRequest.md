# AcceptFindingRequest

Request to accept a FSPM finding. A reason is required.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Marks the finding as accepted. | 
**status_updated_reason** | **str** | The reason for accepting the finding. | 

## Example

```python
from fireblocks.models.accept_finding_request import AcceptFindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptFindingRequest from a JSON string
accept_finding_request_instance = AcceptFindingRequest.from_json(json)
# print the JSON string representation of the object
print(AcceptFindingRequest.to_json())

# convert the object into a dict
accept_finding_request_dict = accept_finding_request_instance.to_dict()
# create an instance of AcceptFindingRequest from a dict
accept_finding_request_from_dict = AcceptFindingRequest.from_dict(accept_finding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


