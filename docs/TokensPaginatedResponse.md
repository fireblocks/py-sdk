# TokensPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[TokenLinkDto]**](TokenLinkDto.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks_client.models.tokens_paginated_response import TokensPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TokensPaginatedResponse from a JSON string
tokens_paginated_response_instance = TokensPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print TokensPaginatedResponse.to_json()

# convert the object into a dict
tokens_paginated_response_dict = tokens_paginated_response_instance.to_dict()
# create an instance of TokensPaginatedResponse from a dict
tokens_paginated_response_form_dict = tokens_paginated_response.from_dict(tokens_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


