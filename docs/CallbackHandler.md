# CallbackHandler


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** | The callback handler&#39;s URL | 
**public_key** | **str** | The callback handler&#39;s public key | [optional] 
**cert_public_key_hash** | **str** | A hashed representation of the public key of the callback handler&#39;s certificate | [optional] 

## Example

```python
from fireblocks.models.callback_handler import CallbackHandler

# TODO update the JSON string below
json = "{}"
# create an instance of CallbackHandler from a JSON string
callback_handler_instance = CallbackHandler.from_json(json)
# print the JSON string representation of the object
print(CallbackHandler.to_json())

# convert the object into a dict
callback_handler_dict = callback_handler_instance.to_dict()
# create an instance of CallbackHandler from a dict
callback_handler_from_dict = CallbackHandler.from_dict(callback_handler_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


