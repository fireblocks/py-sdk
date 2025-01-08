# UpdateCallbackHandlerRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_handler** | [**CallbackHandlerRequest**](CallbackHandlerRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.update_callback_handler_request import UpdateCallbackHandlerRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCallbackHandlerRequest from a JSON string
update_callback_handler_request_instance = UpdateCallbackHandlerRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateCallbackHandlerRequest.to_json())

# convert the object into a dict
update_callback_handler_request_dict = update_callback_handler_request_instance.to_dict()
# create an instance of UpdateCallbackHandlerRequest from a dict
update_callback_handler_request_from_dict = UpdateCallbackHandlerRequest.from_dict(update_callback_handler_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


