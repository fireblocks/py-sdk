# ApiUsersPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CosignerApiUser]**](CosignerApiUser.md) | The data of the current page | 
**next** | **str** | The ID of the next page | [optional] 

## Example

```python
from fireblocks.models.api_users_paginated_response import ApiUsersPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersPaginatedResponse from a JSON string
api_users_paginated_response_instance = ApiUsersPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(ApiUsersPaginatedResponse.to_json())

# convert the object into a dict
api_users_paginated_response_dict = api_users_paginated_response_instance.to_dict()
# create an instance of ApiUsersPaginatedResponse from a dict
api_users_paginated_response_from_dict = ApiUsersPaginatedResponse.from_dict(api_users_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


