# SetConfirmationsThresholdResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**transactions** | **List[str]** |  | [optional] 

## Example

```python
from fireblocks_client.models.set_confirmations_threshold_response import SetConfirmationsThresholdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetConfirmationsThresholdResponse from a JSON string
set_confirmations_threshold_response_instance = SetConfirmationsThresholdResponse.from_json(json)
# print the JSON string representation of the object
print SetConfirmationsThresholdResponse.to_json()

# convert the object into a dict
set_confirmations_threshold_response_dict = set_confirmations_threshold_response_instance.to_dict()
# create an instance of SetConfirmationsThresholdResponse from a dict
set_confirmations_threshold_response_form_dict = set_confirmations_threshold_response.from_dict(set_confirmations_threshold_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


