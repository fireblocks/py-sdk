# PairApiUserResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the API user | 
**callback_handler** | [**CallbackHandlerRequest**](CallbackHandlerRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.pair_api_user_response import PairApiUserResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PairApiUserResponse from a JSON string
pair_api_user_response_instance = PairApiUserResponse.from_json(json)
# print the JSON string representation of the object
print(PairApiUserResponse.to_json())

# convert the object into a dict
pair_api_user_response_dict = pair_api_user_response_instance.to_dict()
# create an instance of PairApiUserResponse from a dict
pair_api_user_response_from_dict = PairApiUserResponse.from_dict(pair_api_user_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


