# PairApiKeyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique identifier of the API key | 
**callback_handler** | [**CallbackHandlerRequest**](CallbackHandlerRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.pair_api_key_response import PairApiKeyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of PairApiKeyResponse from a JSON string
pair_api_key_response_instance = PairApiKeyResponse.from_json(json)
# print the JSON string representation of the object
print(PairApiKeyResponse.to_json())

# convert the object into a dict
pair_api_key_response_dict = pair_api_key_response_instance.to_dict()
# create an instance of PairApiKeyResponse from a dict
pair_api_key_response_from_dict = PairApiKeyResponse.from_dict(pair_api_key_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


