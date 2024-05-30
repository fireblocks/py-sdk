# SmartTransferForbiddenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Forbidden error code | 
**code** | **str** | Error code | 

## Example

```python
from fireblocks.models.smart_transfer_forbidden_response import SmartTransferForbiddenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferForbiddenResponse from a JSON string
smart_transfer_forbidden_response_instance = SmartTransferForbiddenResponse.from_json(json)
# print the JSON string representation of the object
print(SmartTransferForbiddenResponse.to_json())

# convert the object into a dict
smart_transfer_forbidden_response_dict = smart_transfer_forbidden_response_instance.to_dict()
# create an instance of SmartTransferForbiddenResponse from a dict
smart_transfer_forbidden_response_from_dict = SmartTransferForbiddenResponse.from_dict(smart_transfer_forbidden_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


