# SwapProvidersPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SwapProvider]**](SwapProvider.md) | The data of the current page | 
**next** | **str** | The cursor to fetch the next page of results, if absent or null, there are no additional results. | [optional] 

## Example

```python
from fireblocks.models.swap_providers_paginated_response import SwapProvidersPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwapProvidersPaginatedResponse from a JSON string
swap_providers_paginated_response_instance = SwapProvidersPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SwapProvidersPaginatedResponse.to_json())

# convert the object into a dict
swap_providers_paginated_response_dict = swap_providers_paginated_response_instance.to_dict()
# create an instance of SwapProvidersPaginatedResponse from a dict
swap_providers_paginated_response_from_dict = SwapProvidersPaginatedResponse.from_dict(swap_providers_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


