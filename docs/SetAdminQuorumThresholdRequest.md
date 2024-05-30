# SetAdminQuorumThresholdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_quorum_threshold** | **float** | The number of admins that will requires to approve an operation | [optional] 

## Example

```python
from fireblocks_client.models.set_admin_quorum_threshold_request import SetAdminQuorumThresholdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetAdminQuorumThresholdRequest from a JSON string
set_admin_quorum_threshold_request_instance = SetAdminQuorumThresholdRequest.from_json(json)
# print the JSON string representation of the object
print(SetAdminQuorumThresholdRequest.to_json())

# convert the object into a dict
set_admin_quorum_threshold_request_dict = set_admin_quorum_threshold_request_instance.to_dict()
# create an instance of SetAdminQuorumThresholdRequest from a dict
set_admin_quorum_threshold_request_from_dict = SetAdminQuorumThresholdRequest.from_dict(set_admin_quorum_threshold_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


