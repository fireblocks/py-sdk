# SetConfirmationsThresholdRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**num_of_confirmations** | **float** |  | [optional] 

## Example

```python
from fireblocks_client.models.set_confirmations_threshold_request import SetConfirmationsThresholdRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetConfirmationsThresholdRequest from a JSON string
set_confirmations_threshold_request_instance = SetConfirmationsThresholdRequest.from_json(json)
# print the JSON string representation of the object
print(SetConfirmationsThresholdRequest.to_json())

# convert the object into a dict
set_confirmations_threshold_request_dict = set_confirmations_threshold_request_instance.to_dict()
# create an instance of SetConfirmationsThresholdRequest from a dict
set_confirmations_threshold_request_from_dict = SetConfirmationsThresholdRequest.from_dict(set_confirmations_threshold_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


