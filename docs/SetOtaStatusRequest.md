# SetOtaStatusRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Set true or false to enable or disable OTA transactions | [optional] 

## Example

```python
from fireblocks_client.models.set_ota_status_request import SetOtaStatusRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SetOtaStatusRequest from a JSON string
set_ota_status_request_instance = SetOtaStatusRequest.from_json(json)
# print the JSON string representation of the object
print(SetOtaStatusRequest.to_json())

# convert the object into a dict
set_ota_status_request_dict = set_ota_status_request_instance.to_dict()
# create an instance of SetOtaStatusRequest from a dict
set_ota_status_request_from_dict = SetOtaStatusRequest.from_dict(set_ota_status_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


