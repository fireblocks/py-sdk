# PairApiKeyRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**callback_handler** | [**CallbackHandlerRequest**](CallbackHandlerRequest.md) |  | [optional] 

## Example

```python
from fireblocks.models.pair_api_key_request import PairApiKeyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PairApiKeyRequest from a JSON string
pair_api_key_request_instance = PairApiKeyRequest.from_json(json)
# print the JSON string representation of the object
print(PairApiKeyRequest.to_json())

# convert the object into a dict
pair_api_key_request_dict = pair_api_key_request_instance.to_dict()
# create an instance of PairApiKeyRequest from a dict
pair_api_key_request_from_dict = PairApiKeyRequest.from_dict(pair_api_key_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


