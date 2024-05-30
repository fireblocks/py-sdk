# GetOtaStatusResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | Current OTA status | [optional] 

## Example

```python
from fireblocks.models.get_ota_status_response import GetOtaStatusResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetOtaStatusResponse from a JSON string
get_ota_status_response_instance = GetOtaStatusResponse.from_json(json)
# print the JSON string representation of the object
print(GetOtaStatusResponse.to_json())

# convert the object into a dict
get_ota_status_response_dict = get_ota_status_response_instance.to_dict()
# create an instance of GetOtaStatusResponse from a dict
get_ota_status_response_from_dict = GetOtaStatusResponse.from_dict(get_ota_status_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


