# StakingPositionsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Position]**](Position.md) | The data of the current page of staking positions | 
**next** | **str** | The cursor for the next page | [optional] 

## Example

```python
from fireblocks.models.staking_positions_paginated_response import StakingPositionsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StakingPositionsPaginatedResponse from a JSON string
staking_positions_paginated_response_instance = StakingPositionsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(StakingPositionsPaginatedResponse.to_json())

# convert the object into a dict
staking_positions_paginated_response_dict = staking_positions_paginated_response_instance.to_dict()
# create an instance of StakingPositionsPaginatedResponse from a dict
staking_positions_paginated_response_from_dict = StakingPositionsPaginatedResponse.from_dict(staking_positions_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


