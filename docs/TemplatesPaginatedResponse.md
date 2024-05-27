# TemplatesPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[LeanContractDto]**](LeanContractDto.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks_client.models.templates_paginated_response import TemplatesPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TemplatesPaginatedResponse from a JSON string
templates_paginated_response_instance = TemplatesPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print TemplatesPaginatedResponse.to_json()

# convert the object into a dict
templates_paginated_response_dict = templates_paginated_response_instance.to_dict()
# create an instance of TemplatesPaginatedResponse from a dict
templates_paginated_response_form_dict = templates_paginated_response.from_dict(templates_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


