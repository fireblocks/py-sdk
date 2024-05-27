# ApiKeysPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[ApiKey]**](ApiKey.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks_client.models.api_keys_paginated_response import ApiKeysPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiKeysPaginatedResponse from a JSON string
api_keys_paginated_response_instance = ApiKeysPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print ApiKeysPaginatedResponse.to_json()

# convert the object into a dict
api_keys_paginated_response_dict = api_keys_paginated_response_instance.to_dict()
# create an instance of ApiKeysPaginatedResponse from a dict
api_keys_paginated_response_form_dict = api_keys_paginated_response.from_dict(api_keys_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


