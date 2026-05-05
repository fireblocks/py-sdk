# CounterpartyGroupsPaginatedResponse

Paginated list of counterparty groups

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[CounterpartyGroup]**](CounterpartyGroup.md) | The counterparty groups in the current page | 
**total** | **int** | Total number of counterparty groups | [optional] 
**next** | **str** | Cursor for the next page | [optional] 

## Example

```python
from fireblocks.models.counterparty_groups_paginated_response import CounterpartyGroupsPaginatedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of CounterpartyGroupsPaginatedResponse from a JSON string
counterparty_groups_paginated_response_instance = CounterpartyGroupsPaginatedResponse.from_json(json)
# print the JSON string representation of the object
print(CounterpartyGroupsPaginatedResponse.to_json())

# convert the object into a dict
counterparty_groups_paginated_response_dict = counterparty_groups_paginated_response_instance.to_dict()
# create an instance of CounterpartyGroupsPaginatedResponse from a dict
counterparty_groups_paginated_response_from_dict = CounterpartyGroupsPaginatedResponse.from_dict(counterparty_groups_paginated_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


