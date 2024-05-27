# SetAdminQuorumThresholdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | The message which indicates the result of the operation. | 

## Example

```python
from fireblocks_client.models.set_admin_quorum_threshold_response import SetAdminQuorumThresholdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetAdminQuorumThresholdResponse from a JSON string
set_admin_quorum_threshold_response_instance = SetAdminQuorumThresholdResponse.from_json(json)
# print the JSON string representation of the object
print SetAdminQuorumThresholdResponse.to_json()

# convert the object into a dict
set_admin_quorum_threshold_response_dict = set_admin_quorum_threshold_response_instance.to_dict()
# create an instance of SetAdminQuorumThresholdResponse from a dict
set_admin_quorum_threshold_response_form_dict = set_admin_quorum_threshold_response.from_dict(set_admin_quorum_threshold_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


