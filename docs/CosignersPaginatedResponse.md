# CosignersPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Cosigner]**](Cosigner.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks_client.models.cosigners_paginated_response import CosignersPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CosignersPaginatedResponse from a JSON string
cosigners_paginated_response_instance = CosignersPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print CosignersPaginatedResponse.to_json()

# convert the object into a dict
cosigners_paginated_response_dict = cosigners_paginated_response_instance.to_dict()
# create an instance of CosignersPaginatedResponse from a dict
cosigners_paginated_response_form_dict = cosigners_paginated_response.from_dict(cosigners_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


