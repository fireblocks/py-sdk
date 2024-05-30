# SetOtaStatusResponseOneOf


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Message indicating the result of the operation for example when no config change is needed | [optional] 

## Example

```python
from fireblocks.models.set_ota_status_response_one_of import SetOtaStatusResponseOneOf

# TODO update the JSON string below
json = "{}"
# create an instance of SetOtaStatusResponseOneOf from a JSON string
set_ota_status_response_one_of_instance = SetOtaStatusResponseOneOf.from_json(json)
# print the JSON string representation of the object
print(SetOtaStatusResponseOneOf.to_json())

# convert the object into a dict
set_ota_status_response_one_of_dict = set_ota_status_response_one_of_instance.to_dict()
# create an instance of SetOtaStatusResponseOneOf from a dict
set_ota_status_response_one_of_from_dict = SetOtaStatusResponseOneOf.from_dict(set_ota_status_response_one_of_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


