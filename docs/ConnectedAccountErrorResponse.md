# ConnectedAccountErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error message describing what went wrong | 
**error_code** | **str** | Error code identifying the type of error | 

## Example

```python
from fireblocks.models.connected_account_error_response import ConnectedAccountErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ConnectedAccountErrorResponse from a JSON string
connected_account_error_response_instance = ConnectedAccountErrorResponse.from_json(json)
# print the JSON string representation of the object
print(ConnectedAccountErrorResponse.to_json())

# convert the object into a dict
connected_account_error_response_dict = connected_account_error_response_instance.to_dict()
# create an instance of ConnectedAccountErrorResponse from a dict
connected_account_error_response_from_dict = ConnectedAccountErrorResponse.from_dict(connected_account_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


