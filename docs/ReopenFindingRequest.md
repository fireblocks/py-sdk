# ReopenFindingRequest

Request to reopen a FSPM finding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Marks the finding as open again. | 
**status_updated_reason** | **str** | Ignored when reopening a finding. | [optional] 

## Example

```python
from fireblocks.models.reopen_finding_request import ReopenFindingRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ReopenFindingRequest from a JSON string
reopen_finding_request_instance = ReopenFindingRequest.from_json(json)
# print the JSON string representation of the object
print(ReopenFindingRequest.to_json())

# convert the object into a dict
reopen_finding_request_dict = reopen_finding_request_instance.to_dict()
# create an instance of ReopenFindingRequest from a dict
reopen_finding_request_from_dict = ReopenFindingRequest.from_dict(reopen_finding_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


