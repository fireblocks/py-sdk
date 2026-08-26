# UpdateFindingExternalRequest

Request to update the status of a FSPM finding. Only OPEN (reopen) and ACCEPTED (accept) are settable; findings become RESOLVED via automated detection, not through this API. `statusUpdatedReason` is required when accepting a finding and ignored when reopening.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **str** | Marks the finding as open again. | 
**status_updated_reason** | **str** | Ignored when reopening a finding. | 

## Example

```python
from fireblocks.models.update_finding_external_request import UpdateFindingExternalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateFindingExternalRequest from a JSON string
update_finding_external_request_instance = UpdateFindingExternalRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateFindingExternalRequest.to_json())

# convert the object into a dict
update_finding_external_request_dict = update_finding_external_request_instance.to_dict()
# create an instance of UpdateFindingExternalRequest from a dict
update_finding_external_request_from_dict = UpdateFindingExternalRequest.from_dict(update_finding_external_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


