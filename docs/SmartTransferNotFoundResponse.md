# SmartTransferNotFoundResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Not found error message | 
**code** | **str** | Error code | 

## Example

```python
from fireblocks_client.models.smart_transfer_not_found_response import SmartTransferNotFoundResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferNotFoundResponse from a JSON string
smart_transfer_not_found_response_instance = SmartTransferNotFoundResponse.from_json(json)
# print the JSON string representation of the object
print(SmartTransferNotFoundResponse.to_json())

# convert the object into a dict
smart_transfer_not_found_response_dict = smart_transfer_not_found_response_instance.to_dict()
# create an instance of SmartTransferNotFoundResponse from a dict
smart_transfer_not_found_response_from_dict = SmartTransferNotFoundResponse.from_dict(smart_transfer_not_found_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


