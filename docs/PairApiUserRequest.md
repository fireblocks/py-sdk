# PairApiUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_handler** | [**CallbackHandlerRequest**](CallbackHandlerRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.pair_api_user_request import PairApiUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PairApiUserRequest from a JSON string
pair_api_user_request_instance = PairApiUserRequest.from_json(json)
# print the JSON string representation of the object
print(PairApiUserRequest.to_json())

# convert the object into a dict
pair_api_user_request_dict = pair_api_user_request_instance.to_dict()
# create an instance of PairApiUserRequest from a dict
pair_api_user_request_from_dict = PairApiUserRequest.from_dict(pair_api_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


