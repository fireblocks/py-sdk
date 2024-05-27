# SetOtaStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message indicating the result of the operation for example when no config change is needed | [optional] 

## Example

```python
from fireblocks_client.models.set_ota_status_response import SetOtaStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SetOtaStatusResponse from a JSON string
set_ota_status_response_instance = SetOtaStatusResponse.from_json(json)
# print the JSON string representation of the object
print SetOtaStatusResponse.to_json()

# convert the object into a dict
set_ota_status_response_dict = set_ota_status_response_instance.to_dict()
# create an instance of SetOtaStatusResponse from a dict
set_ota_status_response_form_dict = set_ota_status_response.from_dict(set_ota_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


