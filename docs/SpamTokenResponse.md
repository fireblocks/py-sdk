# SpamTokenResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **bool** | Token spam result | 

## Example

```python
from fireblocks_client.models.spam_token_response import SpamTokenResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SpamTokenResponse from a JSON string
spam_token_response_instance = SpamTokenResponse.from_json(json)
# print the JSON string representation of the object
print(SpamTokenResponse.to_json())

# convert the object into a dict
spam_token_response_dict = spam_token_response_instance.to_dict()
# create an instance of SpamTokenResponse from a dict
spam_token_response_from_dict = SpamTokenResponse.from_dict(spam_token_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


