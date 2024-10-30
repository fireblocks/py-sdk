# SmartTransferStatistic

Smart transfers statistic

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inflow** | [**SmartTransferStatisticInflow**](SmartTransferStatisticInflow.md) |  | 
**outflow** | [**SmartTransferStatisticOutflow**](SmartTransferStatisticOutflow.md) |  | 
**total_active_tickets** | **int** | Number of total active tickets | 
**total_inactive_tickets** | **int** | Number of total inactive tickets (expired, canceled, completed) | 

## Example

```python
from fireblocks.models.smart_transfer_statistic import SmartTransferStatistic

# TODO update the JSON string below
json = "{}"
# create an instance of SmartTransferStatistic from a JSON string
smart_transfer_statistic_instance = SmartTransferStatistic.from_json(json)
# print the JSON string representation of the object
print(SmartTransferStatistic.to_json())

# convert the object into a dict
smart_transfer_statistic_dict = smart_transfer_statistic_instance.to_dict()
# create an instance of SmartTransferStatistic from a dict
smart_transfer_statistic_from_dict = SmartTransferStatistic.from_dict(smart_transfer_statistic_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


