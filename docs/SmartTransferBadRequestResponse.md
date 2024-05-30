# SmartTransferBadRequestResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Bad request error message | 
**code** | **str** | Bad request error code | 

## Example

```python
from fireblocks.models.smart_transfer_bad_request_response import SmartTransferBadRequestResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferBadRequestResponse from a JSON string
smart_transfer_bad_request_response_instance = SmartTransferBadRequestResponse.from_json(json)
# print the JSON string representation of the object
print(SmartTransferBadRequestResponse.to_json())

# convert the object into a dict
smart_transfer_bad_request_response_dict = smart_transfer_bad_request_response_instance.to_dict()
# create an instance of SmartTransferBadRequestResponse from a dict
smart_transfer_bad_request_response_from_dict = SmartTransferBadRequestResponse.from_dict(smart_transfer_bad_request_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


