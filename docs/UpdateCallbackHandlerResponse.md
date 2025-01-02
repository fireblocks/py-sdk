# UpdateCallbackHandlerResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the API key | 
**callback_handler** | [**CallbackHandlerRequest**](CallbackHandlerRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.update_callback_handler_response import UpdateCallbackHandlerResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateCallbackHandlerResponse from a JSON string
update_callback_handler_response_instance = UpdateCallbackHandlerResponse.from_json(json)
# print the JSON string representation of the object
print(UpdateCallbackHandlerResponse.to_json())

# convert the object into a dict
update_callback_handler_response_dict = update_callback_handler_response_instance.to_dict()
# create an instance of UpdateCallbackHandlerResponse from a dict
update_callback_handler_response_from_dict = UpdateCallbackHandlerResponse.from_dict(update_callback_handler_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


