# CallbackHandlerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The callback handler&#39;s URL | 
**public_key** | **str** | The callback handler&#39;s public key | [optional] 
**cert** | **str** | The callback handler&#39;s certificate | [optional] 

## Example

```python
from fireblocks.models.callback_handler_request import CallbackHandlerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackHandlerRequest from a JSON string
callback_handler_request_instance = CallbackHandlerRequest.from_json(json)
# print the JSON string representation of the object
print(CallbackHandlerRequest.to_json())

# convert the object into a dict
callback_handler_request_dict = callback_handler_request_instance.to_dict()
# create an instance of CallbackHandlerRequest from a dict
callback_handler_request_from_dict = CallbackHandlerRequest.from_dict(callback_handler_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


