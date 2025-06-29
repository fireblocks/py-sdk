# SwapOperationsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[SwapOperation]**](SwapOperation.md) | The data of the current page | 
**next** | **str** | The cursor to fetch the next page of results, if absent or null, there are no additional results. | [optional] 

## Example

```python
from fireblocks.models.swap_operations_paginated_response import SwapOperationsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwapOperationsPaginatedResponse from a JSON string
swap_operations_paginated_response_instance = SwapOperationsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(SwapOperationsPaginatedResponse.to_json())

# convert the object into a dict
swap_operations_paginated_response_dict = swap_operations_paginated_response_instance.to_dict()
# create an instance of SwapOperationsPaginatedResponse from a dict
swap_operations_paginated_response_from_dict = SwapOperationsPaginatedResponse.from_dict(swap_operations_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


