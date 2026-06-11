# StakingPositionRelatedTransactionsPaginatedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[PositionRelatedTransaction]**](PositionRelatedTransaction.md) | The related transactions for the current page. | 
**next** | **str** | Cursor for the next page. Use this value in the pageCursor parameter to fetch the next page. Null if no more pages. | [optional] 

## Example

```python
from fireblocks.models.staking_position_related_transactions_paginated_response import StakingPositionRelatedTransactionsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of StakingPositionRelatedTransactionsPaginatedResponse from a JSON string
staking_position_related_transactions_paginated_response_instance = StakingPositionRelatedTransactionsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(StakingPositionRelatedTransactionsPaginatedResponse.to_json())

# convert the object into a dict
staking_position_related_transactions_paginated_response_dict = staking_position_related_transactions_paginated_response_instance.to_dict()
# create an instance of StakingPositionRelatedTransactionsPaginatedResponse from a dict
staking_position_related_transactions_paginated_response_from_dict = StakingPositionRelatedTransactionsPaginatedResponse.from_dict(staking_position_related_transactions_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


